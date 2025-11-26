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
├── fittrack_cgi/                      # Assignments 5, 6, 7, 9: CGI Web Application
│   ├── *.py                           # Python CGI scripts (13 total)
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
│   │   ├── autocomplete.py           # HW9: Dynamic autocomplete API
│   │   ├── get_client_info.py        # HW10: Client IP detection API
│   │   ├── geolocation.py            # HW10: IP geolocation lookup API
│   │   ├── search_user_activity.py   # HW6: User activity search (Aleksandr)
│   │   ├── user_detail.py            # HW6: User detail page (Aleksandr)
│   │   ├── search_gym_members.py     # HW6: Gym member search (Lee)
│   │   ├── member_detail.py          # HW6: Member detail page (Lee)
│   │   ├── search_exercise_performance.py  # HW6: Exercise search (Arslan)
│   │   └── exercise_detail.py        # HW6: Exercise detail page (Arslan)
│   ├── forms/                         # HTML forms (13 total)
│   │   ├── add_user.html             # HW5: User form (no autocomplete)
│   │   ├── add_gym.html              # HW5: Gym form (no autocomplete)
│   │   ├── add_exercise.html         # HW5: Exercise form (no autocomplete)
│   │   ├── add_workout.html          # HW5+HW9: Workout with user autocomplete
│   │   ├── add_class.html            # HW5+HW9: Class with gym autocomplete
│   │   ├── add_progress.html         # HW5+HW9: Progress with user autocomplete
│   │   ├── add_workout_exercise.html # HW5+HW9: Link with workout/exercise autocomplete
│   │   ├── add_class_booking.html    # HW5+HW9: Booking with user/class autocomplete
│   │   ├── add_gym_member.html       # HW5+HW9: Member with user/gym autocomplete
│   │   ├── search_hub.html           # HW6: Search landing page
│   │   ├── search_user_activity.html # HW6: User activity search (Aleksandr)
│   │   ├── search_gym_members.html   # HW6: Gym member search (Lee)
│   │   └── search_exercise_performance.html  # HW6: Exercise search (Arslan)
│   │   ├── location_map.html         # HW10: Full-page geolocation map
│   │   └── location_widget.html      # HW10: Embeddable map widget
│   ├── css/                           # Corporate Design CSS
│   │   └── map-styles.css            # HW10: Custom styles for map
│   ├── js/                            # JavaScript modules
│   │   └── map_functionality.js      # HW10: Leaflet map implementation
│   ├── img/                           # Brand assets
│   ├── index.html                     # Homepage (updated for HW10)
│   ├── maintenance.html               # Data management hub
│   ├── imprint.html                   # Legal page
│   ├── README.md                      # CGI implementation documentation
│   └── DEPLOYMENT_INSTRUCTIONS.md     # Complete deployment guide
├── HW6/                               # Assignment 6: Search Functionality
│   ├── HW6_Search_Implementation_Plan.md  # Search implementation plan
│   ├── generate_test_data.sql         # Test data generation script
│   └── add_workouts_for_existing_users.sql  # Additional workout data
├── HW7/                               # Assignment 7: Security
│   ├── security_ii_schema.sql         # Authentication database schema
│   └── SECURITY_II_IMPLEMENTATION.md  # Authentication documentation
├── HW8/                               # Assignment 8: Web Log Evaluation
│   ├── analyze_logs.py                # Apache log analysis script
│   ├── web_log_summary.txt            # Text statistics output
│   ├── access_timeline.png            # Access timeline diagram
│   ├── browser_distribution.png       # Browser distribution chart
│   ├── HW8 - Web Log Analysis Report.pdf        # Comprehensive PDF report
│   ├── HW8 - Web Log Analysis Summary.pdf       # Summary PDF report
│   ├── HW8_Web_Log_Analysis_Report.html         # HTML source (comprehensive)
│   └── HW8_Summary_Report.html                  # HTML source (summary)
├── HW9/                               # Assignment 9: jQuery UI Autocomplete
│   ├── add_workout.html               # Autocomplete for user selection (Aleksandr)
│   ├── add_class.html                 # Autocomplete for gym selection (Aleksandr)
│   ├── add_workout_exercise.html      # Autocomplete for workout/exercise (Siwoo)
│   ├── add_gym_member.html            # Autocomplete for user/gym (Arslan)
│   ├── add_class_booking.html         # Autocomplete for user/class (Arslan)
│   ├── add_progress.html              # Autocomplete for user selection (Siwoo)
│   └── autocomplete.py                # Backend API for dynamic search
├── HW10/                              # Assignment 10: Linked Services
│   └── HW10_IP_Geolocation_Implementation_Plan.md # Implementation plan
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
  - jQuery UI autocomplete for foreign key selections (HW9)
  - Deployed on ClamV server
