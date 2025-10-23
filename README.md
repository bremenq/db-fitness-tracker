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
├── fittrack_app/                      # Assignment 5: Flask Web Application
│   ├── app.py                         # Main Flask application with all 9 routes
│   ├── config.py                      # Database configuration
│   ├── requirements.txt               # Python dependencies
│   ├── README.md                      # Flask app documentation
│   ├── static/                        # Static assets
│   │   ├── css/style.css             # Corporate Design CSS
│   │   └── img/fittrack-pro-logo.svg # Brand logo
│   └── templates/                     # Jinja2 templates
│       ├── base.html                  # Base template with navigation
│       ├── index.html                 # Homepage (Flask version)
│       ├── imprint.html               # Legal page (Flask version)
│       ├── maintenance.html           # Data management hub
│       ├── 404.html                   # Error page
│       ├── entities/                  # Entity forms (6 forms + feedback)
│       └── relationships/             # Relationship forms (3 forms + feedback)
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

#### Assignment 4 Requirements Fulfilled:
✅ **Corporate Design Development** - Complete brand identity with logo, colors, typography  
✅ **Homepage Implementation** - Feature overview with CD styling and placeholders  
✅ **Imprint Page** - Contact information and required German legal disclaimer  
✅ **CSS-Only Layout** - No inline styles in HTML, all styling in separate CSS file  
✅ **Image Organization** - All images in separate `img/` directory  
✅ **PDF Documentation** - Complete Corporate Design specification document  
✅ **Website URL** - `http://clabsql.clamv.constructor.university/~azinovev/public_html/` (ready for deployment)  
✅ **Legal Compliance** - GDPR statement and German jurisdiction disclaimer  
✅ **Responsive Design** - Mobile-friendly layout with proper accessibility

### 📋 Assignment 5 - Flask Web Application ✅
- **Content:** Web frontend to database services with data entry forms
- **Team Collaboration:** All members contributing forms
- **Technology Stack:** Python Flask + MariaDB + Corporate Design CSS
- **Files:**
  - `fittrack_app/` - Complete Flask web application
    - `app.py` - Main Flask application with all 9 routes and database logic
    - `config.py` - Database configuration for MariaDB connection
    - `requirements.txt` - Python dependencies (Flask, SQLAlchemy, PyMySQL)
    - `templates/` - Jinja2 templates with Corporate Design integration
    - `static/` - CSS and images from Assignment 4

#### Assignment 5 Requirements Fulfilled:
✅ **9 Data Entry Forms** - Complete CRUD operations for all entities and relationships  
✅ **Entity Forms (6)** - User, Gym, Class, Exercise, Workout, Progress Tracking  
✅ **Relationship Forms (3)** - Workout-Exercise links, Class bookings, Gym memberships  
✅ **POST Method Usage** - All forms use POST for data submission (security best practice)  
✅ **Auto-generated IDs** - Primary keys generated server-side, not user input  
✅ **Meaningful Dropdowns** - Foreign key selectors show names, not IDs  
✅ **Corporate Design Integration** - Consistent styling with Assignment 4  
✅ **Database Schema Compatibility** - Forms match HW2/HW3 database structure  
✅ **Error Handling** - Success/error feedback pages for all forms  
✅ **Professional Navigation** - Integrated with existing website structure

#### Work Distribution:
- **Aleksandr Zinovev:** User forms, Progress Tracking, Workout-Exercise relationships, Flask setup
- **Siwoo Lee:** Gym forms, Class forms, Class booking relationships  
- **Arslan Ahmet Berk:** Exercise forms, Workout forms, Workout-Exercise relationships

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
- **Assignment 5:** Flask Web Application ✅ **COMPLETED**

## Contact

For questions about this project, contact any team member:
- **Aleksandr Zinovev** - User hierarchy lead | Website implementation ✅ **HW3 & HW4 Complete**
- **Siwoo Lee** - Staff hierarchy lead ✅ **HW3 Complete**
- **Arslan Ahmet Berk** - Exercise hierarchy lead ✅ **HW3 Complete**

---

*This repository contains all homework submissions and project materials for the Database Systems course.*
