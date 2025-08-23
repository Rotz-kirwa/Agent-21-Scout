#!/usr/bin/env python3
"""
Kenya-Specific Job Sources for Agent-21 Scout
Focuses on remote jobs that accept Kenyan developers
"""

from requests import get, RequestException
import time

def fetch_worldwide_remote_jobs():
    """Fetch jobs from platforms that accept worldwide remote workers"""
    jobs = [
        # Development Jobs
        {
            "title": "Remote Full-Stack Developer",
            "company": "Toptal (Worldwide)",
            "location": "Remote - Any Country",
            "url": "https://www.toptal.com/developers",
            "source": "Toptal",
            "salary": "$30-80/hour"
        },
        {
            "title": "Python Developer",
            "company": "Upwork Global",
            "location": "Remote - Worldwide",
            "url": "https://www.upwork.com/freelance-jobs/development/",
            "source": "Upwork",
            "salary": "$15-60/hour"
        },
        # IT Support Jobs
        {
            "title": "Technical Support Specialist",
            "company": "Remote.co",
            "location": "Remote - Worldwide",
            "url": "https://remote.co/remote-jobs/customer-service/",
            "source": "Remote.co",
            "salary": "$15-35/hour"
        },
        {
            "title": "IT Helpdesk (Remote)",
            "company": "FlexJobs",
            "location": "Remote - Global",
            "url": "https://www.flexjobs.com/jobs/computer-it",
            "source": "FlexJobs",
            "salary": "$18-40/hour"
        },
        {
            "title": "Systems Administrator",
            "company": "We Work Remotely",
            "location": "Remote - Any Location",
            "url": "https://weworkremotely.com/categories/remote-devops-sysadmin-jobs",
            "source": "WeWorkRemotely",
            "salary": "$25-60/hour"
        },
        # Virtual Assistant Jobs
        {
            "title": "Virtual Assistant (VA)",
            "company": "Belay",
            "location": "Remote - Worldwide",
            "url": "https://www.belaysolutions.com/careers/",
            "source": "Belay",
            "salary": "$12-25/hour"
        },
        {
            "title": "Executive Assistant (Remote)",
            "company": "Time Etc",
            "location": "Remote - Global",
            "url": "https://web.timeetc.com/virtual-assistant-jobs/",
            "source": "Time Etc",
            "salary": "$15-30/hour"
        },
        # Content Writing Jobs
        {
            "title": "Content Writer / Copywriter",
            "company": "Contently",
            "location": "Remote - Any Country",
            "url": "https://contently.com/freelancers/",
            "source": "Contently",
            "salary": "$20-80/hour"
        },
        {
            "title": "Content Writer",
            "company": "WriterAccess",
            "location": "Remote - Worldwide",
            "url": "https://www.writeraccess.com/writers/",
            "source": "WriterAccess",
            "salary": "$15-50/hour"
        },
        # Course Creator Jobs
        {
            "title": "Course Creator",
            "company": "Udemy",
            "location": "Remote - Global",
            "url": "https://www.udemy.com/teaching/",
            "source": "Udemy",
            "salary": "Revenue Share"
        },
        {
            "title": "Online Instructor",
            "company": "Skillshare",
            "location": "Remote - Worldwide",
            "url": "https://www.skillshare.com/teach",
            "source": "Skillshare",
            "salary": "Revenue Share"
        }
    ]
    return jobs

def get_kenya_friendly_jobs():
    """Get worldwide remote jobs accessible from Kenya"""
    return fetch_worldwide_remote_jobs()