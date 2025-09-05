#!/usr/bin/env python3
"""
Comprehensive Link Audit - Check that every job has a proper clickable URL
"""

import sys
import os
import re

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Mock the telegram functions to avoid sending messages during testing
def mock_send_telegram_message(message):
    pass

def mock_send_job_summary(jobs):
    pass

import telegram_bot
telegram_bot.send_telegram_message = mock_send_telegram_message
telegram_bot.send_job_summary = mock_send_job_summary

from telegram_jobs import JobScout

def is_valid_url(url):
    """Check if URL is valid and clickable"""
    if not url or not isinstance(url, str):
        return False, "Missing or invalid URL"
    
    url = url.strip()
    if not url:
        return False, "Empty URL"
    
    # Check for placeholder URLs
    placeholder_patterns = [
        r'example\.com',
        r'example-.*\.com',
        r'company\.com',
        r'^#$',
        r'^N/A$',
        r'^\.$',
        r'^-$'
    ]
    
    for pattern in placeholder_patterns:
        if re.search(pattern, url, re.IGNORECASE):
            return False, f"Placeholder URL: {url}"
    
    # Check if URL starts with http/https
    if not url.startswith(('http://', 'https://')):
        return False, f"Invalid URL format (missing protocol): {url}"
    
    # Check for obviously broken URLs
    if len(url) < 10:  # Very short URLs are likely broken
        return False, f"URL too short: {url}"
    
    return True, "Valid URL"

def audit_all_job_functions():
    """Audit all job functions for link issues"""
    scout = JobScout()
    test_keywords = ["remote", "developer", "support", "assistant", "data", "python", "javascript"]
    
    print("🔗 COMPREHENSIVE JOB LINK AUDIT")
    print("=" * 60)
    
    # Get all methods that start with 'fetch_'
    fetch_methods = [method for method in dir(scout) if method.startswith('fetch_') and callable(getattr(scout, method))]
    
    all_issues = []
    total_jobs = 0
    jobs_with_issues = 0
    
    for method_name in sorted(fetch_methods):
        try:
            method = getattr(scout, method_name)
            jobs = method(test_keywords)
            
            print(f"\n📋 {method_name}: {len(jobs)} jobs")
            
            method_issues = []
            
            for i, job in enumerate(jobs):
                total_jobs += 1
                
                # Check if job has URL field
                if 'url' not in job:
                    issue = {
                        'function': method_name,
                        'job_index': i + 1,
                        'job_title': job.get('title', 'No title'),
                        'issue_type': 'missing_url_field',
                        'issue_description': 'Job missing URL field',
                        'job_data': job
                    }
                    method_issues.append(issue)
                    print(f"  ❌ Job {i+1}: Missing URL field - {job.get('title', 'No title')}")
                    continue
                
                # Validate URL
                is_valid, validation_message = is_valid_url(job['url'])
                
                if not is_valid:
                    issue = {
                        'function': method_name,
                        'job_index': i + 1,
                        'job_title': job.get('title', 'No title'),
                        'issue_type': 'invalid_url',
                        'issue_description': validation_message,
                        'current_url': job['url'],
                        'job_data': job
                    }
                    method_issues.append(issue)
                    print(f"  ❌ Job {i+1}: {validation_message} - {job.get('title', 'No title')}")
                else:
                    print(f"  ✅ Job {i+1}: Valid URL - {job.get('title', 'No title')}")
            
            if method_issues:
                jobs_with_issues += len(method_issues)
                all_issues.extend(method_issues)
                
        except Exception as e:
            print(f"❌ Error testing {method_name}: {e}")
            issue = {
                'function': method_name,
                'job_index': 'N/A',
                'job_title': 'Function Error',
                'issue_type': 'function_error',
                'issue_description': f'Function failed: {str(e)}',
                'job_data': None
            }
            all_issues.append(issue)
    
    # Summary Report
    print(f"\n📊 COMPREHENSIVE AUDIT SUMMARY")
    print("=" * 40)
    print(f"Total jobs audited: {total_jobs}")
    print(f"Jobs with link issues: {jobs_with_issues}")
    print(f"Jobs with valid links: {total_jobs - jobs_with_issues}")
    print(f"Success rate: {((total_jobs - jobs_with_issues) / total_jobs * 100):.1f}%" if total_jobs > 0 else "N/A")
    
    if all_issues:
        print(f"\n🚨 DETAILED ISSUES REPORT ({len(all_issues)} issues):")
        print("-" * 50)
        
        # Group issues by type
        issues_by_type = {}
        for issue in all_issues:
            issue_type = issue['issue_type']
            if issue_type not in issues_by_type:
                issues_by_type[issue_type] = []
            issues_by_type[issue_type].append(issue)
        
        for issue_type, issues in issues_by_type.items():
            print(f"\n{issue_type.upper().replace('_', ' ')} ({len(issues)} issues):")
            for issue in issues:
                print(f"  • {issue['function']} - Job {issue['job_index']}: {issue['job_title']}")
                print(f"    Issue: {issue['issue_description']}")
                if 'current_url' in issue:
                    print(f"    Current URL: {issue['current_url']}")
        
        # Generate fix suggestions
        print(f"\n🔧 FIX SUGGESTIONS:")
        print("-" * 20)
        
        for issue in all_issues:
            if issue['issue_type'] in ['missing_url_field', 'invalid_url']:
                function_name = issue['function']
                job_title = issue['job_title']
                
                # Suggest appropriate URLs based on job type and function
                suggested_url = suggest_url_for_job(function_name, job_title)
                print(f"• {function_name} - {job_title}:")
                print(f"  Suggested URL: {suggested_url}")
    
    else:
        print("\n✅ ALL JOBS HAVE VALID LINKS!")
    
    return all_issues

