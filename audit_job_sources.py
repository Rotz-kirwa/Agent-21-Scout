#!/usr/bin/env python3
"""
Job Source Audit Script
Tests all existing fetch functions to identify failures and issues
"""

import sys
import os
import traceback
from datetime import datetime
import time

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Mock the telegram functions to avoid API calls during testing
def mock_send_telegram_message(message):
    pass

def mock_send_job_summary(jobs):
    pass

# Replace the telegram functions
import telegram_bot
telegram_bot.send_telegram_message = mock_send_telegram_message
telegram_bot.send_job_summary = mock_send_job_summary

# Import after mocking
from telegram_jobs import JobScout

class JobSourceAuditor:
    def __init__(self):
        self.scout = JobScout()
        self.results = {}
        self.test_keywords = ["remote", "developer", "support", "assistant", "data"]
    
    def test_fetch_function(self, func_name, *args, **kwargs):
        """Test a single fetch function and return results"""
        try:
            print(f"Testing {func_name}...", end=" ")
            start_time = time.time()
            
            # Get the function from the scout object
            func = getattr(self.scout, func_name)
            
            # Call the function
            jobs = func(*args, **kwargs)
            
            end_time = time.time()
            execution_time = end_time - start_time
            
            # Validate results
            if jobs is None:
                status = "FAILED"
                error = "Function returned None"
                job_count = 0
            elif not isinstance(jobs, list):
                status = "FAILED"
                error = f"Function returned {type(jobs)} instead of list"
                job_count = 0
            elif len(jobs) == 0:
                status = "WARNING"
                error = "Function returned empty list"
                job_count = 0
            else:
                status = "SUCCESS"
                error = None
                job_count = len(jobs)
                
                # Validate job structure
                for i, job in enumerate(jobs[:3]):  # Check first 3 jobs
                    if not isinstance(job, dict):
                        status = "FAILED"
                        error = f"Job {i} is not a dictionary: {type(job)}"
                        break
                    
                    required_fields = ['title', 'company', 'location', 'url', 'source']
                    missing_fields = [field for field in required_fields if field not in job]
                    if missing_fields:
                        status = "WARNING"
                        error = f"Job {i} missing fields: {missing_fields}"
                        break
            
            print(f"{status} ({job_count} jobs, {execution_time:.2f}s)")
            if error:
                print(f"  Error: {error}")
            
            return {
                'status': status,
                'job_count': job_count,
                'execution_time': execution_time,
                'error': error
            }
            
        except Exception as e:
            print(f"FAILED")
            error_msg = f"{type(e).__name__}: {str(e)}"
            print(f"  Error: {error_msg}")
            
            return {
                'status': 'FAILED',
                'job_count': 0,
                'execution_time': 0,
                'error': error_msg,
                'traceback': traceback.format_exc()
            }
    
    def audit_all_sources(self):
        """Audit all job source functions"""
        print("🔍 Starting Job Source Audit")
        print("=" * 60)
        print(f"Started at: {datetime.now()}")
        print()
        
        # List of all fetch functions to test
        fetch_functions = [
            # Core API functions
            ('fetch_remotive_jobs', 'remote'),
            ('fetch_reliable_jobs', self.test_keywords),
            ('fetch_wellfound_jobs', self.test_keywords),
            ('fetch_nowhiteboard_jobs', self.test_keywords),
            ('fetch_workingnomads_jobs', self.test_keywords),
            ('fetch_amazon_jobs', self.test_keywords),
            ('fetch_amazon_aws_jobs',),
            ('fetch_static_jobs', self.test_keywords),
            ('fetch_flexjobs_api', self.test_keywords),
            
            # Company-specific functions
            ('fetch_gitlab_jobs', self.test_keywords),
            ('fetch_automattic_jobs', self.test_keywords),
            ('fetch_zapier_jobs', self.test_keywords),
            ('fetch_buffer_jobs', self.test_keywords),
            ('fetch_doist_jobs', self.test_keywords),
            ('fetch_remote_com_jobs', self.test_keywords),
            ('fetch_deel_jobs', self.test_keywords),
            ('fetch_andela_jobs', self.test_keywords),
            ('fetch_crypto_jobs', self.test_keywords),
            ('fetch_wikimedia_jobs', self.test_keywords),
            
            # Category-specific functions
            ('fetch_customer_support_jobs', self.test_keywords),
            ('fetch_operations_hr_jobs', self.test_keywords),
            ('fetch_finance_jobs', self.test_keywords),
            ('fetch_technical_writing_jobs', self.test_keywords),
            
            # Specialized platform functions
            ('fetch_bpo_outsourcing_jobs', self.test_keywords),
            ('fetch_ai_training_jobs', self.test_keywords),
            ('fetch_freelance_gig_jobs', self.test_keywords),
            ('fetch_va_support_jobs', self.test_keywords),
            ('fetch_social_media_platform_jobs', self.test_keywords),
            ('fetch_customer_support_platform_jobs', self.test_keywords),
            ('fetch_ad_review_specialist_jobs', self.test_keywords),
            ('fetch_data_labeling_specialist_jobs', self.test_keywords),
            ('fetch_comprehensive_platform_jobs', self.test_keywords),
            ('fetch_creator_economy_jobs', self.test_keywords),
            ('fetch_gaming_platform_jobs', self.test_keywords),
            ('fetch_chat_moderation_jobs', self.test_keywords),
            ('fetch_social_platform_extended_jobs', self.test_keywords),
            
            # Sample and new category functions
            ('fetch_sample_specialized_jobs', self.test_keywords),
            ('fetch_sales_bizdev_jobs', self.test_keywords),
            ('fetch_product_management_jobs', self.test_keywords),
            ('fetch_ecommerce_jobs', self.test_keywords),
            ('fetch_healthcare_remote_jobs', self.test_keywords),
            ('fetch_translation_jobs', self.test_keywords),
            ('fetch_research_survey_jobs', self.test_keywords),
        ]
        
        # Test each function
        for func_info in fetch_functions:
            func_name = func_info[0]
            args = func_info[1:] if len(func_info) > 1 else ()
            
            result = self.test_fetch_function(func_name, *args)
            self.results[func_name] = result
            
            # Small delay between tests
            time.sleep(0.5)
        
        self.generate_audit_report()
    
    def generate_audit_report(self):
        """Generate comprehensive audit report"""
        print()
        print("=" * 60)
        print("📊 AUDIT REPORT SUMMARY")
        print("=" * 60)
        
        # Count results by status
        status_counts = {'SUCCESS': 0, 'WARNING': 0, 'FAILED': 0}
        total_jobs = 0
        total_time = 0
        
        for func_name, result in self.results.items():
            status_counts[result['status']] += 1
            total_jobs += result['job_count']
            total_time += result['execution_time']
        
        print(f"✅ Successful Sources: {status_counts['SUCCESS']}")
        print(f"⚠️  Warning Sources: {status_counts['WARNING']}")
        print(f"❌ Failed Sources: {status_counts['FAILED']}")
        print(f"📈 Total Jobs Found: {total_jobs}")
        print(f"⏱️  Total Execution Time: {total_time:.2f}s")
        print(f"📊 Success Rate: {(status_counts['SUCCESS'] / len(self.results)) * 100:.1f}%")
        
        # Detailed results
        print()
        print("🔍 DETAILED RESULTS:")
        print("-" * 60)
        
        # Group by status
        for status in ['FAILED', 'WARNING', 'SUCCESS']:
            functions_with_status = [(name, result) for name, result in self.results.items() 
                                   if result['status'] == status]
            
            if functions_with_status:
                status_emoji = {'SUCCESS': '✅', 'WARNING': '⚠️', 'FAILED': '❌'}[status]
                print(f"{status_emoji} {status} SOURCES ({len(functions_with_status)}):")
                
                for func_name, result in functions_with_status:
                    print(f"  • {func_name}: {result['job_count']} jobs ({result['execution_time']:.2f}s)")
                    if result['error']:
                        print(f"    Error: {result['error']}")
                print()
        
        # Priority fixes needed
        failed_functions = [name for name, result in self.results.items() 
                          if result['status'] == 'FAILED']
        
        if failed_functions:
            print(f"🚨 PRIORITY FIXES NEEDED ({len(failed_functions)} functions):")
            print("-" * 40)
            for func_name in failed_functions:
                result = self.results[func_name]
                print(f"• {func_name}")
                print(f"  Error: {result['error']}")
                if 'traceback' in result:
                    print(f"  Traceback available for debugging")
            print()
        
        # Recommendations
        print("💡 RECOMMENDATIONS:")
        print("-" * 30)
        
        if status_counts['FAILED'] > 0:
            print(f"1. Fix {status_counts['FAILED']} failed sources immediately")
        
        if status_counts['WARNING'] > 0:
            print(f"2. Investigate {status_counts['WARNING']} sources returning empty results")
        
        if total_jobs < 100:
            print("3. Add more job sources to reach 300+ daily jobs target")
        
        if total_time > 300:  # 5 minutes
            print("4. Optimize slow sources to meet 15-minute execution target")
        
        print()
        print("✅ Audit Complete! Check results above for next steps.")
        
        # Save detailed results to file
        self.save_audit_results()
    
    def save_audit_results(self):
        """Save detailed audit results to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"job_source_audit_{timestamp}.json"
        
        audit_data = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_sources': len(self.results),
                'successful': len([r for r in self.results.values() if r['status'] == 'SUCCESS']),
                'warnings': len([r for r in self.results.values() if r['status'] == 'WARNING']),
                'failed': len([r for r in self.results.values() if r['status'] == 'FAILED']),
                'total_jobs': sum(r['job_count'] for r in self.results.values()),
                'total_time': sum(r['execution_time'] for r in self.results.values())
            },
            'detailed_results': self.results
        }
        
        try:
            import json
            with open(filename, 'w') as f:
                json.dump(audit_data, f, indent=2)
            print(f"📄 Detailed results saved to: {filename}")
        except Exception as e:
            print(f"⚠️  Could not save results file: {e}")

def main():
    auditor = JobSourceAuditor()
    auditor.audit_all_sources()

if __name__ == "__main__":
    main()