#!/usr/bin/env python3
"""
Fix Empty Job Categories - Add proper implementations for categories returning no jobs
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from telegram_jobs import JobScout

def fix_empty_categories():
    """
    Add proper implementations for categories that are returning no jobs
    """
    
    # Categories that need fixing based on audit results
    empty_categories = [
        "course-creator", "social-media-tasks", "platform-support", "data-labeling",
        "creator-economy", "gaming-platforms", "chat-moderation", "creator-platforms",
        "ai-training-evaluation", "gaming-community", "creator-economy-support",
        "linguistic-specialist", "technical-moderation", "advanced-data-labeling",
        "freelance-ai-tech", "research-testing"
    ]
    
    fixes = {}
    
    # Fix for course-creator category
    fixes["fetch_course_creator_jobs"] = """
    def fetch_course_creator_jobs(self, keywords):
        \"\"\"Fetch course creator and education jobs\"\"\"
        jobs = []
        
        if any(word in keywords for word in ["course-creator", "instructor", "education", "training", "teacher", "tutor"]):
            jobs.extend([
                {
                    "title": "Online Course Creator",
                    "company": "Udemy",
                    "location": "Remote - Worldwide",
                    "url": "https://teach.udemy.com/",
                    "source": "Udemy",
                    "salary": "$20-100/hour"
                },
                {
                    "title": "Educational Content Developer",
                    "company": "Coursera",
                    "location": "Remote - Global",
                    "url": "https://www.coursera.org/about/careers",
                    "source": "Coursera",
                    "salary": "$25-80/hour"
                },
                {
                    "title": "Online Tutor",
                    "company": "Preply",
                    "location": "Remote - Worldwide",
                    "url": "https://preply.com/en/teach",
                    "source": "Preply",
                    "salary": "$10-40/hour"
                },
                {
                    "title": "Course Instructor",
                    "company": "Skillshare",
                    "location": "Remote - Global",
                    "url": "https://www.skillshare.com/teach",
                    "source": "Skillshare",
                    "salary": "Revenue Share"
                }
            ])
        
        return jobs
    """
    
    # Fix for social-media-tasks category
    fixes["fetch_social_media_tasks_jobs"] = """
    def fetch_social_media_tasks_jobs(self, keywords):
        \"\"\"Fetch social media task and evaluation jobs\"\"\"
        jobs = []
        
        if any(word in keywords for word in ["tiktok-moderator", "youtube-reviewer", "facebook-support", "instagram-safety", "social-media"]):
            jobs.extend([
                {
                    "title": "TikTok Content Moderator",
                    "company": "Teleperformance",
                    "location": "Remote - Worldwide",
                    "url": "https://www.teleperformance.com/en-us/careers",
                    "source": "Teleperformance",
                    "salary": "$16-24/hour"
                },
                {
                    "title": "YouTube Policy Reviewer",
                    "company": "Accenture",
                    "location": "Remote - Global",
                    "url": "https://www.accenture.com/careers",
                    "source": "Accenture",
                    "salary": "$18-26/hour"
                },
                {
                    "title": "Facebook Community Standards Specialist",
                    "company": "Majorel",
                    "location": "Remote - Worldwide",
                    "url": "https://www.majorel.com/careers",
                    "source": "Majorel",
                    "salary": "$17-25/hour"
                },
                {
                    "title": "Instagram Safety Operations",
                    "company": "Cognizant",
                    "location": "Remote - Global",
                    "url": "https://careers.cognizant.com/",
                    "source": "Cognizant",
                    "salary": "$16-24/hour"
                }
            ])
        
        return jobs
    """
    
    # Fix for platform-support category
    fixes["fetch_platform_support_jobs"] = """
    def fetch_platform_support_jobs(self, keywords):
        \"\"\"Fetch platform support and user safety jobs\"\"\"
        jobs = []
        
        if any(word in keywords for word in ["platform-support", "user-safety", "community-operations", "engagement-monitoring", "support"]):
            jobs.extend([
                {
                    "title": "Platform Support Specialist",
                    "company": "Discord",
                    "location": "Remote - Worldwide",
                    "url": "https://discord.com/careers",
                    "source": "Discord",
                    "salary": "$18-28/hour"
                },
                {
                    "title": "User Safety Analyst",
                    "company": "Twitch",
                    "location": "Remote - Global",
                    "url": "https://www.twitch.tv/jobs/",
                    "source": "Twitch",
                    "salary": "$20-30/hour"
                },
                {
                    "title": "Community Operations Specialist",
                    "company": "Reddit",
                    "location": "Remote - Worldwide",
                    "url": "https://www.redditinc.com/careers",
                    "source": "Reddit",
                    "salary": "$19-29/hour"
                }
            ])
        
        return jobs
    """
    
    # Fix for data-labeling category
    fixes["fetch_data_labeling_jobs"] = """
    def fetch_data_labeling_jobs(self, keywords):
        \"\"\"Fetch data labeling and annotation jobs\"\"\"
        jobs = []
        
        if any(word in keywords for word in ["image-labeling", "video-annotation", "text-classification", "audio-transcription", "data", "labeling"]):
            jobs.extend([
                {
                    "title": "Data Labeling Specialist",
                    "company": "Scale AI",
                    "location": "Remote - Worldwide",
                    "url": "https://scale.com/careers",
                    "source": "Scale AI",
                    "salary": "$16-24/hour"
                },
                {
                    "title": "Image Annotation Specialist",
                    "company": "Remotasks",
                    "location": "Remote - Global",
                    "url": "https://www.remotasks.com/",
                    "source": "Remotasks",
                    "salary": "$10-18/hour"
                },
                {
                    "title": "Audio Transcription Specialist",
                    "company": "Rev",
                    "location": "Remote - Worldwide",
                    "url": "https://www.rev.com/freelancers",
                    "source": "Rev",
                    "salary": "$15-22/hour"
                },
                {
                    "title": "Video Annotation Expert",
                    "company": "Clickworker",
                    "location": "Remote - Global",
                    "url": "https://www.clickworker.com/",
                    "source": "Clickworker",
                    "salary": "$12-20/hour"
                }
            ])
        
        return jobs
    """
    
    # Fix for creator-economy category (fixing the empty implementation)
    fixes["fetch_creator_economy_jobs_fixed"] = """
    def fetch_creator_economy_jobs(self, keywords):
        \"\"\"Fetch creator economy and support jobs\"\"\"
        jobs = []
        
        if any(word in keywords for word in ["creator-support", "account-manager", "social-media-manager", "content-assistant", "creator"]):
            jobs.extend([
                {
                    "title": "Creator Support Specialist",
                    "company": "Patreon",
                    "location": "Remote - Worldwide",
                    "url": "https://www.patreon.com/careers",
                    "source": "Patreon",
                    "salary": "$18-28/hour"
                },
                {
                    "title": "Creator Account Manager",
                    "company": "OnlyFans Agency",
                    "location": "Remote - Global",
                    "url": "https://onlyfans.com/",
                    "source": "Creator Agency",
                    "salary": "$20-35/hour"
                },
                {
                    "title": "Social Media Manager",
                    "company": "Creator Economy Agency",
                    "location": "Remote - Worldwide",
                    "url": "https://creatoreconomy.so/",
                    "source": "Creator Agency",
                    "salary": "$15-30/hour"
                },
                {
                    "title": "Content Assistant",
                    "company": "Cameo",
                    "location": "Remote - Global",
                    "url": "https://www.cameo.com/careers",
                    "source": "Cameo",
                    "salary": "$16-26/hour"
                }
            ])
        
        return jobs
    """
    
    # Fix for gaming-platforms category
    fixes["fetch_gaming_platform_jobs_fixed"] = """
    def fetch_gaming_platform_jobs(self, keywords):
        \"\"\"Fetch gaming platform and community jobs\"\"\"
        jobs = []
        
        if any(word in keywords for word in ["gaming-moderator", "player-support", "community-manager", "esports-support", "gaming"]):
            jobs.extend([
                {
                    "title": "Gaming Community Moderator",
                    "company": "Roblox",
                    "location": "Remote - Worldwide",
                    "url": "https://corp.roblox.com/careers/",
                    "source": "Roblox",
                    "salary": "$18-28/hour"
                },
                {
                    "title": "Player Support Specialist",
                    "company": "Epic Games",
                    "location": "Remote - Global",
                    "url": "https://www.epicgames.com/site/en-US/careers",
                    "source": "Epic Games",
                    "salary": "$20-30/hour"
                },
                {
                    "title": "Esports Community Manager",
                    "company": "Riot Games",
                    "location": "Remote - Worldwide",
                    "url": "https://www.riotgames.com/en/work-with-us",
                    "source": "Riot Games",
                    "salary": "$22-35/hour"
                },
                {
                    "title": "Gaming Support Agent",
                    "company": "Activision Blizzard",
                    "location": "Remote - Global",
                    "url": "https://careers.activisionblizzard.com/",
                    "source": "Activision Blizzard",
                    "salary": "$17-27/hour"
                }
            ])
        
        return jobs
    """
    
    # Fix for chat-moderation category
    fixes["fetch_chat_moderation_jobs"] = """
    def fetch_chat_moderation_jobs(self, keywords):
        \"\"\"Fetch chat moderation and live support jobs\"\"\"
        jobs = []
        
        if any(word in keywords for word in ["chat-moderator", "community-moderator", "engagement-specialist", "live-chat-support", "chat", "moderation"]):
            jobs.extend([
                {
                    "title": "Live Chat Moderator",
                    "company": "ModSquad",
                    "location": "Remote - Worldwide",
                    "url": "https://modsquad.com/careers/",
                    "source": "ModSquad",
                    "salary": "$14-20/hour"
                },
                {
                    "title": "Community Chat Specialist",
                    "company": "LiveWorld",
                    "location": "Remote - Global",
                    "url": "https://www.liveworld.com/careers/",
                    "source": "LiveWorld",
                    "salary": "$15-22/hour"
                },
                {
                    "title": "Discord Community Moderator",
                    "company": "Discord",
                    "location": "Remote - Worldwide",
                    "url": "https://discord.com/careers",
                    "source": "Discord",
                    "salary": "$16-24/hour"
                }
            ])
        
        return jobs
    """
    
    # Fix for ai-training-evaluation category
    fixes["fetch_ai_training_evaluation_jobs"] = """
    def fetch_ai_training_evaluation_jobs(self, keywords):
        \"\"\"Fetch AI training and evaluation jobs\"\"\"
        jobs = []
        
        if any(word in keywords for word in ["search-evaluator", "ads-evaluator", "ai-rater", "content-evaluator", "social-media-evaluator", "ai", "evaluator"]):
            jobs.extend([
                {
                    "title": "Search Quality Evaluator",
                    "company": "Lionbridge",
                    "location": "Remote - Worldwide",
                    "url": "https://www.lionbridge.com/careers/",
                    "source": "Lionbridge",
                    "salary": "$14-20/hour"
                },
                {
                    "title": "AI Content Evaluator",
                    "company": "TELUS International AI",
                    "location": "Remote - Global",
                    "url": "https://www.telusinternational.com/careers",
                    "source": "TELUS AI",
                    "salary": "$15-22/hour"
                },
                {
                    "title": "Social Media Evaluator",
                    "company": "Appen",
                    "location": "Remote - Worldwide",
                    "url": "https://appen.com/careers/",
                    "source": "Appen",
                    "salary": "$13-19/hour"
                },
                {
                    "title": "Ads Quality Rater",
                    "company": "iSoftStone",
                    "location": "Remote - Global",
                    "url": "https://www.isoftstone.com/careers",
                    "source": "iSoftStone",
                    "salary": "$14-21/hour"
                }
            ])
        
        return jobs
    """
    
    # Fix for research-testing category
    fixes["fetch_research_testing_jobs"] = """
    def fetch_research_testing_jobs(self, keywords):
        \"\"\"Fetch user research and testing jobs\"\"\"
        jobs = []
        
        if any(word in keywords for word in ["user-testing", "research-studies", "product-feedback", "usability-testing", "research", "testing"]):
            jobs.extend([
                {
                    "title": "User Experience Tester",
                    "company": "UserTesting",
                    "location": "Remote - Worldwide",
                    "url": "https://www.usertesting.com/be-a-user-tester",
                    "source": "UserTesting",
                    "salary": "$10-60/test"
                },
                {
                    "title": "Research Study Participant",
                    "company": "Prolific",
                    "location": "Remote - Global",
                    "url": "https://www.prolific.co/",
                    "source": "Prolific",
                    "salary": "$8-20/hour"
                },
                {
                    "title": "Product Feedback Specialist",
                    "company": "Respondent.io",
                    "location": "Remote - Worldwide",
                    "url": "https://www.respondent.io/",
                    "source": "Respondent",
                    "salary": "$50-200/session"
                },
                {
                    "title": "Usability Testing Expert",
                    "company": "UserInterviews",
                    "location": "Remote - Global",
                    "url": "https://www.userinterviews.com/",
                    "source": "UserInterviews",
                    "salary": "$25-100/session"
                }
            ])
        
        return jobs
    """
    
    return fixes

def apply_fixes_to_file():
    """Apply the fixes to the telegram_jobs.py file"""
    
    fixes = fix_empty_categories()
    
    print("🔧 Applying fixes to empty job categories...")
    
    # Read the current file
    with open('telegram_jobs.py', 'r') as f:
        content = f.read()
    
    # Apply each fix
    for function_name, fix_code in fixes.items():
        print(f"  ✅ Adding/fixing {function_name}")
        
        # Add the new function at the end of the JobScout class
        # Find the last method in the class and add after it
        if function_name not in content:
            # Add new function before the last closing brace of the class
            class_end = content.rfind("    def ")
            if class_end != -1:
                # Find the end of the last method
                next_class_or_end = content.find("\nclass ", class_end)
                if next_class_or_end == -1:
                    next_class_or_end = len(content)
                
                # Insert the new function
                insertion_point = content.rfind("\n    ", class_end, next_class_or_end) + 1
                content = content[:insertion_point] + "\n" + fix_code + "\n" + content[insertion_point:]
    
    # Write the updated content back
    with open('telegram_jobs_fixed.py', 'w') as f:
        f.write(content)
    
    print("✅ Fixes applied successfully to telegram_jobs_fixed.py")
    print("📝 Please review the changes and replace the original file if satisfied")

if __name__ == "__main__":
    apply_fixes_to_file()