def suggest_url_for_job(function_name, job_title):
    """Suggest appropriate URLs based on function name and job title"""
    
    # URL suggestions based on function patterns
    url_suggestions = {
        'gitlab': 'https://about.gitlab.com/jobs/',
        'automattic': 'https://automattic.com/work-with-us/',
        'zapier': 'https://zapier.com/jobs',
        'buffer': 'https://buffer.com/journey',
        'doist': 'https://doist.com/careers',
        'remote_com': 'https://remote.com/jobs',
        'deel': 'https://deel.com/careers',
        'sales': 'https://remoteok.io/remote-sales-jobs',
        'product': 'https://remoteok.io/remote-product-manager-jobs',
        'ecommerce': 'https://www.upwork.com/freelance-jobs/ecommerce/',
        'healthcare': 'https://www.flexjobs.com/remote-jobs/healthcare',
        'translation': 'https://www.gengo.com/translators/',
        'research': 'https://www.usertesting.com/get-paid-to-test',
        'customer_support': 'https://remoteok.io/remote-customer-support-jobs',
        'operations': 'https://remoteok.io/remote-operations-jobs',
        'hr': 'https://remoteok.io/remote-hr-jobs',
        'finance': 'https://remoteok.io/remote-finance-jobs',
        'technical_writing': 'https://remoteok.io/remote-technical-writer-jobs',
        'bpo': 'https://www.liveworld.com/careers/',
        'ai_training': 'https://www.appen.com/careers/',
        'freelance': 'https://www.upwork.com/',
        'va_support': 'https://www.belay.com/careers/',
        'content_moderation': 'https://modsquad.com/careers',
        'social_media': 'https://remoteok.io/remote-social-media-jobs',
        'platform_support': 'https://remoteok.io/remote-support-jobs',
        'ad_review': 'https://www.lionbridge.com/join-our-team/',
        'data_labeling': 'https://www.clickworker.com/',
        'creator_economy': 'https://www.patreon.com/careers',
        'gaming': 'https://careers.riotgames.com/',
        'chat_moderation': 'https://modsquad.com/careers'
    }
    
    # Find matching URL based on function name
    for key, url in url_suggestions.items():
        if key in function_name.lower():
            return url
    
    # Default fallback URLs based on job title keywords
    job_title_lower = job_title.lower()
    
    if any(word in job_title_lower for word in ['support', 'customer', 'help']):
        return 'https://remoteok.io/remote-customer-support-jobs'
    elif any(word in job_title_lower for word in ['developer', 'engineer', 'programmer']):
        return 'https://remoteok.io/remote-dev-jobs'
    elif any(word in job_title_lower for word in ['writer', 'content', 'blog']):
        return 'https://remoteok.io/remote-writing-jobs'
    elif any(word in job_title_lower for word in ['assistant', 'va', 'virtual']):
        return 'https://www.belay.com/careers/'
    elif any(word in job_title_lower for word in ['data', 'entry', 'analyst']):
        return 'https://www.clickworker.com/'
    elif any(word in job_title_lower for word in ['sales', 'business']):
        return 'https://remoteok.io/remote-sales-jobs'
    elif any(word in job_title_lower for word in ['manager', 'product']):
        return 'https://remoteok.io/remote-product-manager-jobs'
    else:
        return 'https://remoteok.io/remote-jobs'

if __name__ == "__main__":
    issues = audit_all_job_functions()
    
    if issues:
        print(f"\n⚠️ Found {len(issues)} jobs that need link fixes!")
        print("Run this script to identify specific jobs that need URL updates.")
    else:
        print(f"\n🎉 All jobs have valid, clickable links!")