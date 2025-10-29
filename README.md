# FitTrack Pro - Database Project

**Course:** Database Systems Project 2025  
**Team Members:** Aleksandr Zinovev, Siwoo Lee, Arslan Ahmet Berk

## Project Overview

FitTrack Pro is a comprehensive fitness tracker and gym management system that combines personal workout tracking with gym operations management. The system serves three types of users: individual fitness enthusiasts, gym members, and gym staff.

## Repository Structure

```
├── HW1_Fitness_Tracker_Solution.pdf   # Assignment 1: Service Description & ER Diagram
├── HW2_Mapping_Approach.pdf           # Assignment 2: Relational Mapping
├── HW3_sample_data_staff.sql          # Assignment 3: Staff hierarchy sample data (Lee)
├── HW3_staff_hierarchy_queries.sql    # Assignment 3: Staff hierarchy queries (Lee)
├── HW3_query_log_staff.txt           # Assignment 3: Staff query execution log (Lee)
├── HW3_sample_data_user.sql           # Assignment 3: User hierarchy sample data (Aleksandr)
├── HW3_user_hierarchy_queries.sql     # Assignment 3: User hierarchy queries (Aleksandr)
├── HW3_query_log_user.txt            # Assignment 3: User query execution log (Aleksandr)
├── HW3_sample_data_exercise.sql       # Assignment 3: Exercise hierarchy sample data (Arslan)
├── HW3_exercise_hierarchy_queries.sql # Assignment 3: Exercise hierarchy queries (Arslan)
├── HW3_query_log_exercise.txt        # Assignment 3: Exercise query execution log (Arslan)
├── HW4_Corporate_Design.md            # Assignment 4: Corporate Design documentation
├── public_html/                       # Assignment 4: Website implementation
│   ├── index.html                     # Homepage with CD implementation
│   ├── imprint.html                   # Legal information page
│   ├── style.css                      # CSS implementing Corporate Design
│   ├── HW4_Corporate_Design_Documentation.html  # CD documentation (HTML)
│   ├── HW4_Corporate_Design_Documentation.md    # CD documentation (Markdown)
│   ├── FitTrack Pro - Corporate Design Documentation.pdf  # CD documentation (PDF)
│   ├── documentation-style.css        # CSS for documentation
│   └── img/                          # Image assets
│       ├── fittrack-pro-logo.svg     # Brand logo
│       ├── logo-demo.html            # Logo demonstration
│       └── color-palette.html        # Color palette visualization
├── fittrack_cgi/                      # Assignments 5 & 6: CGI Web Application
│   ├── *.py                           # Python CGI scripts (12 total)
│   │   ├── add_user.py               # HW5: User insertion script
│   │   ├── add_gym.py                # HW5: Gym insertion script
│   │   ├── add_workout.py            # HW5: Workout insertion script
│   │   ├── add_exercise.py           # HW5: Exercise insertion script
│   │   ├── add_class.py              # HW5: Class insertion script
│   │   ├── add_progress.py           # HW5: Progress tracking script
│   │   ├── add_workout_exercise.py   # HW5: Workout-Exercise link script
│   │   ├── add_class_booking.py      # HW5: Class booking script
│   │   ├── add_gym_member.py         # HW5: Gym member script
│   │   ├── get_data.py               # HW5: AJAX data provider
│   │   ├── search_user_activity.py   # HW6: User activity search
│   │   └── user_detail.py            # HW6: User detail page
│   ├── forms/                         # HTML forms (12 total)
│   │   ├── add_*.html                # HW5: 9 data entry forms
│   │   ├── search_hub.html           # HW6: Search landing page
│   │   ├── search_user_activity.html # HW6: User activity search
│   │   └── search_gym_members.html   # HW6: Gym member search (in progress)
│   ├── css/                           # Corporate Design CSS
│   ├── img/                           # Brand assets
│   ├── index.html                     # Homepage
│   ├── maintenance.html               # Data management hub
│   ├── imprint.html                   # Legal page
│   ├── README.md                      # CGI implementation documentation
│   └── DEPLOYMENT_INSTRUCTIONS.md     # Complete deployment guide
├── HW6/                               # Assignment 6: Search Functionality
│   ├── HW6_Search_Implementation_Plan.md  # Search implementation plan
│   ├── generate_test_data.sql         # Test data generation script
│   └── add_workouts_for_existing_users.sql  # Additional workout data
├── fittrack_schema.sql                # Assignment 2: Database schema implementation
├── FitTrack Pro - ER Diagram.pdf     # Visual ER Diagram
└── README.md                          # This file
```

