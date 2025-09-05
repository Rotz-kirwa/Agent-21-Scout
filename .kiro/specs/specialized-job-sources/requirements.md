# Requirements Document

## Introduction

This feature expands the existing telegram job bot to include specialized job sources that focus on content moderation, community management, virtual assistance, and platform-specific roles. These sources include adult/fan subscription platforms, major social media platforms, BPO/outsourcing agencies, gaming companies, AI training platforms, and specialized moderator companies. The expansion targets high-demand remote work opportunities in emerging digital economy sectors.

## Requirements

### Requirement 1

**User Story:** As a job seeker looking for content moderation work, I want to receive job notifications from adult/fan subscription platforms, so that I can find legitimate remote work opportunities as chat moderators, account managers, and customer support specialists.

#### Acceptance Criteria

1. WHEN the job scout runs THEN the system SHALL fetch jobs from adult/fan subscription platforms including OnlyFans, Fansly, FanCentro, AdmireMe, ManyVids, PocketStars, Patreon, and JustForFans
2. WHEN fetching adult platform jobs THEN the system SHALL include roles for chat moderators, account managers, promoters, and customer support
3. WHEN adult platform jobs are found THEN the system SHALL categorize them under "creator-economy" and "chat-moderation" categories
4. WHEN adult platform jobs are displayed THEN the system SHALL maintain professional language and focus on legitimate employment opportunities

### Requirement 2

**User Story:** As a job seeker interested in social media work, I want to receive notifications for content moderation and community operations roles from major platforms, so that I can work directly with companies like TikTok, Meta, YouTube, and Twitter.

#### Acceptance Criteria

1. WHEN the job scout runs THEN the system SHALL fetch jobs from major social media platforms including TikTok (ByteDance), Meta (Facebook, Instagram, WhatsApp), YouTube (Google), Twitter/X, Reddit, Twitch, Discord, and Snapchat
2. WHEN fetching social media platform jobs THEN the system SHALL include roles for content moderators, community support specialists, trust & safety specialists, and account operations
3. WHEN social media platform jobs are found THEN the system SHALL categorize them under "content-moderation", "social-media-tasks", and "platform-support" categories
4. WHEN social media platform jobs are displayed THEN the system SHALL specify which platform the role supports

### Requirement 3

**User Story:** As a job seeker looking for stable remote work, I want to receive notifications from established BPO and outsourcing agencies, so that I can find consistent employment with companies that provide services to major platforms.

#### Acceptance Criteria

1. WHEN the job scout runs THEN the system SHALL fetch jobs from BPO agencies including Teleperformance, Majorel, Accenture, Cognizant, TaskUs, Genpact, TTEC, Concentrix, Alorica, Foundever, Arvato, and HGS
2. WHEN fetching BPO agency jobs THEN the system SHALL include roles for chat support, email support, content moderation, customer success, and virtual assistant work
3. WHEN BPO agency jobs are found THEN the system SHALL categorize them under "bpo-outsourcing", "customer-support", and "virtual-assistant" categories
4. WHEN BPO agency jobs are displayed THEN the system SHALL indicate which platforms or clients the agency serves

### Requirement 4

**User Story:** As a gaming enthusiast seeking remote work, I want to receive notifications for community management and moderation roles from gaming companies, so that I can combine my passion for gaming with employment opportunities.

#### Acceptance Criteria

1. WHEN the job scout runs THEN the system SHALL fetch jobs from gaming companies including Roblox, Epic Games, Activision Blizzard, Riot Games, Twitch, IMVU, and Second Life (Linden Lab)
2. WHEN fetching gaming company jobs THEN the system SHALL include roles for in-game chat moderators, community operations, and player support
3. WHEN gaming company jobs are found THEN the system SHALL categorize them under "gaming-platforms" and "chat-moderation" categories
4. WHEN gaming company jobs are displayed THEN the system SHALL specify which games or platforms the role supports

### Requirement 5

**User Story:** As a job seeker interested in AI and data work, I want to receive notifications from comprehensive AI training and data annotation platforms, so that I can find flexible microtask opportunities including search evaluation, content rating, and data labeling work.

#### Acceptance Criteria

