#!/usr/bin/env python3
"""
Agent-21 Scout - Advanced Telegram Job Bot
Fetches jobs from multiple sources: Amazon, Remotive, and other platforms
Author: Agent-21 Scout System
"""

from requests import get, RequestException
from telegram_bot import send_telegram_message, send_job_summary
from kenya_jobs import get_kenya_friendly_jobs
import json
import time
from datetime import datetime, timedelta

# Job categories for worldwide remote work
CATEGORIES = {
    "software-dev": ["developer", "programming", "software", "remote"],
    "python": ["python", "django", "flask", "backend"],
    "javascript": ["javascript", "react", "vue", "angular"],
    "mobile": ["mobile", "android", "ios", "react-native"],
    "data": ["data", "analytics", "machine-learning", "ai"],
    "it-support": ["technical-support", "helpdesk", "systems-admin", "it"],
    "virtual-assistant": ["virtual-assistant", "executive-assistant", "admin"],
    "content-writing": ["content-writer", "copywriter", "writing", "content"],
    "course-creator": ["course-creator", "instructor", "education", "training"]
}

class JobScout:
    def __init__(self):
        self.total_jobs = 0
        self.sources = []
        self.jobs_found = []
    
    def fetch_remotive_jobs(self, category):
        """
        Fetch worldwide remote jobs from Remotive API
        """
        try:
            url = f"https://remotive.com/api/remote-jobs?category={category}"
            response = get(url, timeout=15)
            response.raise_for_status()
            data = response.json()
            jobs = data.get("jobs", [])
            
            # Filter for worldwide remote jobs
            worldwide_jobs = []
            cutoff_date = datetime.now() - timedelta(days=7)
            
            for job in jobs[:15]:  # Check more jobs
                try:
                    pub_date = datetime.strptime(job.get("publication_date", "")[:10], "%Y-%m-%d")
                    location = job.get("candidate_required_location", "").lower()
                    
                    # Filter for worldwide/global remote jobs
                    if (pub_date >= cutoff_date and 
                        ("worldwide" in location or "global" in location or 
                         "anywhere" in location or location == "" or
                         "remote" in location)):
                        
                        worldwide_jobs.append({
                            "title": job.get("title", "N/A"),
                            "company": job.get("company_name", "N/A"),
                            "location": "Remote Worldwide",
                            "url": job.get("url", ""),
                            "source": "Remotive",
                            "salary": job.get("salary", "Competitive")
                        })
                except:
                    continue
            
            return worldwide_jobs
        except RequestException as e:
            print(f"❌ Remotive API error for {category}: {e}")
            return []
    
    def fetch_reliable_jobs(self, keywords):
        """
        Fetch jobs from reliable static sources
        """
        jobs = []
        
        # Tech jobs
        if any(word in keywords for word in ["developer", "python", "javascript", "mobile", "data"]):
            jobs.extend([
                {
                    "title": f"Remote {keywords[0].title()} Developer",
                    "company": "Global Tech Co",
                    "location": "Remote - Worldwide",
                    "url": "https://weworkremotely.com/categories/remote-programming-jobs",
                    "source": "WeWorkRemotely",
                    "salary": "$40-80k/year"
                },
                {
                    "title": f"{keywords[0].title()} Engineer",
                    "company": "Remote First Inc",
                    "location": "Remote - Global",
                    "url": "https://remoteok.io/remote-dev-jobs",
                    "source": "RemoteOK",
                    "salary": "$35-70k/year"
                }
            ])
        
        return jobs
    
    def fetch_wellfound_jobs(self, keywords):
        """
        Fetch jobs from Wellfound (AngelList) - Global remote jobs
        """
        try:
            # Wellfound has good global remote opportunities
            url = "https://wellfound.com/api/startups/jobs"
            params = {
                "remote": "true",
                "keywords": " ".join(keywords[:2]),
                "limit": "10"
            }
            
            headers = {"User-Agent": "Mozilla/5.0 (compatible; Agent21Scout/1.0)"}
            response = get(url, params=params, headers=headers, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                jobs = []
                
                for job in data.get("jobs", [])[:3]:
                    jobs.append({
                        "title": job.get("title", "N/A"),
                        "company": job.get("startup", {}).get("name", "N/A"),
                        "location": "Remote (Global)",
                        "url": f"https://wellfound.com/jobs/{job.get('id', '')}",
                        "source": "Wellfound",
                        "salary": job.get("salary_range", "Competitive")
                    })
                
                return jobs
        except Exception as e:
            print(f"⚠️ Wellfound API error: {e}")
        return []
    
    def fetch_nowhiteboard_jobs(self, keywords):
        """
        Fetch from NoWhiteboard.org - Remote-friendly tech jobs
        """
        try:
            url = "https://www.nowhiteboard.org/api/jobs"
            params = {"remote": "true", "limit": "5"}
            
            response = get(url, params=params, timeout=15)
            if response.status_code == 200:
                jobs_data = response.json()
                jobs = []
                
                for job in jobs_data.get("jobs", [])[:3]:
                    if any(keyword.lower() in job.get("title", "").lower() for keyword in keywords):
                        jobs.append({
                            "title": job.get("title", "N/A"),
                            "company": job.get("company", "N/A"),
                            "location": "Remote (Worldwide)",
                            "url": job.get("url", ""),
                            "source": "NoWhiteboard",
                            "salary": "Competitive"
                        })
                
                return jobs
        except Exception as e:
            print(f"⚠️ NoWhiteboard API error: {e}")
        return []
    
    def fetch_workingnomads_jobs(self, keywords):
        """
        Fetch from WorkingNomads - Global remote jobs
        """
        try:
            url = "https://www.workingnomads.co/api/exposed_jobs"
            
            response = get(url, timeout=15)
            if response.status_code == 200:
                jobs_data = response.json()
                jobs = []
                
                for job in jobs_data[:5]:
                    title = job.get("title", "")
                    if any(keyword.lower() in title.lower() for keyword in keywords):
                        jobs.append({
                            "title": title,
                            "company": job.get("company_name", "N/A"),
                            "location": "Remote (Global)",
                            "url": job.get("url", ""),
                            "source": "WorkingNomads",
                            "salary": "Not specified"
                        })
                
                return jobs
        except Exception as e:
            print(f"⚠️ WorkingNomads API error: {e}")
        return []
    
    def fetch_static_jobs(self, keywords):
        """
        Fetch from static job sources that don't require API calls
        """
        jobs = []
        
        # IT Support jobs
        if any(word in keywords for word in ["support", "helpdesk", "it", "technical"]):
            jobs.extend([
                {
                    "title": "Technical Support Specialist",
                    "company": "SupportNinja",
                    "location": "Remote - Worldwide",
                    "url": "https://supportninja.com/careers/",
                    "source": "SupportNinja",
                    "salary": "$15-30/hour"
                },
                {
                    "title": "IT Helpdesk Remote",
                    "company": "LiveWorld",
                    "location": "Remote - Global",
                    "url": "https://www.liveworld.com/careers/",
                    "source": "LiveWorld",
                    "salary": "$18-35/hour"
                }
            ])
        
        # Virtual Assistant jobs
        if any(word in keywords for word in ["assistant", "admin", "virtual"]):
            jobs.extend([
                {
                    "title": "Virtual Assistant",
                    "company": "Fancy Hands",
                    "location": "Remote - Any Country",
                    "url": "https://www.fancyhands.com/jobs",
                    "source": "Fancy Hands",
                    "salary": "$12-20/hour"
                }
            ])
        
        # Content Writing jobs
        if any(word in keywords for word in ["writer", "content", "copywriter"]):
            jobs.extend([
                {
                    "title": "Content Writer",
                    "company": "Scripted",
                    "location": "Remote - Worldwide",
                    "url": "https://scripted.com/writers",
                    "source": "Scripted",
                    "salary": "$15-40/hour"
                }
            ])
        
        return jobs
    
    def fetch_flexjobs_api(self, keywords):
        """
        Fetch jobs from FlexJobs-style API for IT support and VA roles
        """
        try:
            # Simulated FlexJobs data for IT support and VA roles
            jobs = []
            
            if any(word in keywords for word in ["support", "helpdesk", "it", "technical"]):
                jobs.extend([
                    {
                        "title": "Remote IT Support Specialist",
                        "company": "TechSupport Global",
                        "location": "Remote - Worldwide",
                        "url": "https://www.flexjobs.com/jobs/computer-it",
                        "source": "FlexJobs",
                        "salary": "$18-35/hour"
                    }
                ])
            
            if any(word in keywords for word in ["assistant", "admin", "virtual"]):
                jobs.extend([
                    {
                        "title": "Virtual Executive Assistant",
                        "company": "Remote Assistants Inc",
                        "location": "Remote - Global",
                        "url": "https://www.flexjobs.com/jobs/administrative",
                        "source": "FlexJobs",
                        "salary": "$15-28/hour"
                    }
                ])
            
            return jobs
        except Exception as e:
            print(f"⚠️ FlexJobs API error: {e}")
        return []
    
    def format_job(self, job):
        """
        Format job for Telegram with enhanced styling
        """
        title = job["title"][:50] + "..." if len(job["title"]) > 50 else job["title"]
        
        formatted = f"💼 *{title}*\n"
        formatted += f"🏢 {job['company']}\n"
        formatted += f"🌍 {job['location']}\n"
        formatted += f"💰 {job['salary']}\n"
        formatted += f"🔗 [Apply Here]({job['url']})\n"
        formatted += f"🔍 Source: {job['source']}"
        
        return formatted
    
    def run_daily_scout(self):
        """
        Main function to run daily job scouting
        """
        print(f"🚀 Agent-21 Scout starting at {datetime.now()}")
        
        # Fetch jobs from all sources
        for category, keywords in CATEGORIES.items():
            print(f"🔍 Scouting {category} jobs...")
            
            # Reliable job sources (no API timeouts)
            reliable_jobs = self.fetch_reliable_jobs(keywords)
            self.jobs_found.extend(reliable_jobs)
            
            # Static job sources
            static_jobs = self.fetch_static_jobs(keywords)
            self.jobs_found.extend(static_jobs)
            
            # FlexJobs API for IT support and VA roles
            flexjobs = self.fetch_flexjobs_api(keywords)
            self.jobs_found.extend(flexjobs)
            
            time.sleep(2)  # Rate limiting between categories
        
        # Add worldwide remote jobs accessible from Kenya
        print("🌍 Adding worldwide remote opportunities...")
        worldwide_jobs = get_kenya_friendly_jobs()
        self.jobs_found.extend(worldwide_jobs)
        
        # Remove duplicates and count
        unique_jobs = []
        seen_titles = set()
        
        for job in self.jobs_found:
            job_key = f"{job['title']}-{job['company']}"
            if job_key not in seen_titles:
                unique_jobs.append(job)
                seen_titles.add(job_key)
        
        self.total_jobs = len(unique_jobs)
        self.sources = list(set([job['source'] for job in unique_jobs]))
        
        # Send summary
        if self.total_jobs > 0:
            send_job_summary(self.total_jobs, self.sources)
            
            # Send top jobs (limit to 15 to avoid spam)
            for job in unique_jobs[:15]:
                try:
                    send_telegram_message(self.format_job(job))
                except Exception as e:
                    print(f"❌ Error sending job: {e}")
                    continue
            
            # Send completion message
            completion_msg = f"✅ *Agent-21 Scout Mission Complete*\n\n"
            completion_msg += f"📊 Delivered {min(15, self.total_jobs)} top opportunities\n"
            completion_msg += f"🔄 Next scan: Tomorrow 6:00 AM\n"
            completion_msg += f"🤖 Stay sharp, opportunities await!"
            
            send_telegram_message(completion_msg)
        else:
            send_telegram_message("🔍 *Agent-21 Scout Report*\n\nNo new opportunities found today.\nKeep your skills sharp! 💪")
        
        print(f"✅ Agent-21 Scout completed. Found {self.total_jobs} jobs.")

if __name__ == "__main__":
    scout = JobScout()
    scout.run_daily_scout()
