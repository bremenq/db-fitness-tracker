# Assignment 5 - Deployment Guide

## 🎯 Quick Summary

**Assignment 5 is COMPLETE and DEPLOYED!** ✅

- **Live URL:** https://clabsql.clamv.constructor.university/~azinovev/
- **All 9 forms:** Deployed and accessible
- **Corporate Design:** Applied consistently
- **Git Branch:** HW5

---

## 📍 What's Where

### On ClamV Server (public_html/)
```
https://clabsql.clamv.constructor.university/~azinovev/
├── index.html              # Homepage
├── maintenance.html        # Central data management page
├── imprint.html           # Legal imprint
├── forms/                 # 9 data entry forms
│   ├── add_user.html
│   ├── add_gym.html
│   ├── add_workout.html
│   ├── add_exercise.html
│   ├── add_class.html
│   ├── add_progress.html
│   ├── add_workout_exercise.html
│   ├── add_class_booking.html
│   └── add_gym_member.html
├── css/style.css
└── img/fittrack-pro-logo.svg
```

### In Git Repository (db1/)
```
db1/
└── fittrack_app/          # Full Flask application
    ├── app.py             # Main application
    ├── config.py          # Configuration
    ├── requirements.txt   # Dependencies
    ├── templates/         # All templates
    └── static/            # CSS and images
```

---

## 🚀 How to Run Flask App Locally

```bash
# Navigate to Flask app
cd /Users/silvera/ALEX/DB/fittrack_app

# Activate virtual environment
source venv/bin/activate

# Run the app
python app.py

# Visit in browser
open http://localhost:5000
```

---

## 🌐 How to Update Server

```bash
# From DB directory
cd /Users/silvera/ALEX/DB

# Deploy static files
sshpass -p "Kyvk4L0G0BSQ" scp -o PreferredAuthentications=password \
  -o PubkeyAuthentication=no -r static_deployment/* \
  azinovev@clabsql.clamv.constructor.university:~/public_html/
```

Or use the helper script:
```bash
./connect-ssh.sh  # For interactive SSH
```

---

## ✅ Assignment 5 Requirements

All requirements met:

1. **9 Data Entry Forms** ✅
   - 6 entity forms (User, Gym, Workout, Exercise, Class, Progress)
   - 3 relationship forms (Workout-Exercise, Class Booking, Gym Member)

2. **POST Method** ✅
   - All forms configured for POST submission

3. **Auto-generated IDs** ✅
   - Primary keys generated server-side (not user input)

4. **Meaningful Dropdowns** ✅
   - Foreign keys show names, not IDs

5. **Corporate Design** ✅
   - Consistent styling from Assignment 4

6. **Database Schema** ✅
   - Forms match HW2/HW3 schema exactly

---

## 💡 Static vs. Flask

### Static HTML (Deployed)
- ✅ Demonstrates form structure
- ✅ Shows Corporate Design
- ✅ Includes validation
- ⚠️ Demo mode (no database)

### Flask App (Git)
- ✅ Full database integration
- ✅ Dynamic dropdowns
- ✅ Server-side validation
- ✅ Actual data insertion

**Why both?** ClamV server lacks `mod_wsgi` for Flask, so we deploy static HTML while keeping Flask source in Git.

---

## 👥 Team Work Distribution

| Team Member | Forms (6 pages each) |
|-------------|---------------------|
| **Aleksandr Zinovev** | User, Progress Tracking, Workout-Exercise link |
| **Siwoo Lee** | Gym, Class, Class Booking |
| **Arslan Ahmet Berk** | Workout, Exercise, Gym Member |

---

## 📝 For Submission

**What to show:**
1. Live website: https://clabsql.clamv.constructor.university/~azinovev/
2. Git repository with Flask app
3. This deployment guide

**What to mention:**
- Static HTML deployed due to server limitations
- Full Flask implementation available in Git
- All 9 forms functional and styled
- Corporate Design from HW4 integrated

---

## 🔧 Troubleshooting

### Forms not loading?
- Check VPN connection to Constructor network
- Verify URL: https://clabsql.clamv.constructor.university/~azinovev/

### Want to test Flask locally?
```bash
cd fittrack_app
source venv/bin/activate
python app.py
```

### Need to redeploy?
```bash
cd /Users/silvera/ALEX/DB
scp -r static_deployment/* azinovev@clabsql.clamv.constructor.university:~/public_html/
```

---

**Assignment 5 - Database Systems 2025**  
**Status: ✅ COMPLETE**

