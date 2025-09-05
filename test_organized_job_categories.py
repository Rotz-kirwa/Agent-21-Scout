#!/usr/bin/env python3
"""
Test Script for Organized Job Categorization System
Demonstrates how jobs will be grouped by skill level and requirements
"""

import json
from datetime import datetime

# Organized Job Categories by Skill Level and Requirements
ORGANIZED_JOB_CATEGORIES = {
    
    # ===== ENTRY LEVEL JOBS (No Experience Required) =====
    "entry_level": {
        "description": "Jobs requiring no prior experience - perfect for beginners",
        "skill_requirements": "Basic computer skills, reliable internet",
        "categories": {
            
            # Basic Customer Support & Chat (Entry Level)
            "basic_customer_support": {
                "keywords": ["customer-support", "chat-support", "email-support", "helpdesk", "live-chat"],
                "salary_range": "$12-20/hour",
                "companies": ["LiveWorld", "ModSquad", "SupportNinja", "Teleperformance", "TTEC"],
                "requirements": "Good communication, basic computer skills"
            },
            
            # Basic Content Moderation (Entry Level)
            "basic_content_moderation": {
                "keywords": ["content-moderator", "community-moderator", "social-media-moderator", "chat-moderator"],
                "salary_range": "$13-18/hour", 
                "companies": ["Majorel", "TaskUs", "Concentrix", "Alorica", "ModSquad"],
                "requirements": "Attention to detail, cultural awareness"
            },
            
            # Basic Data Entry & Microtasks (Entry Level)
            "basic_data_entry": {
                "keywords": ["data-entry", "microtasks", "surveys", "basic-annotation", "clickworker"],
                "salary_range": "$8-15/hour",
                "companies": ["Clickworker", "Microworkers", "Amazon MTurk", "OneForma"],
                "requirements": "Basic computer skills, attention to detail"
            },
            
            # Basic Virtual Assistant (Entry Level)
            "basic_virtual_assistant": {
                "keywords": ["virtual-assistant", "admin-assistant", "scheduling", "email-management"],
                "salary_range": "$10-18/hour",
                "companies": ["Fancy Hands", "Time Etc", "Belay Solutions", "CloudTask"],
                "requirements": "Organization skills, basic office software"
            }
        }
    },
    
    # ===== INTERMEDIATE LEVEL JOBS (Some Experience/Skills Required) =====
    "intermediate_level": {
        "description": "Jobs requiring some experience or specific skills",
        "skill_requirements": "1-2 years experience or specific technical skills",
        "categories": {
            
            # Advanced Customer Support (Intermediate)
            "advanced_customer_support": {
                "keywords": ["technical-support", "customer-success", "account-manager", "support-specialist"],
                "salary_range": "$18-30/hour",
                "companies": ["SupportNinja", "Automattic", "GitLab", "Buffer", "Remote.com"],
                "requirements": "Technical knowledge, problem-solving skills"
            },
            
            # Platform-Specific Moderation (Intermediate)
            "platform_moderation": {
                "keywords": ["tiktok-moderator", "facebook-moderator", "youtube-reviewer", "instagram-safety", "trust-safety"],
                "salary_range": "$16-25/hour",
                "companies": ["ByteDance", "Meta", "Google", "Twitter", "Reddit", "Discord"],
                "requirements": "Platform knowledge, policy understanding"
            },
            
            # AI Training & Evaluation (Intermediate)
            "ai_training_evaluation": {
                "keywords": ["search-evaluator", "ads-evaluator", "ai-rater", "content-evaluator", "social-media-evaluator"],
                "salary_range": "$14-22/hour",
                "companies": ["TELUS International", "Appen", "Lionbridge", "OneForma", "iSoftStone"],
                "requirements": "Analytical skills, cultural knowledge, attention to detail"
            },
            
            # Gaming Community Management (Intermediate)
            "gaming_community": {
                "keywords": ["gaming-moderator", "player-support", "community-manager", "esports-support"],
                "salary_range": "$15-25/hour",
                "companies": ["Roblox", "Epic Games", "Riot Games", "Activision Blizzard", "Twitch"],
                "requirements": "Gaming knowledge, community management experience"
            },
            
            # Creator Economy Support (Intermediate)
            "creator_economy": {
                "keywords": ["creator-support", "account-manager", "fan-engagement", "content-assistant", "social-media-manager"],
                "salary_range": "$15-28/hour",
                "companies": ["Creator Agencies", "Patreon", "OnlyFans Agencies", "Social Media Agencies"],
                "requirements": "Social media knowledge, customer service skills"
            }
        }
    },
    
    # ===== SPECIALIZED/EXPERT LEVEL JOBS (Advanced Skills Required) =====
    "expert_level": {
        "description": "Jobs requiring specialized skills or advanced experience",
        "skill_requirements": "Advanced technical skills, specialized knowledge, or 3+ years experience",
        "categories": {
            
            # Advanced AI & Data Science (Expert)
            "advanced_ai_data": {
                "keywords": ["prompt-engineering", "ai-training", "machine-learning", "data-annotation", "model-training"],
                "salary_range": "$20-40/hour",
                "companies": ["Scale AI", "Surge AI", "Outlier AI", "OpenAI Contractors", "Anthropic Contractors"],
                "requirements": "AI/ML knowledge, programming skills, advanced analytical skills"
            },
            
            # Linguistic & Translation Specialists (Expert)
            "linguistic_specialist": {
                "keywords": ["linguistic-annotation", "translation-evaluation", "grammar-analysis", "language-quality"],
                "salary_range": "$18-35/hour",
                "companies": ["TELUS International", "Lionbridge", "iSoftStone", "Appen"],
                "requirements": "Advanced language skills, linguistic education, cultural expertise"
            },
            
            # Technical Content Moderation (Expert)
            "technical_moderation": {
                "keywords": ["trust-safety-specialist", "policy-specialist", "content-reviewer", "safety-analyst"],
                "salary_range": "$22-35/hour",
                "companies": ["Meta", "Google", "Twitter", "TikTok", "Specialized Agencies"],
                "requirements": "Policy knowledge, analytical skills, technical understanding"
            },
            
            # Advanced Data Labeling (Expert)
            "advanced_data_labeling": {
                "keywords": ["3d-labeling", "autonomous-vehicle", "medical-annotation", "technical-annotation"],
                "salary_range": "$20-35/hour",
                "companies": ["Scale AI", "Remotasks", "Surge AI", "Tech Giants"],
                "requirements": "Technical expertise, specialized domain knowledge"
            },
            
            # Freelance AI & Tech (Expert)
            "freelance_ai_tech": {
                "keywords": ["ai-consultant", "ml-freelancer", "prompt-engineer", "dataset-specialist"],
                "salary_range": "$25-60/hour",
                "companies": ["Upwork", "Toptal", "Freelancer.com", "Direct Clients"],
                "requirements": "Advanced technical skills, portfolio, proven experience"
            }
        }
    },
    
    # ===== FLEXIBLE/PART-TIME OPPORTUNITIES =====
    "flexible_opportunities": {
        "description": "Flexible, part-time, or project-based work",
        "skill_requirements": "Varies by opportunity",
        "categories": {
            
            # Microtasks & Gig Work
            "microtasks_gig": {
                "keywords": ["microtasks", "small-tasks", "gig-work", "project-based", "flexible-hours"],
                "salary_range": "$5-20/hour",
                "companies": ["Clickworker", "Microworkers", "Amazon MTurk", "Remotasks"],
                "requirements": "Flexible schedule, task-oriented mindset"
            },
            
            # Research & Testing
            "research_testing": {
                "keywords": ["user-testing", "research-studies", "product-feedback", "usability-testing"],
                "salary_range": "$10-25/hour",
                "companies": ["UserTesting", "Prolific", "Respondent.io", "Research Companies"],
                "requirements": "Analytical thinking, feedback skills"
            }
        }
    }
}

