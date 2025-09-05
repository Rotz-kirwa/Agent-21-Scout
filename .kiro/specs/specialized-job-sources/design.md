# Design Document

## Overview

This design extends the existing telegram job bot architecture to include specialized job sources focusing on content moderation, community management, virtual assistance, and platform-specific roles. The implementation follows the established pattern of individual fetch functions that return standardized job objects, with seamless integration into the existing scout workflow.

The specialized sources target high-demand remote work opportunities in emerging digital economy sectors, including adult/fan subscription platforms, major social media platforms, BPO agencies, gaming companies, AI training platforms, and specialized moderator companies.

## Architecture

### Current System Integration

The new specialized job sources will integrate with the existing `JobScout` class architecture:

```python
class JobScout:
    def __init__(self):
        self.total_jobs = 0
        self.sources = []
        self.jobs_found = []
    
    # Existing fetch functions...
    
    # New specialized fetch functions
    def fetch_adult_platform_jobs(self, keywords)
    def fetch_social_media_platform_jobs_extended(self, keywords)
    def fetch_bpo_agencies_extended_jobs(self, keywords)
    def fetch_gaming_companies_jobs(self, keywords)
    def fetch_ai_training_platforms_jobs(self, keywords)
    def fetch_specialized_moderator_companies_jobs(self, keywords)
```

### Data Flow Architecture

1. **Job Fetching Phase**: Each specialized source function fetches jobs independently
2. **Data Standardization**: All jobs conform to the existing job object structure
3. **Aggregation**: Jobs are added to the main `jobs_found` list
4. **Notification**: Jobs are sent via existing Telegram notification system

### Error Handling Strategy

- **Graceful Degradation**: Failed sources don't block other sources
- **Fallback Content**: Static job listings when APIs are unavailable
- **Logging**: Comprehensive error logging for debugging
- **Timeout Management**: Reasonable timeouts to prevent hanging

## Components and Interfaces

### 1. Adult/Fan Platform Job Fetcher

**Function**: `fetch_adult_platform_jobs(self, keywords)`

**Purpose**: Fetches legitimate employment opportunities from adult/fan subscription platforms

**Implementation Strategy**:
- **Direct API Approach**: Limited due to platform restrictions
- **Curated Job Listings**: Maintain curated lists of known opportunities
- **Third-party Job Boards**: Leverage job boards that list these opportunities
- **Agency Partnerships**: Include agencies that specialize in creator support

**Job Categories Targeted**:
- Chat moderators
- Account managers
- Customer support specialists
- Content promoters
- Virtual assistants for creators

**Sample Implementation**:
```python
def fetch_adult_platform_jobs(self, keywords):
    jobs = []
    
    # Creator economy and chat moderation keywords
    if any(word in keywords for word in ["chat", "moderator", "assistant", "support", "creator"]):
        # Curated opportunities from legitimate agencies
        jobs.extend([
            {
                "title": "Chat Moderator - Creator Platforms",
                "company": "Creator Support Agency",
                "location": "Remote - Worldwide",
                "url": "https://example-agency.com/careers",
                "source": "Creator Economy",
                "salary": "$15-25/hour"
            }
        ])
    
    return jobs
```

### 2. Enhanced Social Media Platform Job Fetcher

**Function**: `fetch_social_media_platform_jobs_extended(self, keywords)`

**Purpose**: Expands existing social media job fetching to include direct platform opportunities

**Implementation Strategy**:
- **Greenhouse API Integration**: Many platforms use Greenhouse for hiring
- **Direct Career Page Scraping**: For platforms with public job listings
- **BPO Partner Integration**: Include contractors that work with these platforms
- **LinkedIn API**: Leverage LinkedIn's job search for platform-specific roles

**Platforms Covered**:
- TikTok (ByteDance)
- Meta (Facebook, Instagram, WhatsApp)
- YouTube (Google)
- Twitter/X
- Reddit
- Twitch
- Discord
- Snapchat

