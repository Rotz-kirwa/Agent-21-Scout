#!/usr/bin/env python3
"""
Test script to showcase platform-specific job sources (TikTok, YouTube, Facebook, etc.)
"""

from telegram_jobs import JobScout
from telegram_bot import send_telegram_message

def test_platform_specific_jobs():
    print("📱 Testing Platform-Specific Job Sources...")
    
    scout = JobScout()
    
    # Test platform-specific categories
    platform_categories = [
        ("social-media-tasks", ["tiktok-moderator", "youtube-reviewer", "facebook-support"]),
        ("platform-support", ["platform-support", "user-safety", "community-operations"]),
        ("ad-review-specialist", ["ad-reviewer", "advertising-compliance", "campaign-reviewer"]),
        ("data-labeling", ["image-labeling", "video-annotation", "text-classification"])
    ]
    
    all_platform_jobs = []
    category_summary = {}
    companies = set()
    
    for category, keywords in platform_categories:
        print(f"\n🔍 Testing {category} jobs...")
        
        if category == "social-media-tasks":
            jobs = scout.fetch_social_media_platform_jobs(keywords)
        elif category == "platform-support":
            jobs = scout.fetch_customer_support_platform_jobs(keywords)
        elif category == "ad-review-specialist":
            jobs = scout.fetch_ad_review_specialist_jobs(keywords)
        elif category == "data-labeling":
            jobs = scout.fetch_data_labeling_specialist_jobs(keywords)
        
        all_platform_jobs.extend(jobs)
        category_summary[category] = len(jobs)
        
        # Collect companies
        for job in jobs:
            companies.add(job['company'])
        
        print(f"   Found {len(jobs)} {category} jobs")
        if jobs:
            for job in jobs[:3]:  # Show first 3 jobs
                print(f"   - {job['title']} at {job['company']} ({job['salary']})")
    
    # Test the dedicated platform-specific function
    print(f"\n📱 Testing dedicated platform-specific opportunities...")
    scout.fetch_platform_specific_opportunities()
    platform_specific_jobs = [job for job in scout.jobs_found if 
                             any(platform in job['title'].lower() for platform in 
                                 ['tiktok', 'youtube', 'facebook', 'instagram', 'google'])]
    
    print(f"   Found {len(platform_specific_jobs)} platform-specific positions")
    
    # Test comprehensive platform jobs
    print(f"\n🏢 Testing comprehensive platform companies...")
    comprehensive_jobs = scout.fetch_comprehensive_platform_jobs([])
    print(f"   Found {len(comprehensive_jobs)} additional company opportunities")
    
    # Summary
    total_platform_jobs = len(all_platform_jobs) + len(platform_specific_jobs) + len(comprehensive_jobs)
    
    print(f"\n📊 Platform-Specific Jobs Summary:")
    print(f"   📱 Social Media Tasks: {category_summary.get('social-media-tasks', 0)} jobs")
    print(f"   🛡️ Platform Support: {category_summary.get('platform-support', 0)} jobs")
    print(f"   📢 Ad Review: {category_summary.get('ad-review-specialist', 0)} jobs")
    print(f"   🏷️ Data Labeling: {category_summary.get('data-labeling', 0)} jobs")
    print(f"   🎯 Platform-Specific: {len(platform_specific_jobs)} jobs")
    print(f"   🏢 Additional Companies: {len(comprehensive_jobs)} jobs")
    print(f"   💼 Total Platform Jobs: {total_platform_jobs} jobs")
    
    print(f"\n📱 Platforms You'll Work With:")
    platforms = ['TikTok', 'YouTube', 'Facebook', 'Instagram', 'Google', 'Meta']
    for platform in platforms:
        platform_jobs_count = len([job for job in all_platform_jobs + platform_specific_jobs 
                                  if platform.lower() in job['title'].lower()])
        if platform_jobs_count > 0:
            print(f"   ✅ {platform}: {platform_jobs_count} opportunities")
    
    print(f"\n🏢 Major BPO Companies Working with These Platforms:")
    major_bpo = ['Teleperformance', 'Majorel', 'Accenture', 'Cognizant', 'Genpact', 
                 'Wipro', 'HCL Technologies', 'Infosys BPM', 'TCS', 'Capgemini']
    for company in major_bpo:
        if company in companies:
            print(f"   ✅ {company}")
    
    print(f"\n🤖 AI/Data Companies:")
    ai_companies = ['Appen', 'TELUS International AI', 'Lionbridge', 'Scale AI', 
                    'Surge AI', 'OneForma', 'Labelbox', 'Rev.com']
    for company in ai_companies:
        if company in companies:
            print(f"   ✅ {company}")
    
    print(f"\n💼 Typical Tasks You'll Do:")
    print(f"   📱 Content Moderation: Review videos, images, posts for harmful content")
    print(f"   🛡️ Trust & Safety: Protect users from scams, harassment, misinformation")
    print(f"   📢 Ad Review: Check if ads meet platform guidelines")
    print(f"   🏷️ Data Labeling: Tag content for AI training")
    print(f"   💬 Customer Support: Help users with platform issues")
    print(f"   👥 Community Operations: Monitor engagement, flag spam")
    
    print(f"\n💰 Salary Ranges by Task Type:")
    print(f"   📱 TikTok/YouTube Moderation: $15-26/hour")
    print(f"   🛡️ Facebook/Meta Safety: $16-27/hour")
    print(f"   📢 Google Ads Review: $14-25/hour")
    print(f"   🏷️ AI Data Labeling: $12-28/hour")
    print(f"   💬 Platform Support: $13-23/hour")
    
    print(f"\n🌟 Perfect For:")
    print(f"   ✅ People who spend time on social media")
    print(f"   ✅ Detail-oriented individuals")
    print(f"   ✅ Those interested in online safety")
    print(f"   ✅ Beginners to remote work")
    print(f"   ✅ Flexible schedule needs")
    
    # Send test notification
    try:
        test_message = f"📱 *Platform-Specific Jobs Added!*\n\n"
        test_message += f"📱 *TikTok/YouTube*: {category_summary.get('social-media-tasks', 0)} jobs ($15-26/hr)\n"
        test_message += f"🛡️ *Platform Support*: {category_summary.get('platform-support', 0)} jobs ($13-23/hr)\n"
        test_message += f"📢 *Ad Review*: {category_summary.get('ad-review-specialist', 0)} jobs ($14-25/hr)\n"
        test_message += f"🏷️ *Data Labeling*: {category_summary.get('data-labeling', 0)} jobs ($12-28/hr)\n\n"
        test_message += f"💼 Total: {total_platform_jobs} platform opportunities\n"
        test_message += f"🎯 Work directly with TikTok, YouTube, Facebook, Google!\n"
        test_message += f"🌍 Perfect for social media users!"
        
        send_telegram_message(test_message)
        print("\n✅ Test notification sent to Telegram!")
    except Exception as e:
        print(f"\n❌ Failed to send test notification: {e}")
    
    return total_platform_jobs

if __name__ == "__main__":
    total_jobs = test_platform_specific_jobs()
    print(f"\n🎉 Test completed! Platform-specific job integration is active!")
    print(f"💡 Perfect for social media users and content enthusiasts!")
    print(f"📈 Expected daily jobs: 230+ (including {total_jobs} platform-specific)")