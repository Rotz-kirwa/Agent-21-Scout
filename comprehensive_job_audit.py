#!/usr/bin/env python3
"""
Comprehensive Job Audit - Test all job categories and API connections
"""

import sys
import os
import json
from datetime import datetime
from collections import defaultdict

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

from telegram_jobs import JobScout, CATEGORIES

class JobCategoryAuditor:
    def __init__(self):
        self.scout = JobScout()
        self.results = {}
        self.api_status = {}
        self.category_performance = {}
        
    def test_individual_apis(self):
        """Test individual API endpoints"""
        print("🔍 Testing Individual API Endpoints")
        print("=" * 60)
        
        api_tests = [
            ("GitLab API", self.scout.fetch_gitlab_jobs, ["developer"]),
            ("Automattic API", self.scout.fetch_automattic_jobs, ["developer"]),
            ("Zapier API", self.scout.fetch_zapier_jobs, ["developer"]),
            ("Buffer API", self.scout.fetch_buffer_jobs, ["developer"]),
            ("Doist API", self.scout.fetch_doist_jobs, ["developer"]),
            ("Remote.com API", self.scout.fetch_remote_com_jobs, ["developer"]),
            ("Deel API", self.scout.fetch_deel_jobs, ["developer"]),
            ("FlexJobs API", self.scout.fetch_flexjobs_api, ["developer"]),
            ("Remotive API", self.scout.fetch_remotive_jobs, "developer"),
            ("Wellfound API", self.scout.fetch_wellfound_jobs, ["developer"]),
            ("NoWhiteboard API", self.scout.fetch_nowhiteboard_jobs, ["developer"]),
            ("WorkingNomads API", self.scout.fetch_workingnomads_jobs, ["developer"]),
        ]
        
        for api_name, api_function, test_keywords in api_tests:
            try:
                print(f"Testing {api_name}...")
                
                if api_name == "Remotive API":
                    # Remotive takes a single string, not a list
                    jobs = api_function(test_keywords)
                else:
                    jobs = api_function(test_keywords)
                
                job_count = len(jobs) if jobs else 0
                
                if job_count > 0:
                    print(f"  ✅ {api_name}: {job_count} jobs found")
                    self.api_status[api_name] = {"status": "working", "jobs": job_count}
                else:
                    print(f"  ⚠️ {api_name}: No jobs found (API may be working but no matches)")
                    self.api_status[api_name] = {"status": "no_results", "jobs": 0}
                    
            except Exception as e:
                print(f"  ❌ {api_name}: Failed - {str(e)[:100]}...")
                self.api_status[api_name] = {"status": "failed", "error": str(e)}
        
        print()
    
    def test_job_categories(self):
        """Test all job categories"""
        print("📊 Testing All Job Categories")
        print("=" * 60)
        
        for category, keywords in CATEGORIES.items():
            try:
                print(f"Testing category: {category}")
                
                # Test the category by running it through the main scouting process
                total_jobs = 0
                working_sources = 0
                failed_sources = 0
                
                # Test major company APIs
                company_apis = [
                    ("GitLab", self.scout.fetch_gitlab_jobs),
                    ("Automattic", self.scout.fetch_automattic_jobs),
                    ("Zapier", self.scout.fetch_zapier_jobs),
                    ("Buffer", self.scout.fetch_buffer_jobs),
                    ("Doist", self.scout.fetch_doist_jobs),
                    ("Remote.com", self.scout.fetch_remote_com_jobs),
                    ("Deel", self.scout.fetch_deel_jobs),
                ]
                
                for source_name, api_function in company_apis:
                    try:
                        jobs = api_function(keywords)
                        job_count = len(jobs) if jobs else 0
                        total_jobs += job_count
                        
                        if job_count > 0:
                            working_sources += 1
                        
                    except Exception as e:
                        failed_sources += 1
                
                # Test specialized job functions
                specialized_functions = [
                    ("Sales & BizDev", self.scout.fetch_sales_bizdev_jobs),
                    ("Product Management", self.scout.fetch_product_management_jobs),
                    ("Ecommerce", self.scout.fetch_ecommerce_jobs),
                    ("Healthcare Remote", self.scout.fetch_healthcare_remote_jobs),
                    ("Translation", self.scout.fetch_translation_jobs),
                    ("Research & Surveys", self.scout.fetch_research_survey_jobs),
                    ("Customer Support", self.scout.fetch_customer_support_jobs),
                    ("Operations HR", self.scout.fetch_operations_hr_jobs),
                    ("Finance", self.scout.fetch_finance_jobs),
                    ("Technical Writing", self.scout.fetch_technical_writing_jobs),
                    ("BPO Outsourcing", self.scout.fetch_bpo_outsourcing_jobs),
                    ("AI Training", self.scout.fetch_ai_training_jobs),
                    ("Freelance Gig", self.scout.fetch_freelance_gig_jobs),
                    ("VA Support", self.scout.fetch_va_support_jobs),
                    ("Creator Economy", self.scout.fetch_creator_economy_jobs),
                    ("Gaming Platforms", self.scout.fetch_gaming_platform_jobs),
                    ("Chat Moderation", self.scout.fetch_chat_moderation_jobs),
                    ("Social Media Tasks", self.scout.fetch_social_media_tasks_jobs),
                    ("Data Labeling", self.scout.fetch_data_labeling_specialist_jobs),
                    ("Course Creator", self.scout.fetch_course_creator_jobs),
                    ("Research Testing", self.scout.fetch_research_testing_jobs),
                ]
                
                for source_name, func in specialized_functions:
                    try:
                        jobs = func(keywords)
                        job_count = len(jobs) if jobs else 0
                        total_jobs += job_count
                        
                        if job_count > 0:
                            working_sources += 1
                            
                    except Exception as e:
                        failed_sources += 1
                
                # Store results
                self.category_performance[category] = {
                    "total_jobs": total_jobs,
                    "working_sources": working_sources,
                    "failed_sources": failed_sources,
                    "keywords": keywords
                }
                
                if total_jobs > 0:
                    print(f"  ✅ {category}: {total_jobs} jobs from {working_sources} sources")
                else:
                    print(f"  ⚠️ {category}: No jobs found ({failed_sources} sources failed)")
                    
            except Exception as e:
                print(f"  ❌ {category}: Category test failed - {str(e)[:100]}...")
                self.category_performance[category] = {
                    "total_jobs": 0,
                    "working_sources": 0,
                    "failed_sources": 1,
                    "error": str(e)
                }
        
        print()
    
    def test_specialized_functions(self):
        """Test specialized job functions that don't use keywords"""
        print("🎯 Testing Specialized Job Functions")
        print("=" * 60)
        
        specialized_tests = [
            ("Amazon AWS Jobs", lambda: self.scout.fetch_amazon_aws_jobs()),
            ("Major Remote Companies", lambda: self.scout.fetch_major_remote_companies()),
            ("Beginner Friendly Jobs", lambda: self.scout.fetch_beginner_friendly_jobs()),
            ("BPO Gig Opportunities", lambda: self.scout.fetch_bpo_gig_opportunities()),
            ("Platform Specific Jobs", lambda: self.scout.fetch_platform_specific_opportunities()),
        ]
        
        for test_name, test_function in specialized_tests:
            try:
                print(f"Testing {test_name}...")
                result = test_function()
                
                if result is None:
                    print(f"  ✅ {test_name}: Function executed (no return value)")
                    self.api_status[test_name] = {"status": "working", "jobs": "N/A"}
                else:
                    job_count = len(result) if isinstance(result, list) else 0
                    print(f"  ✅ {test_name}: {job_count} jobs")
                    self.api_status[test_name] = {"status": "working", "jobs": job_count}
                    
            except Exception as e:
                print(f"  ❌ {test_name}: Failed - {str(e)[:100]}...")
                self.api_status[test_name] = {"status": "failed", "error": str(e)}
        
        print()
    
    def generate_report(self):
        """Generate comprehensive audit report"""
        print("📋 COMPREHENSIVE AUDIT REPORT")
        print("=" * 60)
        
        # API Status Summary
        working_apis = sum(1 for api in self.api_status.values() if api["status"] == "working")
        failed_apis = sum(1 for api in self.api_status.values() if api["status"] == "failed")
        no_result_apis = sum(1 for api in self.api_status.values() if api["status"] == "no_results")
        
        print(f"🔌 API STATUS SUMMARY:")
        print(f"  ✅ Working APIs: {working_apis}")
        print(f"  ⚠️ APIs with no results: {no_result_apis}")
        print(f"  ❌ Failed APIs: {failed_apis}")
        print(f"  📊 Total APIs tested: {len(self.api_status)}")
        
        # Category Performance Summary
        working_categories = sum(1 for cat in self.category_performance.values() if cat["total_jobs"] > 0)
        empty_categories = sum(1 for cat in self.category_performance.values() if cat["total_jobs"] == 0)
        
        print(f"\n📂 CATEGORY STATUS SUMMARY:")
        print(f"  ✅ Categories with jobs: {working_categories}")
        print(f"  ⚠️ Categories with no jobs: {empty_categories}")
        print(f"  📊 Total categories: {len(self.category_performance)}")
        
        # Detailed API Status
        print(f"\n🔍 DETAILED API STATUS:")
        for api_name, status in self.api_status.items():
            if status["status"] == "working":
                jobs = status.get("jobs", "N/A")
                print(f"  ✅ {api_name}: Working ({jobs} jobs)")
            elif status["status"] == "no_results":
                print(f"  ⚠️ {api_name}: Working but no results")
            else:
                error = status.get("error", "Unknown error")[:50]
                print(f"  ❌ {api_name}: Failed - {error}...")
        
        # Categories needing attention
        print(f"\n⚠️ CATEGORIES NEEDING ATTENTION:")
        problem_categories = []
        for category, performance in self.category_performance.items():
            if performance["total_jobs"] == 0:
                problem_categories.append(category)
                print(f"  • {category}: No jobs found")
        
        if not problem_categories:
            print("  ✅ All categories are producing jobs!")
        
        # Recommendations
        print(f"\n💡 RECOMMENDATIONS:")
        
        if failed_apis > 0:
            print(f"  🔧 Fix {failed_apis} failed API connections")
        
        if empty_categories > 0:
            print(f"  📝 Review keywords for {empty_categories} empty categories")
        
        if no_result_apis > 0:
            print(f"  🔍 Investigate {no_result_apis} APIs with no results")
        
        # Success rate
        total_tests = len(self.api_status) + len(self.category_performance)
        successful_tests = working_apis + working_categories
        success_rate = (successful_tests / total_tests * 100) if total_tests > 0 else 0
        
        print(f"\n📈 OVERALL SUCCESS RATE: {success_rate:.1f}%")
        
        return {
            "api_status": self.api_status,
            "category_performance": self.category_performance,
            "summary": {
                "working_apis": working_apis,
                "failed_apis": failed_apis,
                "working_categories": working_categories,
                "empty_categories": empty_categories,
                "success_rate": success_rate
            }
        }
    
    def save_report(self, report):
        """Save audit report to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"job_audit_report_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"\n💾 Detailed report saved to: {filename}")

def main():
    """Main audit function"""
    print("🚀 Starting Comprehensive Job Category & API Audit")
    print("=" * 60)
    print(f"Audit started at: {datetime.now()}")
    print()
    
    auditor = JobCategoryAuditor()
    
    # Run all tests
    auditor.test_individual_apis()
    auditor.test_job_categories()
    auditor.test_specialized_functions()
    
    # Generate and save report
    report = auditor.generate_report()
    auditor.save_report(report)
    
    print(f"\n🎉 Audit completed at: {datetime.now()}")

if __name__ == "__main__":
    main()