**Sample Implementation**:
```python
def fetch_social_media_platform_jobs_extended(self, keywords):
    jobs = []
    
    # Content moderation and community support keywords
    if any(word in keywords for word in ["moderator", "community", "trust", "safety", "support"]):
        # TikTok/ByteDance opportunities
        jobs.extend(self._fetch_bytedance_jobs(keywords))
        
        # Meta opportunities
        jobs.extend(self._fetch_meta_jobs(keywords))
        
        # YouTube/Google opportunities
        jobs.extend(self._fetch_youtube_jobs(keywords))
    
    return jobs
```

### 3. Enhanced BPO Agency Job Fetcher

**Function**: `fetch_bpo_agencies_extended_jobs(self, keywords)`

**Purpose**: Expands existing BPO job fetching to include more agencies and specific platform partnerships

**Implementation Strategy**:
- **Agency Career APIs**: Direct integration with agency job APIs
- **Platform Partnership Mapping**: Identify which agencies serve which platforms
- **Geographic Filtering**: Focus on agencies that hire globally
- **Role Specialization**: Target specific roles like content moderation and chat support

**Agencies Covered**:
- Teleperformance
- Majorel
- Accenture
- Cognizant
- TaskUs
- Genpact
- TTEC
- Concentrix
- Alorica
- Foundever (formerly Sitel)
- Arvato (Bertelsmann)
- HGS (Hinduja Global Solutions)

### 4. Gaming Company Job Fetcher

**Function**: `fetch_gaming_companies_jobs(self, keywords)`

**Purpose**: Fetches community management and moderation roles from gaming companies

**Implementation Strategy**:
- **Gaming Company APIs**: Direct integration where available
- **Gaming Job Boards**: Specialized gaming industry job boards
- **Community Platform Integration**: Discord, Reddit gaming communities
- **Esports Organizations**: Include esports community management roles

**Companies Covered**:
- Roblox
- Epic Games (Fortnite)
- Activision Blizzard
- Riot Games (League of Legends)
- Twitch (Amazon-owned)
- IMVU / Second Life (Linden Lab)

### 5. AI Training Platform Job Fetcher

**Function**: `fetch_ai_training_platforms_jobs(self, keywords)`

**Purpose**: Fetches flexible microtask opportunities from AI training platforms

**Implementation Strategy**:
- **Platform APIs**: Direct integration with platform job APIs
- **Microtask Aggregation**: Combine multiple small opportunities
- **Skill-based Filtering**: Match opportunities to user skills
- **Flexible Work Emphasis**: Highlight the flexible nature of these roles

**Platforms Covered**:
- Appen (search evaluation, speech transcription, image/video labeling)
- TELUS International AI (formerly Lionbridge AI/RaterLabs - ads evaluator, social media evaluator, data annotation)
- Scale AI (data labeling for machine learning, sometimes via Surge AI)
- Surge AI (high-quality data annotation tasks, text/content evaluation)
- Outlier AI (text/data labeling, prompt testing for LLMs)
- Remotasks by Scale AI (3D labeling, image annotation, self-driving car datasets)
- Clickworker (small AI training tasks, data entry, text classification, surveys)
- OneForma by Pactera Edge (data collection, testing, annotation projects)
- iSoftStone (AI training, text annotation, linguistic tasks)
- Microworkers (microtasks including AI model training jobs)
- Tech Giant Contractors (Google via TELUS/Appen/Lionbridge, Microsoft via Appen/OneForma/TELUS, Amazon MTurk/AWS AI, Meta via Accenture/Cognizant/TELUS)
- Freelance Platforms (Upwork, Fiverr, Freelancer.com, Toptal for AI gigs)

### 6. Specialized Moderator Company Job Fetcher

**Function**: `fetch_specialized_moderator_companies_jobs(self, keywords)`

**Purpose**: Fetches jobs from companies that specialize in community management and virtual assistance

**Implementation Strategy**:
- **Specialized Company APIs**: Direct integration with company job systems
- **Service Provider Networks**: Include networks of specialized service providers
- **Client Platform Mapping**: Identify which clients these companies serve
- **Skill Specialization**: Focus on community management and moderation skills