1. WHEN the job scout runs THEN the system SHALL fetch jobs from specialized AI training platforms including Appen, TELUS International AI (formerly Lionbridge AI/RaterLabs), Scale AI, Surge AI, Outlier AI, Remotasks, Clickworker, OneForma, iSoftStone, and Microworkers
2. WHEN fetching AI training platform jobs THEN the system SHALL include roles for search engine evaluators, AI content raters, data annotators, linguistic specialists, prompt testers, transcribers, image/video labelers, and speech transcription specialists
3. WHEN AI training platform jobs are found THEN the system SHALL categorize them under "ai-training", "data-labeling", "search-evaluation", and "content-rating" categories
4. WHEN AI training platform jobs are displayed THEN the system SHALL indicate the flexible/microtask nature and specify the type of AI work (search evaluation, content rating, data annotation, etc.)
5. WHEN the job scout runs THEN the system SHALL fetch outsourced AI work from tech giants including Google (via TELUS, Appen, Lionbridge), Microsoft (via Appen, OneForma, TELUS), Amazon (MTurk, AWS AI labeling), Meta (via Accenture, Cognizant, TELUS), and OpenAI/Anthropic contractors
6. WHEN fetching freelance AI work THEN the system SHALL include opportunities from Upwork, Fiverr, Freelancer.com, and Toptal for AI training gigs, prompt engineering, and annotation projects

### Requirement 6

**User Story:** As a job seeker looking for specialized community management work, I want to receive notifications from companies that focus specifically on moderation and virtual assistance, so that I can find roles with companies that specialize in these services.

#### Acceptance Criteria

1. WHEN the job scout runs THEN the system SHALL fetch jobs from specialized companies including ModSquad, SupportNinja, Boldly, Time Etc, Belay Solutions, and CloudTask
2. WHEN fetching specialized company jobs THEN the system SHALL include roles for chat moderators, virtual assistants, social media managers, and customer engagement specialists
3. WHEN specialized company jobs are found THEN the system SHALL categorize them under "chat-moderation", "virtual-assistant", and "creator-platforms" categories
4. WHEN specialized company jobs are displayed THEN the system SHALL highlight the company's specialization in community management or virtual assistance

### Requirement 7

**User Story:** As a user of the job bot, I want the new specialized job sources to integrate seamlessly with the existing system, so that I receive all job notifications in the same format and can track the total number of jobs found.

#### Acceptance Criteria

1. WHEN new specialized job sources are added THEN the system SHALL maintain the existing job data structure with title, company, location, url, source, and salary fields
2. WHEN specialized jobs are fetched THEN the system SHALL increment the total job count and include these sources in the daily summary
3. WHEN specialized jobs are sent THEN the system SHALL use the same Telegram message format as existing job notifications
4. WHEN the job scout completes THEN the system SHALL report the number of jobs found from each new specialized source

### Requirement 8

**User Story:** As a job seeker, I want jobs to be organized by skill level and requirements, so that I can easily find opportunities that match my qualifications and experience level.

#### Acceptance Criteria

1. WHEN jobs are fetched THEN the system SHALL categorize them into entry-level, intermediate-level, expert-level, and flexible opportunity groups
2. WHEN displaying job categories THEN the system SHALL include skill requirements, salary ranges, and company examples for each category
3. WHEN jobs are sent to users THEN the system SHALL group similar jobs together and indicate the skill level required
4. WHEN users receive job notifications THEN the system SHALL provide clear categorization with entry-level jobs (no experience required), intermediate jobs (some experience/skills), expert jobs (advanced skills), and flexible opportunities (part-time/project-based)
5. WHEN organizing job categories THEN the system SHALL include specific requirements like "Basic computer skills" for entry-level, "1-2 years experience" for intermediate, and "Advanced technical skills" for expert level

### Requirement 9

**User Story:** As a job seeker, I want the system to handle errors gracefully when fetching from specialized sources, so that failures from one source don't prevent me from receiving jobs from other sources.

#### Acceptance Criteria

1. WHEN a specialized job source API fails THEN the system SHALL log the error and continue processing other sources
2. WHEN a specialized job source is temporarily unavailable THEN the system SHALL provide fallback job listings where possible
3. WHEN multiple specialized sources fail THEN the system SHALL still send notifications for successfully fetched jobs
4. WHEN all specialized sources fail THEN the system SHALL continue with existing job sources and log the failures