- **Files:**
  - `*.py` - 13 executable Python CGI scripts (in root directory)
  - `forms/` - 9 HTML forms with database integration and autocomplete
  - `get_data.py` - AJAX endpoint for dynamic dropdowns
  - `autocomplete.py` - Dynamic autocomplete API (HW9)
  - `README.md` - CGI implementation documentation
  - `DEPLOYMENT_INSTRUCTIONS.md` - Complete deployment guide

#### Work Distribution:
- **Aleksandr Zinovev:** User forms, Progress Tracking, Workout-Exercise relationships
- **Siwoo Lee:** Gym forms, Class forms, Class booking relationships  
- **Arslan Ahmet Berk:** Exercise forms, Workout forms, Gym member relationships

### ✅ Assignment 6 - Search Functionality **COMPLETED**
- **Team Collaboration:** Each member implements one search feature
- **Technology Stack:** Python CGI + PyMySQL + MariaDB
- **Location:** `fittrack_cgi/` directory + `HW6/` for documentation

#### Search Features (All Completed!)
1. **User Activity Analysis** (Aleksandr) ✅ **COMPLETED**
   - Search by user type, date range, activity metrics
   - Results page with user groups and statistics
   - Individual user detail pages with workout history
   
2. **Gym Member Management** (Lee) ✅ **COMPLETED**
   - Search by membership type, status, date range
   - Member listing with membership details
   - Individual member detail pages with workouts and bookings
   
3. **Exercise Performance** (Arslan) ✅ **COMPLETED**
   - Search by category, difficulty, muscle groups
   - Performance statistics and popularity metrics
   - Exercise detail pages with top performers

#### Files:
- `search_user_activity.py` + `user_detail.py` - User search (Aleksandr) ✅
- `search_gym_members.py` + `member_detail.py` - Gym member search (Lee) ✅
- `search_exercise_performance.py` + `exercise_detail.py` - Exercise search (Arslan) ✅
- `forms/search_hub.html` - Search landing page ✅
- `forms/search_*.html` - All 3 search forms ✅
- `HW6/HW6_Search_Implementation_Plan.md` - Implementation plan ✅
- `HW6/add_gym_members.sql` - Test data generation ✅

### ✅ Assignment 7 - Security II: Web Authentication **COMPLETED**
- **Web service authentication and access control**
- **Location:** `HW7/` directory + `fittrack_cgi/` authentication files

#### Implementation Details
- **Database Schema:** `HW7/security_ii_schema.sql` - admin_user table
- **Authentication Module:** `fittrack_cgi/auth_utils.py` - Session management
- **Login System:** `fittrack_cgi/login.html` + `login.py` + `logout.py`
- **Protected Pages:** All 9 add_*.py scripts require authentication
- **Public Pages:** All search_*.py scripts remain accessible
- **Documentation:** `HW7/SECURITY_II_IMPLEMENTATION.md`
- **Default Credentials:** Username: `admin`, Password: `fittrack2025`