**Companies Covered**:
- ModSquad
- SupportNinja
- Boldly
- Time Etc
- Belay Solutions
- CloudTask

## Data Models

### Enhanced Job Object Structure

The existing job object structure will be maintained for consistency:

```python
job = {
    "title": str,           # Job title
    "company": str,         # Company name
    "location": str,        # Location (typically "Remote - Worldwide")
    "url": str,            # Application URL
    "source": str,         # Source platform/company
    "salary": str,         # Salary range or "Competitive"
    "category": str,       # New: Job category for filtering
    "platform_served": str, # New: Which platform this role serves (optional)
    "work_type": str       # New: "full-time", "part-time", "microtask", "flexible"
}
```

### Organized Job Category System

The job categories will be organized hierarchically by skill level, requirements, and specialization to help users find jobs that match their qualifications:

```python
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

# Simplified category mapping for backward compatibility
CATEGORIES.update({
    # Entry Level Categories
    "basic-customer-support": ["customer-support", "chat-support", "email-support", "helpdesk", "live-chat"],
    "basic-content-moderation": ["content-moderator", "community-moderator", "social-media-moderator", "chat-moderator"],
    "basic-data-entry": ["data-entry", "microtasks", "surveys", "basic-annotation", "clickworker"],
    "basic-virtual-assistant": ["virtual-assistant", "admin-assistant", "scheduling", "email-management"],
    
    # Intermediate Level Categories  
    "advanced-customer-support": ["technical-support", "customer-success", "account-manager", "support-specialist"],
    "platform-moderation": ["tiktok-moderator", "facebook-moderator", "youtube-reviewer", "instagram-safety", "trust-safety"],
    "ai-training-evaluation": ["search-evaluator", "ads-evaluator", "ai-rater", "content-evaluator", "social-media-evaluator"],
    "gaming-community": ["gaming-moderator", "player-support", "community-manager", "esports-support"],
    "creator-economy": ["creator-support", "account-manager", "fan-engagement", "content-assistant", "social-media-manager"],
    
    # Expert Level Categories
    "advanced-ai-data": ["prompt-engineering", "ai-training", "machine-learning", "data-annotation", "model-training"],
    "linguistic-specialist": ["linguistic-annotation", "translation-evaluation", "grammar-analysis", "language-quality"],
    "technical-moderation": ["trust-safety-specialist", "policy-specialist", "content-reviewer", "safety-analyst"],
    "advanced-data-labeling": ["3d-labeling", "autonomous-vehicle", "medical-annotation", "technical-annotation"],
    "freelance-ai-tech": ["ai-consultant", "ml-freelancer", "prompt-engineer", "dataset-specialist"],
    
    # Flexible Categories
    "microtasks-gig": ["microtasks", "small-tasks", "gig-work", "project-based", "flexible-hours"],
    "research-testing": ["user-testing", "research-studies", "product-feedback", "usability-testing"]
})
```

## Error Handling

### Graceful Degradation Strategy

1. **Individual Function Isolation**: Each fetch function is wrapped in try-catch blocks
2. **Fallback Content**: When APIs fail, provide curated static job listings
3. **Partial Success Handling**: Continue processing even if some sources fail
4. **User Notification**: Include source availability in daily summaries

### Error Logging

```python
def fetch_with_error_handling(self, fetch_function, source_name, keywords):
    try:
        jobs = fetch_function(keywords)
        print(f"✅ {source_name}: Found {len(jobs)} jobs")
        return jobs
    except RequestException as e:
        print(f"❌ {source_name} API error: {e}")
        return self._get_fallback_jobs(source_name, keywords)
    except Exception as e:
        print(f"⚠️ {source_name} unexpected error: {e}")
        return []
```

### Timeout Management

- **API Timeouts**: 15-second timeout for all API calls
- **Rate Limiting**: 2-second delays between source categories
- **Retry Logic**: Single retry for failed requests with exponential backoff

## Testing Strategy

