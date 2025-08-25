"""
AWS Lambda handler for Agent-21 Scout Payment Bot
"""

import json
import os
import sqlite3
import boto3
from datetime import datetime
import re

# AWS Lambda handler
def lambda_handler(event, context):
    """Handle SMS webhook in AWS Lambda"""
    
    try:
        # Parse the incoming request
        if event.get('httpMethod') == 'POST':
            body = json.loads(event.get('body', '{}'))
            
            # Handle SMS webhook
            if event.get('path') == '/webhook/sms':
                return handle_sms_webhook(body)
            
            # Handle test webhook
            elif event.get('path') == '/webhook/test':
                return {
                    'statusCode': 200,
                    'body': json.dumps({
                        'status': 'success',
                        'message': 'Lambda webhook working!',
                        'timestamp': datetime.now().isoformat()
                    })
                }
        
        # Health check
        elif event.get('httpMethod') == 'GET' and event.get('path') == '/health':
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'status': 'healthy',
                    'service': 'Agent-21 Payment Lambda'
                })
            }
        
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Not found'})
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def handle_sms_webhook(data):
    """Process M-Pesa SMS webhook"""
    
    sms_text = data.get('message', '').lower()
    payment_amount = int(os.environ.get('PAYMENT_AMOUNT', '50'))
    
    # Check if it's M-Pesa confirmation
    if 'confirmed' in sms_text and f'ksh{payment_amount}' in sms_text.replace(' ', ''):
        
        # Extract reference code
        ref_match = re.search(r'reference[:\s]*(\d{6})', sms_text)
        
        if ref_match:
            reference_code = ref_match.group(1)
            
            # Send Telegram message via SNS or direct API call
            send_telegram_invite(reference_code)
            
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'status': 'success',
                    'message': 'Payment processed'
                })
            }
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'status': 'ignored',
            'message': 'SMS not relevant'
        })
    }

def send_telegram_invite(reference_code):
    """Send Telegram invite using AWS SNS or direct API"""
    
    # You can use AWS SNS to trigger another Lambda
    # or make direct Telegram API call here
    
    sns = boto3.client('sns')
    
    message = {
        'reference_code': reference_code,
        'action': 'send_invite'
    }
    
    sns.publish(
        TopicArn=os.environ.get('SNS_TOPIC_ARN'),
        Message=json.dumps(message)
    )