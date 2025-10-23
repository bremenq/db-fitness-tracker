# FitTrack Pro - CGI Deployment

## 🎯 What is This?

This is a **working version** of FitTrack Pro that uses Python CGI scripts to actually insert data into the MariaDB database on the server.

Unlike the static HTML version, these forms **really work** and connect to the database!

---

## 📁 Structure

```
cgi_deployment/
├── index.html              # Homepage
├── maintenance.html        # Central management page
├── imprint.html           # Legal page
├── cgi-bin/               # Python CGI scripts (9 total)
│   ├── add_user.cgi
│   ├── add_gym.cgi
│   ├── add_workout.cgi
│   ├── add_exercise.cgi
│   ├── add_class.cgi
│   ├── add_progress.cgi
│   ├── add_workout_exercise.cgi
│   ├── add_class_booking.cgi
│   └── add_gym_member.cgi
├── forms/                 # HTML forms (point to CGI scripts)
│   ├── add_user.html
│   └── ... (9 total)
├── css/
│   └── style.css
└── img/
    └── fittrack-pro-logo.svg
```

---

## 🚀 How to Deploy to Server

### 1. Upload to Server

```bash
cd /Users/silvera/ALEX/DB
scp -r cgi_deployment/* azinovev@clabsql.clamv.constructor.university:~/public_html/
```

### 2. Make CGI Scripts Executable

```bash
ssh azinovev@clabsql.clamv.constructor.university
chmod +x ~/public_html/cgi-bin/*.cgi
```

### 3. Test

Visit: `http://10.60.36.1/~azinovev/maintenance.html`

---

## 🧪 How to Test Locally

### Option 1: Python HTTP Server with CGI

```bash
cd cgi_deployment
python3 -m http.server --cgi 8000
```

Visit: `http://localhost:8000/maintenance.html`

**Note:** CGI scripts will try to connect to the remote database.

### Option 2: Test Individual CGI Script

```bash
cd cgi_deployment/cgi-bin
python3 add_user.cgi
```

---

## 💾 Database Connection

All CGI scripts connect to:
- **Host:** `clabsql.clamv.constructor.university`
- **Database:** `db_azinovev`
- **User:** `azinovev`
- **Password:** (embedded in scripts)

---

## ✅ What Works

1. ✅ **All 9 forms** actually insert data into MariaDB
2. ✅ **Auto-increment IDs** work (server-generated)
3. ✅ **Foreign key validation** enforced by database
4. ✅ **Success/error feedback** pages
5. ✅ **Corporate Design** styling applied

---

## ⚠️ Limitations

1. **Slow:** CGI starts Python on every request (not like Flask which stays running)
2. **No dropdowns:** Forms don't load existing data for dropdowns (would need separate CGI scripts)
3. **Basic validation:** Only HTML5 client-side validation
4. **No sessions:** Each request is independent

---

## 🔄 CGI vs Flask vs Static

| Feature | Static HTML | CGI (This) | Flask |
|---------|------------|------------|-------|
| Database inserts | ❌ | ✅ | ✅ |
| Speed | ⚡ Fast | 🐌 Slow | ⚡ Fast |
| Dynamic dropdowns | ❌ | ⚠️ Possible | ✅ |
| Server requirements | None | Python + PyMySQL | mod_wsgi |
| Admin needed | ❌ | ❌ | ✅ |

---

## 📝 How CGI Works

```
1. User fills form
   ↓
2. Form submits to /cgi-bin/add_user.cgi
   ↓
3. Apache runs Python script
   ↓
4. Script connects to database
   ↓
5. Script inserts data
   ↓
6. Script prints HTML response
   ↓
7. User sees success/error page
```

---

## 🛠️ Dependencies

CGI scripts require:
- Python 3.6+
- PyMySQL library

Install on server:
```bash
pip3 install --user pymysql
```

---

## 📊 Assignment 5 Compliance

✅ **9 Data Entry Forms** - All working with database
✅ **POST Method** - All forms use POST
✅ **Auto-generated IDs** - Server-side generation
✅ **Database Integration** - Real MariaDB connection
✅ **Error Handling** - Try/catch with feedback
✅ **Corporate Design** - Consistent styling

---

## 🎓 For Submission

**Show this version if:**
- Professor wants working database on server
- You want to demonstrate real data insertion
- You have time to deploy and test

**Use Flask version if:**
- You want modern, fast implementation
- You can demo locally during presentation
- Server lacks CGI support

**Use static HTML if:**
- Simplest deployment
- Server has limitations
- Time is limited

---

## 👥 Team Distribution

- **Aleksandr:** User, Progress Tracking, Workout-Exercise forms
- **Siwoo:** Gym, Class, Class Booking forms
- **Arslan:** Workout, Exercise, Gym Member forms

---

**Assignment 5 - Database Systems 2025**  
**CGI Implementation - Working Database Version**