# Sample jobs to demonstrate categorization
SAMPLE_JOBS = [
    # Entry Level Jobs
    {
        "title": "Customer Support Representative",
        "company": "LiveWorld",
        "location": "Remote - Worldwide",
        "url": "https://liveworld.com/careers",
        "source": "LiveWorld",
        "salary": "$15/hour",
        "keywords": ["customer-support", "chat-support"]
    },
    {
        "title": "Content Moderator",
        "company": "ModSquad",
        "location": "Remote - Global",
        "url": "https://modsquad.com/careers",
        "source": "ModSquad",
        "salary": "$16/hour",
        "keywords": ["content-moderator", "community-moderator"]
    },
    {
        "title": "Data Entry Specialist",
        "company": "Clickworker",
        "location": "Remote - Worldwide",
        "url": "https://clickworker.com/jobs",
        "source": "Clickworker",
        "salary": "$12/hour",
        "keywords": ["data-entry", "microtasks"]
    },
    
    # Intermediate Level Jobs
    {
        "title": "Technical Support Specialist",
        "company": "GitLab",
        "location": "Remote - Worldwide",
        "url": "https://about.gitlab.com/jobs",
        "source": "GitLab",
        "salary": "$25/hour",
        "keywords": ["technical-support", "customer-success"]
    },
    {
        "title": "TikTok Content Moderator",
        "company": "ByteDance",
        "location": "Remote - Global",
        "url": "https://careers.tiktok.com",
        "source": "TikTok",
        "salary": "$20/hour",
        "keywords": ["tiktok-moderator", "platform-moderation"]
    },
    {
        "title": "Search Quality Evaluator",
        "company": "TELUS International",
        "location": "Remote - Worldwide",
        "url": "https://telusinternational.com/careers",
        "source": "TELUS International",
        "salary": "$18/hour",
        "keywords": ["search-evaluator", "ai-rater"]
    },
    
    # Expert Level Jobs
    {
        "title": "AI Prompt Engineer",
        "company": "Scale AI",
        "location": "Remote - Worldwide",
        "url": "https://scale.com/careers",
        "source": "Scale AI",
        "salary": "$35/hour",
        "keywords": ["prompt-engineering", "ai-training"]
    },
    {
        "title": "Linguistic Annotation Specialist",
        "company": "Lionbridge",
        "location": "Remote - Global",
        "url": "https://lionbridge.com/careers",
        "source": "Lionbridge",
        "salary": "$28/hour",
        "keywords": ["linguistic-annotation", "language-quality"]
    },
    
    # Flexible Opportunities
    {
        "title": "Microtask Worker",
        "company": "Amazon MTurk",
        "location": "Remote - Flexible",
        "url": "https://mturk.com",
        "source": "Amazon MTurk",
        "salary": "$8-15/hour",
        "keywords": ["microtasks", "gig-work"]
    }
]

