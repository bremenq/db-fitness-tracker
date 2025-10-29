Executing command on clabsql.clamv.constructor.university: 
cat ~/public_html/README.md

# FitTrack Pro - Static HTML Deployment

This directory contains the static HTML version of the FitTrack Pro web application for Assignment 5.

## 📁 Structure

```
static_deployment/
├── index.html              # Homepage (from HW4)
├── imprint.html            # Legal imprint (from HW4)
├── maintenance.html        # Central data management page
├── css/
│   └── style.css          # Corporate Design styles (from HW4)
├── img/
│   └── fittrack-pro-logo.svg
└── forms/                  # 9 data entry forms
    ├── add_user.html
    ├── add_gym.html
    ├── add_workout.html
    ├── add_exercise.html
    ├── add_class.html
    ├── add_progress.html
    ├── add_workout_exercise.html
    ├── add_class_booking.html
    └── add_gym_member.html
```

## 🎯 Assignment 5 Requirements

✅ **9 Data Entry Forms** - All forms included
✅ **POST Method** - All forms configured for POST
✅ **Corporate Design** - Consistent styling from HW4
✅ **Navigation** - Integrated with existing website
✅ **Form Validation** - HTML5 client-side validation

## 🚀 Deployment

### To ClamV Server:

```bash
# From the DB directory
cd /Users/silvera/ALEX/DB
scp -r static_deployment/* username@clabsql.clamv.constructor.university:~/public_html/
```

### Local Testing:

```bash
# Simple HTTP server
cd static_deployment
python3 -m http.server 8000
# Visit: http://localhost:8000
```

## 💡 Demo Mode

The static HTML forms include a JavaScript demo handler that shows an alert when forms are submitted. This demonstrates the form structure and validation without requiring a backend.

**For full functionality with database integration**, run the Flask application:

```bash
cd ../fittrack_app
source venv/bin/activate
python app.py
# Visit: http://localhost:5000
```

## 📝 Notes

- **Static vs. Flask**: This static version is for demonstration and meets assignment requirements
- **Database**: The Flask app version connects to MariaDB and performs actual database operations
- **Dropdowns**: Static forms show demo data; Flask app loads real data from the database
- **Validation**: Both versions include client-side validation; Flask adds server-side validation

## 👥 Team

- **Aleksandr Zinovev** - User & Progress Tracking forms
- **Siwoo Lee** - Gym & Class management forms  
- **Arslan Ahmet Berk** - Workout & Exercise forms

---

**Assignment 5 - Database Systems Course 2025**

