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
  - **Arslan:** Exercise hierarchy (Cardio, Strength, Flexibility) 

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
- **Aleksandr Zinovev:** User hierarchy implementation and management 
- **Siwoo Lee:** Staff hierarchy implementation and management 
- **Arslan Ahmet Berk:** Exercise hierarchy implementation and management 

## Contact

For questions about this project, contact any team member:
- **Aleksandr Zinovev** - User hierarchy lead ✅ **HW3 Complete**
- **Siwoo Lee** - Staff hierarchy lead ✅ **HW3 Complete**
- **Arslan Ahmet Berk** - Exercise hierarchy lead - *HW3 Pending*

---

*This repository contains all homework submissions and project materials for the Database Systems course.*
