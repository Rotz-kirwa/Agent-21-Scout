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
        },
        # Amazon-related Remote Opportunities
        {
            "title": "Amazon FBA Virtual Assistant",
            "company": "Various Amazon Sellers",
            "location": "Remote - Worldwide",
            "url": "https://www.upwork.com/freelance-jobs/amazon-fba/",
            "source": "Upwork",
            "salary": "$10-30/hour"
        },
        {
            "title": "AWS Cloud Support Associate",
            "company": "Amazon Web Services",
            "location": "Remote - Global",
            "url": "https://www.amazon.jobs/en/search?base_query=cloud+support&loc_query=",
            "source": "Amazon Jobs",
            "salary": "$40-70k/year"
        },
        # Major Remote-First Companies (Kenya-Friendly)
        {
            "title": "Software Engineer",
            "company": "GitLab",
            "location": "Remote - Worldwide",
            "url": "https://about.gitlab.com/jobs/",
            "source": "GitLab",
            "salary": "$70-130k/year"
        },
        {
            "title": "Happiness Engineer",
            "company": "Automattic",
            "location": "Remote - Worldwide",
            "url": "https://automattic.com/work-with-us/",
            "source": "Automattic",
            "salary": "$50-80k/year"
        },
        {
            "title": "Customer Champion",
            "company": "Zapier",
            "location": "Remote - Worldwide",
            "url": "https://zapier.com/jobs",
            "source": "Zapier",
            "salary": "$45-75k/year"
        },
        {
            "title": "Software Developer",
            "company": "Andela",
            "location": "Remote - 135+ Countries",
            "url": "https://andela.com/careers/",
            "source": "Andela",
            "salary": "$30-80k/year"
        },
        {
            "title": "Content Creator",
            "company": "Buffer",
            "location": "Remote - Worldwide",
            "url": "https://buffer.com/journey",
            "source": "Buffer",
            "salary": "$40-70k/year"
        },
        {
            "title": "Mobile Developer",
            "company": "Doist",
            "location": "Remote - Worldwide",
            "url": "https://doist.com/careers",
            "source": "Doist",
            "salary": "$60-100k/year"
        },
        {
            "title": "Customer Success Manager",
            "company": "Remote.com",
            "location": "Remote - Worldwide",
            "url": "https://remote.com/careers",
            "source": "Remote.com",
            "salary": "$45-75k/year"
        },
        {
            "title": "Account Executive",
            "company": "Deel",
            "location": "Remote - 100+ Countries",
            "url": "https://www.deel.com/careers",
            "source": "Deel",
            "salary": "$50-100k/year"
        },
        {
            "title": "Customer Support Specialist",
            "company": "Binance",
            "location": "Remote - Worldwide",
            "url": "https://www.binance.com/en/careers",
            "source": "Binance",
            "salary": "$25-50k/year"
        },
        {
            "title": "Community Relations Specialist",
            "company": "Wikimedia Foundation",
            "location": "Remote - Worldwide",
            "url": "https://wikimediafoundation.org/about/jobs/",
            "source": "Wikimedia",
            "salary": "$45-80k/year"
        }
    ]
    return jobs

def get_kenya_friendly_jobs():
    """Get worldwide remote jobs accessible from Kenya"""
    return fetch_worldwide_remote_jobs()