class JobCategorizer:
    def __init__(self):
        self.organized_categories = ORGANIZED_JOB_CATEGORIES
        
    def categorize_job(self, job):
        """Categorize a job based on its keywords and requirements"""
        job_keywords = job.get("keywords", [])
        
        for level_name, level_data in self.organized_categories.items():
            for category_name, category_data in level_data["categories"].items():
                category_keywords = category_data["keywords"]
                
                # Check if any job keywords match category keywords
                if any(keyword in job_keywords for keyword in category_keywords):
                    return {
                        "level": level_name,
                        "category": category_name,
                        "category_data": category_data,
                        "level_description": level_data["description"],
                        "skill_requirements": level_data["skill_requirements"]
                    }
        
        return None
    
    def organize_jobs_by_category(self, jobs):
        """Organize jobs into categories by skill level"""
        organized_jobs = {
            "entry_level": [],
            "intermediate_level": [],
            "expert_level": [],
            "flexible_opportunities": []
        }
        
        for job in jobs:
            categorization = self.categorize_job(job)
            if categorization:
                job["categorization"] = categorization
                organized_jobs[categorization["level"]].append(job)
            else:
                # Default to entry level if no match found
                job["categorization"] = {
                    "level": "entry_level",
                    "category": "general",
                    "category_data": {"salary_range": "Competitive", "requirements": "Basic skills"},
                    "level_description": "General opportunities",
                    "skill_requirements": "Basic computer skills"
                }
                organized_jobs["entry_level"].append(job)
        
        return organized_jobs
    
    def format_job_notification(self, organized_jobs):
        """Format organized jobs for Telegram notification"""
        message = f"🎯 **Daily Job Report - {datetime.now().strftime('%Y-%m-%d')}**\n\n"
        
        level_emojis = {
            "entry_level": "🟢",
            "intermediate_level": "🟡", 
            "expert_level": "🔴",
            "flexible_opportunities": "🟣"
        }
        
        level_names = {
            "entry_level": "Entry Level (No Experience Required)",
            "intermediate_level": "Intermediate Level (Some Experience/Skills)",
            "expert_level": "Expert Level (Advanced Skills)",
            "flexible_opportunities": "Flexible Opportunities (Part-time/Project-based)"
        }
        
        total_jobs = 0
        
        for level, jobs in organized_jobs.items():
            if jobs:
                emoji = level_emojis.get(level, "⚪")
                level_name = level_names.get(level, level.replace("_", " ").title())
                
                message += f"{emoji} **{level_name}**\n"
                message += f"📊 {len(jobs)} opportunities found\n\n"
                
                # Group jobs by category within each level
                categories = {}
                for job in jobs:
                    cat = job["categorization"]["category"]
                    if cat not in categories:
                        categories[cat] = []
                    categories[cat].append(job)
                
                for category, category_jobs in categories.items():
                    if category_jobs:
                        cat_data = category_jobs[0]["categorization"]["category_data"]
                        message += f"💼 **{category.replace('_', ' ').title()}** ({len(category_jobs)} jobs)\n"
                        message += f"💰 Salary: {cat_data.get('salary_range', 'Competitive')}\n"
                        message += f"📋 Requirements: {cat_data.get('requirements', 'Basic skills')}\n"
                        
                        # Show first 3 jobs in each category
                        for i, job in enumerate(category_jobs[:3]):
                            message += f"• {job['title']} - {job['company']} ({job['salary']})\n"
                        
                        if len(category_jobs) > 3:
                            message += f"  ... and {len(category_jobs) - 3} more jobs\n"
                        
                        message += "\n"
                
                total_jobs += len(jobs)
                message += "─" * 40 + "\n\n"
        
        message += f"📈 **Total Jobs Found: {total_jobs}**\n"
        message += f"🌍 All jobs are remote and worldwide accessible\n"
        message += f"⏰ Updated: {datetime.now().strftime('%H:%M UTC')}"
        
        return message