## Assignments Location

### 📋 Assignment 1 - Service Description & ER Diagram
- **File:** `HW1_Fitness_Tracker_Solution.pdf`
- **Content:** Project overview, functionality description, ER diagram with ISA hierarchies

### 📋 Assignment 2 - Relational Mapping
- **Files:** 
  - `HW2_Mapping_Approach.pdf` - Mapping approach documentation
  - `fittrack_schema.sql` - Complete SQL schema implementation
- **Content:** Conversion of ER diagram to relational schema with full SQL implementation

### 📋 Assignment 3 - Database Implementation
- **Content:** Database implementation with sample data and queries for each ISA hierarchy
- **Work Division:**
  - **Aleksandr:** User hierarchy (Individual Users, Gym Members, Staff) ✅ **COMPLETED**
  - **Lee:** Staff hierarchy (Trainers, Managers, Receptionists) ✅ **COMPLETED**
  - **Arslan:** Exercise hierarchy (Cardio, Strength, Flexibility) ✅ **COMPLETED**

#### Staff Hierarchy (Lee) ✅
- **Files:** 
  - `HW3_sample_data_staff.sql` - Sample data for Staff hierarchy
  - `HW3_staff_hierarchy_queries.sql` - 3 queries for Staff hierarchy
  - `HW3_query_log_staff.txt` - Query execution results and logs

#### User Hierarchy (Aleksandr) ✅
- **Files:** 
  - `HW3_sample_data_user.sql` - Sample data for User hierarchy
  - `HW3_user_hierarchy_queries.sql` - 3 queries for User hierarchy
  - `HW3_query_log_user.txt` - Query execution results and logs

#### Exercise Hierarchy (Arslan) ✅
- **Files:** 
  - `HW3_sample_data_exercise.sql` - Sample data for Exercise hierarchy
  - `HW3_exercise_hierarchy_queries.sql` - 3 queries for Exercise hierarchy
  - `HW3_query_log_exercise.txt` - Query execution results and logs

### 📋 Assignment 4 - Website Implementation ✅
- **Content:** Corporate Design development and website implementation
- **Lead:** Aleksandr Zinovev
- **Files:**
  - `HW4_Corporate_Design.md` - Corporate Design specification document
  - `public_html/` - Complete website implementation
    - `index.html` - Homepage with CD implementation and placeholders
    - `imprint.html` - Legal information page with required German disclaimer
    - `style.css` - CSS file implementing Corporate Design (no inline styles)
    - `HW4_Corporate_Design_Documentation.html` - Visual CD documentation with colors and logo
    - `HW4_Corporate_Design_Documentation.md` - Markdown source for documentation
    - `FitTrack Pro - Corporate Design Documentation.pdf` - PDF deliverable
    - `documentation-style.css` - Standalone CSS for documentation
    - `img/fittrack-pro-logo.svg` - Brand logo in SVG format
    - `img/logo-demo.html` - Interactive logo demonstration
    - `img/color-palette.html` - Visual color palette with hex codes

### 📋 Assignment 5 - Web Application with Database Integration ✅
- **Team Collaboration:** All members contributing forms
- **Technology Stack:** Python CGI + PyMySQL + MariaDB + Corporate Design CSS
- **Location:** `fittrack_cgi/` directory

#### CGI Implementation
- **Technology:** Python 3.6+ CGI scripts with PyMySQL
- **Features:**
  - Direct database connection to MariaDB on clabsql server
  - Works without admin privileges or mod_wsgi
  - All 9 forms insert data into database
  - Dynamic feedback pages
  - AJAX data loading for dropdowns
  - Deployed on ClamV server
