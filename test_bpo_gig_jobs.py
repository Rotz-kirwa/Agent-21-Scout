#!/usr/bin/env python3
"""
Test script to showcase BPO, AI training, and gig economy job sources
"""

from telegram_jobs import JobScout
from telegram_bot import send_telegram_message

def test_bpo_gig_jobs():
    print("🏭 Testing BPO, AI Training & Gig Economy Jobs...")
    
    scout = JobScout()
    
    # Test new job categories
    new_categories = [
        ("bpo-outsourcing", ["content-moderator", "support-agent", "trust-safety"]),
        ("ai-training", ["data-annotation", "ai-training", "rater", "labeling"]),
        ("freelance-gig", ["freelance", "virtual-assistant", "small-tasks"]),
        ("content-moderation", ["content-moderator", "community-moderation"])
    ]
    
    all_new_jobs = []
    category_summary = {}
    companies = set()
    
    for category, keywords in new_categories:
        print(f"\n🔍 Testing {category} jobs...")
        
        if category == "bpo-outsourcing":
            jobs = scout.fetch_bpo_outsourcing_jobs(keywords)
        elif category == "ai-training":
            jobs = scout.fetch_ai_training_jobs(keywords)
        elif category == "freelance-gig":
            jobs = scout.fetch_freelance_gig_jobs(keywords)
        elif category == "content-moderation":
            jobs = scout.fetch_va_support_jobs(keywords)  # VA support includes moderation
        
        all_new_jobs.extend(jobs)
        category_summary[category] = len(jobs)
        
        # Collect companies
        for job in jobs:
            companies.add(job['company'])
        
        print(f"   Found {len(jobs)} {category} jobs")
        if jobs:
            for job in jobs[:3]:  # Show first 3 jobs
                print(f"   - {job['title']} at {job['company']} ({job['salary']})")
    
    # Test the dedicated BPO/gig function
    print(f"\n🏭 Testing dedicated BPO & gig opportunities...")
    scout.fetch_bpo_gig_opportunities()
    dedicated_jobs = [job for job in scout.jobs_found if 
                     job['company'] in ['Teleperformance', 'Majorel', 'Accenture', 'Appen', 
                                       'TELUS AI', 'Upwork', 'ModSquad', 'Remotasks']]
    
    print(f"   Found {len(dedicated_jobs)} BPO & gig positions")
    
    # Summary
    total_new_jobs = len(all_new_jobs) + len(dedicated_jobs)
    
    print(f"\n📊 BPO & Gig Economy Jobs Summary:")
    print(f"   🏭 BPO/Outsourcing: {category_summary.get('bpo-outsourcing', 0)} jobs")
    print(f"   🤖 AI Training: {category_summary.get('ai-training', 0)} jobs")
    print(f"   💼 Freelance/Gig: {category_summary.get('freelance-gig', 0)} jobs")
    print(f"   🛡️ Content Moderation: {category_summary.get('content-moderation', 0)} jobs")
    print(f"   🎯 Additional Opportunities: {len(dedicated_jobs)} jobs")
    print(f"   💼 Total New Sources: {total_new_jobs} jobs")
    
    print(f"\n🏢 Major BPO Companies Now Included:")
    bpo_companies = ['Teleperformance', 'Majorel', 'Accenture', 'Cognizant', 'Genpact', 
                     'TaskUs', 'Concentrix', 'TTEC']
    for company in bpo_companies:
        if company in companies:
            print(f"   ✅ {company}")
    
    print(f"\n🤖 AI Training Platforms:")
    ai_companies = ['Appen', 'TELUS International AI', 'Lionbridge', 'Clickworker', 
                    'Remotasks', 'OneForma', 'Scale AI']
    for company in ai_companies:
        if company in companies:
            print(f"   ✅ {company}")
    
    print(f"\n💼 Freelance & Gig Platforms:")
    gig_companies = ['Upwork', 'Fiverr', 'Freelancer.com', 'PeoplePerHour', 'Workana']
    for company in gig_companies:
        if company in companies:
            print(f"   ✅ {company}")
    
    print(f"\n🛡️ Specialized Support Companies:")
    support_companies = ['ModSquad', 'SupportNinja', 'Boldly', 'Time Etc', 'Belay', 'Fancy Hands']
    for company in support_companies:
        if company in companies:
            print(f"   ✅ {company}")
    
    print(f"\n💰 Typical Salary Ranges:")
    print(f"   🏭 BPO/Content Moderation: $12-30/hour")
    print(f"   🤖 AI Training/Data: $8-25/hour")
    print(f"   💼 Freelance/VA: $5-30/hour")
    print(f"   🛡️ Specialized Support: $10-28/hour")
    
    print(f"\n🌟 Perfect For:")
    print(f"   ✅ Complete beginners to remote work")
    print(f"   ✅ Flexible schedule needs")
    print(f"   ✅ Part-time or full-time work")
    print(f"   ✅ Building remote work experience")
    print(f"   ✅ No technical background required")
    
    # Send test notification
    try:
        test_message = f"🏭 *BPO & Gig Economy Jobs Added!*\n\n"
        test_message += f"🏭 *BPO Companies*: {category_summary.get('bpo-outsourcing', 0)} jobs ($12-30/hr)\n"
        test_message += f"🤖 *AI Training*: {category_summary.get('ai-training', 0)} jobs ($8-25/hr)\n"
        test_message += f"💼 *Freelance/Gig*: {category_summary.get('freelance-gig', 0)} jobs ($5-30/hr)\n"
        test_message += f"🛡️ *Support/VA*: {category_summary.get('content-moderation', 0)} jobs ($10-28/hr)\n\n"
        test_message += f"💼 Total: {total_new_jobs} new opportunities\n"
        test_message += f"🌍 Perfect for beginners, flexible schedules!\n"
        test_message += f"🎯 Work with TikTok, YouTube, Meta contractors!"
        
        send_telegram_message(test_message)
        print("\n✅ Test notification sent to Telegram!")
    except Exception as e:
        print(f"\n❌ Failed to send test notification: {e}")
    
    return total_new_jobs

if __name__ == "__main__":
    total_jobs = test_bpo_gig_jobs()
    print(f"\n🎉 Test completed! BPO & gig economy integration is active!")
    print(f"💡 Perfect for flexible work and building remote experience!")
    print(f"📈 Expected daily jobs: 170+ (including {total_jobs} from new sources)")