def test_job_categorization():
    """Test the job categorization system"""
    print("🧪 Testing Organized Job Categorization System\n")
    print("=" * 60)
    
    categorizer = JobCategorizer()
    
    # Test individual job categorization
    print("\n1. Testing Individual Job Categorization:")
    print("-" * 40)
    
    for job in SAMPLE_JOBS[:3]:
        categorization = categorizer.categorize_job(job)
        print(f"Job: {job['title']}")
        print(f"Company: {job['company']}")
        if categorization:
            print(f"Level: {categorization['level'].replace('_', ' ').title()}")
            print(f"Category: {categorization['category'].replace('_', ' ').title()}")
            print(f"Salary Range: {categorization['category_data']['salary_range']}")
            print(f"Requirements: {categorization['category_data']['requirements']}")
        print()
    
    # Test full job organization
    print("\n2. Testing Full Job Organization:")
    print("-" * 40)
    
    organized_jobs = categorizer.organize_jobs_by_category(SAMPLE_JOBS)
    
    for level, jobs in organized_jobs.items():
        if jobs:
            print(f"\n{level.replace('_', ' ').title()}: {len(jobs)} jobs")
            for job in jobs:
                print(f"  • {job['title']} - {job['company']}")
    
    # Test notification formatting
    print("\n3. Testing Telegram Notification Format:")
    print("-" * 40)
    
    notification = categorizer.format_job_notification(organized_jobs)
    print(notification)
    
    # Show category breakdown
    print("\n4. Category System Overview:")
    print("-" * 40)
    
    for level_name, level_data in ORGANIZED_JOB_CATEGORIES.items():
        print(f"\n{level_name.replace('_', ' ').title()}:")
        print(f"Description: {level_data['description']}")
        print(f"Requirements: {level_data['skill_requirements']}")
        print("Categories:")
        for cat_name, cat_data in level_data['categories'].items():
            print(f"  • {cat_name.replace('_', ' ').title()}: {cat_data['salary_range']}")

if __name__ == "__main__":
    test_job_categorization()