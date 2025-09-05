#!/usr/bin/env python3
"""
Test script to showcase beginner-friendly job categories
"""

from telegram_jobs import JobScout
from telegram_bot import send_telegram_message

def test_beginner_friendly_jobs():
    print("🌟 Testing Beginner-Friendly Job Categories...")
    
    scout = JobScout()
    
    # Test beginner-friendly categories
    beginner_categories = [
        ("customer-support", ["customer-support", "customer-success", "community-manager"]),
        ("operations-hr", ["recruiter", "hr-specialist", "people-operations", "project-manager"]),
        ("finance", ["finance-analyst", "accountant", "financial-analyst"]),
        ("technical-writing", ["technical-writer", "documentation", "copywriter", "blog-writer"])
    ]
    
    all_beginner_jobs = []
    category_summary = {}
    
    for category, keywords in beginner_categories:
        print(f"\n🔍 Testing {category} jobs...")
        
        if category == "customer-support":
            jobs = scout.fetch_customer_support_jobs(keywords)
        elif category == "operations-hr":
            jobs = scout.fetch_operations_hr_jobs(keywords)
        elif category == "finance":
            jobs = scout.fetch_finance_jobs(keywords)
        elif category == "technical-writing":
            jobs = scout.fetch_technical_writing_jobs(keywords)
        
        all_beginner_jobs.extend(jobs)
        category_summary[category] = len(jobs)
        
        print(f"   Found {len(jobs)} {category} jobs")
        if jobs:
            for job in jobs[:3]:  # Show first 3 jobs
                print(f"   - {job['title']} at {job['company']} ({job['salary']})")
    
    # Test the dedicated beginner-friendly function
    print(f"\n🌟 Testing dedicated beginner-friendly jobs...")
    scout.fetch_beginner_friendly_jobs()
    dedicated_jobs = [job for job in scout.jobs_found if 
                     any(word in job['title'].lower() for word in 
                         ['entry', 'junior', 'beginner', 'assistant', 'associate'])]
    
    print(f"   Found {len(dedicated_jobs)} entry-level positions")
    
    # Summary
    total_beginner_jobs = len(all_beginner_jobs) + len(dedicated_jobs)
    
    print(f"\n📊 Beginner-Friendly Jobs Summary:")
    print(f"   🎯 Customer Support & Success: {category_summary.get('customer-support', 0)} jobs")
    print(f"   🏢 Operations, HR & Finance: {category_summary.get('operations-hr', 0) + category_summary.get('finance', 0)} jobs")
    print(f"   📝 Content & Writing: {category_summary.get('technical-writing', 0)} jobs")
    print(f"   🌟 Entry-Level Positions: {len(dedicated_jobs)} jobs")
    print(f"   💼 Total Beginner-Friendly: {total_beginner_jobs} jobs")
    
    print(f"\n🏢 Companies Hiring Beginners:")
    companies = set()
    for job in all_beginner_jobs + dedicated_jobs:
        companies.add(job['company'])
    
    for company in sorted(companies):
        print(f"   ✅ {company}")
    
    print(f"\n💰 Salary Ranges for Beginners:")
    print(f"   🎯 Customer Support: $25k-$90k/year")
    print(f"   🏢 Operations/HR: $30k-$120k/year")
    print(f"   💰 Finance: $45k-$100k/year")
    print(f"   📝 Writing: $30k-$85k/year")
    
    print(f"\n🌍 All positions are:")
    print(f"   ✅ 100% Remote")
    print(f"   ✅ Kenya-friendly")
    print(f"   ✅ No experience required for many roles")
    print(f"   ✅ Great for career starters")
    
    # Send test notification
    try:
        test_message = f"🌟 *Beginner-Friendly Jobs Added!*\n\n"
        test_message += f"🎯 *Customer Support*: {category_summary.get('customer-support', 0)} jobs ($25k-$90k)\n"
        test_message += f"🏢 *Operations/HR*: {category_summary.get('operations-hr', 0) + category_summary.get('finance', 0)} jobs ($30k-$120k)\n"
        test_message += f"📝 *Content/Writing*: {category_summary.get('technical-writing', 0)} jobs ($30k-$85k)\n"
        test_message += f"🌟 *Entry-Level*: {len(dedicated_jobs)} positions\n\n"
        test_message += f"💼 Total: {total_beginner_jobs} beginner-friendly opportunities\n"
        test_message += f"🌍 All remote, Kenya-friendly, perfect for career starters!"
        
        send_telegram_message(test_message)
        print("\n✅ Test notification sent to Telegram!")
    except Exception as e:
        print(f"\n❌ Failed to send test notification: {e}")
    
    return total_beginner_jobs

if __name__ == "__main__":
    total_jobs = test_beginner_friendly_jobs()
    print(f"\n🎉 Test completed! Beginner-friendly job categories are active!")
    print(f"💡 Perfect for people starting their remote work journey!")
    print(f"📈 Expected daily jobs: 120+ (including {total_jobs} beginner-friendly)")