### Unit Testing

1. **Individual Function Tests**: Test each fetch function independently
2. **Mock API Responses**: Use mock responses for consistent testing
3. **Error Condition Tests**: Test error handling and fallback mechanisms
4. **Data Structure Validation**: Ensure all returned jobs match expected structure

### Integration Testing

1. **End-to-End Flow**: Test complete job fetching and notification flow
2. **Source Combination**: Test multiple sources working together
3. **Error Recovery**: Test system behavior when multiple sources fail
4. **Performance Testing**: Ensure new sources don't significantly impact execution time

### Test Data Management

```python
# Mock job data for testing
MOCK_ADULT_PLATFORM_JOBS = [
    {
        "title": "Chat Moderator - Creator Platform",
        "company": "Test Creator Agency",
        "location": "Remote - Worldwide",
        "url": "https://test.com/job1",
        "source": "Test Source",
        "salary": "$20/hour"
    }
]
```

### Validation Tests

1. **URL Validation**: Ensure all job URLs are valid and accessible
2. **Salary Format**: Validate salary information follows expected formats
3. **Location Consistency**: Ensure location information is consistent
4. **Category Mapping**: Verify jobs are properly categorized

## Implementation Phases

### Phase 1: Core Infrastructure
- Implement base fetch functions with error handling
- Add new categories to CATEGORIES dictionary
- Create fallback job data structures
- Implement enhanced error logging

### Phase 2: Adult/Fan Platform Integration
- Implement `fetch_adult_platform_jobs()`
- Create curated job listings for creator economy roles
- Add professional language filtering
- Test integration with existing system

### Phase 3: Social Media Platform Enhancement
- Implement `fetch_social_media_platform_jobs_extended()`
- Add Greenhouse API integration for major platforms
- Create platform-specific job categorization
- Implement BPO contractor mapping

### Phase 4: BPO and Gaming Integration
- Implement `fetch_bpo_agencies_extended_jobs()`
- Implement `fetch_gaming_companies_jobs()`
- Add agency-platform relationship mapping
- Create gaming-specific job categories

### Phase 5: AI Training and Specialized Companies
- Implement `fetch_ai_training_platforms_jobs()`
- Implement `fetch_specialized_moderator_companies_jobs()`
- Add microtask work type classification
- Create specialized company integration

### Phase 6: Testing and Optimization
- Comprehensive testing of all new sources
- Performance optimization
- Error handling refinement
- Documentation updates

## Security Considerations

### Content Filtering
- **Professional Language**: Ensure all job descriptions use professional language
- **Legitimate Opportunities**: Focus only on legitimate employment opportunities
- **Age Verification**: Include appropriate disclaimers for adult platform roles
- **Privacy Protection**: Avoid collecting or storing sensitive user data

### API Security
- **Rate Limiting**: Respect API rate limits to avoid blocking
- **User Agent**: Use appropriate user agents for web scraping
- **HTTPS Only**: Ensure all API calls use HTTPS
- **Token Management**: Securely manage any required API tokens

### Data Validation
- **Input Sanitization**: Sanitize all job data before processing
- **URL Validation**: Validate all job URLs before including in notifications
- **Content Moderation**: Filter out inappropriate content automatically
- **Source Verification**: Verify the legitimacy of job sources

## Performance Considerations

### Execution Time
- **Parallel Processing**: Consider parallel execution of independent fetch functions
- **Caching**: Implement caching for frequently accessed data
- **Batch Processing**: Process multiple jobs efficiently
- **Timeout Optimization**: Balance thoroughness with execution speed

### Resource Usage
- **Memory Management**: Efficiently manage job data structures
- **Network Usage**: Minimize unnecessary API calls
- **Storage**: Optimize temporary data storage
- **Logging**: Balance comprehensive logging with performance

### Scalability
- **Source Addition**: Design for easy addition of new job sources
- **Category Expansion**: Allow for easy category expansion
- **Geographic Scaling**: Support for region-specific job sources
- **Volume Handling**: Handle increasing job volumes efficiently