#### Technical Details:
- **Authentication:** Session-based with SHA2-256 password hashing
- **Session Storage:** File-based in `/tmp/fittrack_sessions/`
- **Session Duration:** 30 minutes
- **Access Control:** Write operations (INSERT/UPDATE/DELETE) protected, read operations (SELECT) public
- **Error Handling:** 401 Unauthorized with user-friendly error pages
- **Security Features:** HttpOnly cookies, secure tokens, SQL injection prevention

### ✅ Assignment 8 - Web Log Evaluation **COMPLETED**
- **Apache log analysis with statistics and timeline diagrams**
- **Location:** `HW8/` directory
- **Analysis Period:** November 1-12, 2025

#### Implementation Details
- **Analysis Script:** `HW8/analyze_logs.py` - Python script with matplotlib
- **Technology Stack:** Python 3.6, matplotlib, regex for log parsing
- **Data Source:** Real Apache logs from ClamV server (`/var/log/apache2/`)
- **Reports:** 
  - Comprehensive PDF report (9 sections with detailed analysis)
  - Summary PDF report (text-based with diagrams)
- **Diagrams:**
  - Access timeline (hourly request distribution)
  - Browser distribution pie chart

#### Key Findings:
- **Total Requests:** 77 page requests analyzed
- **Unique Visitors:** 2 IPs (internal university network)
- **Analysis Period:** November 1-12, 2025 (12 days)
- **Error Rate:** 0% - Zero errors found (clean deployment!)
- **Browser Distribution:** Firefox 96.1%, Safari 3.9%
- **Most Popular Page:** maintenance.html (21 requests, 27.3%)
- **Peak Activity:** November 6, 2025 (13:00-18:00)

#### Technical Features:
- **User-Specific Filtering:** Only analyzes pages for `/~azinovev/` and `/cgi-bin/azinovev/`
- **Timeline Visualization:** Hourly request aggregation with matplotlib
- **Browser Detection:** Automatic user agent parsing and categorization
- **Error Analysis:** Comprehensive error log parsing (zero errors found)
- **Statistics Generation:** Detailed text reports with page rankings and visitor analysis

#### Files:
- `analyze_logs.py` - Enhanced Python analysis script ✅
- `web_log_summary.txt` - Complete text statistics ✅
- `access_timeline.png` - Timeline diagram ✅
- `browser_distribution.png` - Browser pie chart ✅
- `HW8 - Web Log Analysis Report.pdf` - Comprehensive report (9 sections) ✅
- `HW8 - Web Log Analysis Summary.pdf` - Summary report with diagrams ✅

### ✅ Assignment 9 - jQuery UI Autocomplete **COMPLETED**
- **Dynamic search with server-side autocomplete (bonus feature included)**
- **Location:** `HW9/` directory + `fittrack_cgi/` updated forms
- **Technology Stack:** jQuery UI + Python CGI + AJAX + JSON

#### Implementation Details
- **Backend API:** `autocomplete.py` - Dynamic server-side search endpoint
- **Frontend:** jQuery UI autocomplete replacing all dropdown `<select>` elements
- **Search Types:** Users, Gyms, Exercises, Workouts, Classes
- **Features:**
  - Real-time search on each keystroke (minLength: 2)
  - SQL `LIKE` queries for partial matching
  - JSON responses with id, value, and label
  - Limit 10 results per search
  - Hidden field pattern for form submission
- **Forms Updated:**
  - All 6 forms with foreign key selections
  - Corporate Design CSS maintained
  - Fully integrated with existing form handlers

#### Work Distribution:
- **Aleksandr Zinovev:** Backend API (autocomplete.py) + User/Gym forms ✅
- **Siwoo Lee:** Workout/Exercise forms + Progress form ✅
- **Arslan Ahmet Berk:** Gym Member + Class Booking forms ✅