- **Files:**
  - `*.py` - 9 executable Python CGI scripts (in root directory)
  - `forms/` - 9 HTML forms with database integration
  - `get_data.py` - AJAX endpoint for dynamic dropdowns
  - `README.md` - CGI implementation documentation
  - `DEPLOYMENT_INSTRUCTIONS.md` - Complete deployment guide

#### Work Distribution:
- **Aleksandr Zinovev:** User forms, Progress Tracking, Workout-Exercise relationships
- **Siwoo Lee:** Gym forms, Class forms, Class booking relationships  
- **Arslan Ahmet Berk:** Exercise forms, Workout forms, Gym member relationships

### 📋 Assignment 6 - Search Functionality 🚧 IN PROGRESS
- **Team Collaboration:** Each member implements one search feature
- **Technology Stack:** Python CGI + PyMySQL + MariaDB
- **Location:** `fittrack_cgi/` directory + `HW6/` for documentation

#### Search Features
1. **User Activity Analysis** (Aleksandr) ✅ **COMPLETED**
   - Search by user type, date range, activity metrics
   - Results page with user groups and statistics
   - Individual user detail pages with workout history
   
2. **Gym Member Management** (Lee) 🚧 **IN PROGRESS**
   - Search by gym, membership type, status
   - Member listing with gym information
   
3. **Exercise Performance** (Arslan) 📋 **PLANNED**
   - Search by exercise type, performance metrics
   - Session frequency analysis

#### Files:
- `search_user_activity.py` - User activity search CGI (Aleksandr) ✅
- `user_detail.py` - User detail page CGI (Aleksandr) ✅
- `forms/search_hub.html` - Search landing page ✅
- `forms/search_user_activity.html` - User activity search form ✅
- `forms/search_gym_members.html` - Gym member search form 🚧
- `HW6/HW6_Search_Implementation_Plan.md` - Implementation plan ✅
- `HW6/*.sql` - Test data generation scripts ✅

## System Features

### Core Functionality
- **Personal Fitness Tracking:** Workout logging, progress monitoring, goal setting
- **Gym Management:** Member management, class scheduling, equipment tracking
- **User Types:** Individual users, gym members, staff (trainers, managers, receptionists)

### Database Design Highlights
- **3 ISA Hierarchies:** Users, Staff, Exercises
- **Normalized Schema:** Efficient data storage and retrieval
- **Comprehensive Relationships:** 1:N and M:N relationships properly implemented


**View ER Diagram:**
  Open `FitTrack Pro - ER Diagram.pdf`

## Team Collaboration

### GitHub Repository
- **Main Repository:** [db-fitness-tracker](https://github.com/bremenq/db-fitness-tracker)

### Work Distribution
Based on the 3 ISA hierarchies in our database design:
- **Aleksandr Zinovev:** User hierarchy implementation and management ✅ **COMPLETED**
- **Siwoo Lee:** Staff hierarchy implementation and management ✅ **COMPLETED**
- **Arslan Ahmet Berk:** Exercise hierarchy implementation and management ✅ **COMPLETED** 

### Assignment Progress
- **Assignment 1:** Service Description & ER Diagram ✅ **COMPLETED**
- **Assignment 2:** Relational Mapping ✅ **COMPLETED**
- **Assignment 3:** Database Implementation ✅ **COMPLETED**
- **Assignment 4:** Website Implementation ✅ **COMPLETED**
- **Assignment 5:** CGI Web Application ✅ **COMPLETED**
- **Assignment 6:** Search Functionality 🚧 **IN PROGRESS** (Aleksandr's part complete)

## Contact

For questions about this project, contact any team member:
- **Aleksandr Zinovev** - User hierarchy lead | Website implementation
- **Siwoo Lee** - Staff hierarchy lead
- **Arslan Ahmet Berk** - Exercise hierarchy lead

---

*This repository contains all homework submissions and project materials for the Database Systems course.*
