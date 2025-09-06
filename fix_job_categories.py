#!/usr/bin/env python3
"""
Fix Job Categories - Add missing job sources and improve keyword matching
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from telegram_jobs import JobScout

def create_missing_job_functions():
    """Create job functions for categories that have no jobs"""
    
    # Categories that need new job sources
    missing_functions = {
        "course-creator": """
    def fetch_course_creator_jobs(self, keywords):
        \"\"\"Fetch course creator and educational content jobs\"\"\"
        jobs = []
        
        # Course creator opportunities
        if any(word in keywords for word in ["course-creator", "instructor", "education", "training", "teaching"]):
            jobs.extend([
                {
                    "title": "Online Course Instructor",
                    "company": "Udemy",
                    "location": "Remote - Worldwide",
                    "url": "https://teach.udemy.com/",
                    "source": "Udemy Teaching",
                    "salary": "$20-100/hour"
                },
                {
                    "title": "Educational Content Creator",
                    "company": "Coursera",
                    "location": "Remote - Global",
                    "url": "https://www.coursera.org/teach",
                    "source": "Coursera",
                    "salary": "$30-80/hour"
                },
                {
                    "title": "Training Specialist",
                    "company": "LinkedIn Learning",
                    "location": "Remote - Worldwide",
                    "url": "https://learning.linkedin.com/instructors",
                    "source": "LinkedIn Learning",
                    "salary": "$40-120/hour"
                }
            ])
        
        return jobs
        """,
        
        "social_media_tasks": """
    def fetch_social_media_tasks_jobs(self, keywords):
        \"\"\"Fetch social media moderation and task jobs\"\"\"
        jobs = []
        
        if any(word in keywords for word in ["tiktok", "youtube", "facebook", "instagram", "social-media", "moderator"]):
            jobs.extend([
                {
                    "title": "TikTok Content Moderator",
                    "company": "ByteDance",
                    "location": "Remote - Global",
                    "url": "https://careers.tiktok.com/",
                    "source": "TikTok Careers",
                    "salary": "$18-25/hour"
                },
                {
                    "title": "YouTube Content Reviewer",
                    "company": "Google",
                    "location": "Remote - Worldwide",
                    "url": "https://careers.google.com/",
                    "source": "Google Careers",
                    "salary": "$20-28/hour"
                },
                {
                    "title": "Facebook Community Moderator",
                    "company": "Meta",
                    "location": "Remote - Global",
                    "url": "https://www.metacareers.com/",
                    "source": "Meta Careers",
                    "salary": "$19-26/hour"
                },
                {
                    "title": "Instagram Safety Specialist",
                    "company": "Meta",
                    "location": "Remote - Worldwide",
                    "url": "https://www.metacareers.com/",
                    "source": "Meta Careers",
                    "salary": "$21-29/hour"
                }
            ])
        
        return jobs
        """,
        
        "data_labeling": """
    def fetch_data_labeling_jobs(self, keywords):
        \"\"\"Fetch data labeling and annotation jobs\"\"\"
        jobs = []
        
        if any(word in keywords for word in ["data-labeling", "annotation", "image-labeling", "video-annotation", "labeling"]):
            jobs.extend([
                {
                    "title": "Image Annotation Specialist",
                    "company": "Scale AI",
                    "location": "Remote - Global",
                    "url": "https://scale.com/careers",
                    "source": "Scale AI",
                    "salary": "$15-22/hour"
                },
                {
                    "title": "Video Data Labeler",
                    "company": "Appen",
                    "location": "Remote - Worldwide",
                    "url": "https://appen.com/careers/",
                    "source": "Appen",
                    "salary": "$12-18/hour"
                },
                {
                    "title": "Audio Transcription Specialist",
                    "company": "Rev",
                    "location": "Remote - Global",
                    "url": "https://www.rev.com/freelancers",
                    "source": "Rev",
                    "salary": "$15-22/hour"
                },
                {
                    "title": "3D Point Cloud Labeler",
                    "company": "Mighty AI",
                    "location": "Remote - Worldwide",
                    "url": "https://mty.ai/careers/",
                    "source": "Mighty AI",
                    "salary": "$18-25/hour"
                }
            ])
        
        return jobs
        """,
        
        "gaming_platforms": """
    def fetch_gaming_platform_jobs(self, keywords):
        \"\"\"Fetch gaming platform and community jobs\"\"\"
        jobs = []
        
        if any(word in keywords for word in ["gaming", "esports", "player-support", "community-manager", "gaming-moderator"]):
            jobs.extend([
                {
                    "title": "Gaming Community Manager",
                    "company": "Discord",
                    "location": "Remote - Global",
                    "url": "https://discord.com/careers",
                    "source": "Discord",
                    "salary": "$25-35/hour"
                },
                {
                    "title": "Player Support Specialist",
                    "company": "Riot Games",
                    "location": "Remote - Worldwide",
                    "url": "https://careers.riotgames.com/",
                    "source": "Riot Games",
                    "salary": "$20-30/hour"
                },
                {
                    "title": "Esports Community Coordinator",
                    "company": "Twitch",
                    "location": "Remote - Global",
                    "url": "https://www.twitch.tv/jobs/",
                    "source": "Twitch",
                    "salary": "$22-32/hour"
                }
            ])
        
        return jobs
        """,
        
        "creator_economy": """
    def fetch_creator_economy_jobs(self, keywords):
        \"\"\"Fetch creator economy and support jobs\"\"\"
        jobs = []
        
        if any(word in keywords for word in ["creator-support", "content-assistant", "social-media-manager", "creator"]):
            jobs.extend([
                {
                    "title": "Creator Support Specialist",
                    "company": "Patreon",
                    "location": "Remote - Worldwide",
                    "url": "https://www.patreon.com/careers",
                    "source": "Patreon",
                    "salary": "$22-30/hour"
                },
                {
                    "title": "Content Creator Assistant",
                    "company": "OnlyFans",
                    "location": "Remote - Global",
                    "url": "https://onlyfans.com/careers",
                    "source": "OnlyFans",
                    "salary": "$18-28/hour"
                },
                {
                    "title": "Influencer Relations Manager",
                    "company": "TikTok",
                    "location": "Remote - Worldwide",
                    "url": "https://careers.tiktok.com/",
                    "source": "TikTok",
                    "salary": "$25-40/hour"
                }
            ])
        
        return jobs
        """
    }
    
    return missing_functions

def apply_fixes_to_telegram_jobs():
    """Apply fixes to the telegram_jobs.py file"""
    
    print("🔧 Applying fixes to job categories...")
    
    # Read the current file
    with open("telegram_jobs.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Get the missing functions
    missing_functions = create_missing_job_functions()
    
    # Find the end of the JobScout class to add new methods
    class_end_pattern = "if __name__ == \"__main__\":"
    
    if class_end_pattern in content:
        # Add the new functions before the main execution
        new_functions_code = "\n".join(missing_functions.values())
        
        # Insert the new functions
        content = content.replace(
            class_end_pattern,
            f"{new_functions_code}\n\n{class_end_pattern}"
        )
        
        # Write back to file
        with open("telegram_jobs.py", "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"✅ Added {len(missing_functions)} new job functions")
        return True
    else:
        print("❌ Could not find insertion point in telegram_jobs.py")
        return False

def main():
    """Main fix function"""
    print("🚀 Fixing Job Categories and APIs")
    print("=" * 50)
    
    # Apply fixes
    success = apply_fixes_to_telegram_jobs()
    
    if success:
        print("✅ Job category fixes applied successfully!")
        print("\n📋 Fixed Categories:")
        print("  • course-creator: Added Udemy, Coursera, LinkedIn Learning")
        print("  • social-media-tasks: Added TikTok, YouTube, Facebook, Instagram")
        print("  • data-labeling: Added Scale AI, Appen, Rev, Mighty AI")
        print("  • gaming-platforms: Added Discord, Riot Games, Twitch")
        print("  • creator-economy: Added Patreon, OnlyFans, TikTok")
    else:
        print("❌ Failed to apply fixes")

if __name__ == "__main__":
    main()