#### Technical Features:
- **Backend:** Python CGI with PyMySQL, SQL LIKE queries
- **Frontend:** jQuery UI 1.13.2, AJAX requests
- **Response Format:** `[{"id": 1, "value": "Name", "label": "Name (Details)"}]`
- **Search Fields:** Multiple fields per entity (name, email, address, etc.)
- **Performance:** Results limited to 10, indexed database queries

#### Files:
- `HW9/autocomplete.py` - Backend API for all search types ✅
- `HW9/add_workout.html` - User autocomplete (Aleksandr) ✅
- `HW9/add_class.html` - Gym autocomplete (Aleksandr) ✅
- `HW9/add_workout_exercise.html` - Workout/Exercise autocomplete (Siwoo) ✅
- `HW9/add_progress.html` - User autocomplete (Siwoo) ✅
- `HW9/add_gym_member.html` - User/Gym autocomplete (Arslan) ✅
- `HW9/add_class_booking.html` - User/Class autocomplete (Arslan) ✅
- `fittrack_cgi/autocomplete.py` - Deployed backend API ✅
- `fittrack_cgi/forms/add_*.html` - All forms updated with autocomplete ✅

### ✅ Assignment 10 - Linked Services: IP Geolocation **COMPLETED**
- **IP-based geolocation with interactive map display**
- **Location:** `HW10/` directory + `fittrack_cgi/` new files
- **Technology Stack:** Leaflet.js + OpenStreetMap + ipinfo.io API

#### Implementation Details
- **Backend APIs:**
  - `get_client_info.py` - Extracts client IP from HTTP headers
  - `geolocation.py` - Fetches coordinates from ipinfo.io API
- **Frontend Map:**
  - `location_map.html` - Full-page interactive map
  - `location_widget.html` - Embeddable map widget on the homepage
  - `map_functionality.js` - Dynamic map logic with AJAX
- **Features:**
  - Real-time IP detection and geolocation
  - Interactive map centered on user's location
  - Marker with IP address popup
  - Fallback to default coordinates (Constructor University) for local/private IPs
  - Responsive design for mobile and desktop

#### Work Distribution:
- **Aleksandr Zinovev:** Backend APIs (`get_client_info.py`, `geolocation.py`) ✅
- **Siwoo Lee:** Frontend map page and JavaScript logic (`location_map.html`, `map_functionality.js`) ✅
- **Arslan Ahmet Berk:** Landing page integration and testing (`index.html`, `location_widget.html`) ✅

#### Files:
- `HW10/HW10_IP_Geolocation_Implementation_Plan.md` - Implementation plan ✅
- `fittrack_cgi/get_client_info.py` - IP detection API ✅
- `fittrack_cgi/geolocation.py` - Geolocation API ✅
- `fittrack_cgi/forms/location_map.html` - Full map page ✅
- `fittrack_cgi/forms/location_widget.html` - Embeddable widget ✅
- `fittrack_cgi/js/map_functionality.js` - Map JavaScript logic ✅
- `fittrack_cgi/css/map-styles.css` - Custom map styles ✅
- `fittrack_cgi/index.html` - Homepage updated with map widget ✅

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
- **Assignment 6:** Search Functionality ✅ **COMPLETED** (All 3 searches implemented)
- **Assignment 7:** Security II - Web Authentication ✅ **COMPLETED**
- **Assignment 8:** Web Log Evaluation ✅ **COMPLETED** (77 requests, 0 errors)
- **Assignment 9:** jQuery UI Autocomplete ✅ **COMPLETED** (Bonus feature included)
- **Assignment 10:** Linked Services - IP Geolocation ✅ **COMPLETED**

## Contact

For questions about this project, contact any team member:
- **Aleksandr Zinovev** - User hierarchy lead | Website implementation
- **Siwoo Lee** - Staff hierarchy lead
- **Arslan Ahmet Berk** - Exercise hierarchy lead

---

*This repository contains all homework submissions and project materials for the Database Systems course.*
