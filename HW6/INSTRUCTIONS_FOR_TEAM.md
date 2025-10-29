# HW6 Instructions for Lee and Arslan

## Why CGI Instead of Flask?

We're using **Python CGI scripts** instead of Flask for HW5 and HW6 because:

1. **ClamV Server Limitations:**
   - The university server doesn't support Flask/mod_wsgi
   - We don't have admin privileges to install Flask frameworks
   - CGI works out-of-the-box on Apache without special configuration

2. **Simplicity:**
   - CGI scripts are standalone Python files that run directly
   - No framework dependencies or complex setup
   - Just upload `.py` files and they work immediately

3. **Already Working:**
   - All 9 HW5 forms are working with CGI
   - Database connection works perfectly
   - Deployed and tested on the server

---

## Where to Find Everything

### 📂 Repository Structure

```
db-fitness-tracker/
├── HW6/
│   ├── HW6_Search_Implementation_Plan.md  ← **READ THIS FIRST!**
│   └── INSTRUCTIONS_FOR_TEAM.md           ← This file
│
└── fittrack_cgi/                          ← **Work here!**
    ├── DEPLOYMENT_INSTRUCTIONS.md         ← How to deploy to server
    ├── README.md                          ← Project overview
    │
    ├── forms/
    │   ├── search_user_activity.html      ← Aleksandr's example (DONE)
    │   ├── search_gym_members.html        ← Lee: Update this
    │   └── search_exercise_performance.html ← Arslan: Create this
    │
    ├── search_user_activity.py            ← Aleksandr's example (DONE)
    ├── user_detail.py                     ← Aleksandr's example (DONE)
    │
    ├── search_gym_members.py              ← Lee: Create this
    ├── gym_member_detail.py               ← Lee: Create this
    │
    ├── search_exercise_performance.py     ← Arslan: Create this
    └── exercise_detail.py                 ← Arslan: Create this
```

---

## What You Need to Do

### Step 1: Get the Code

```bash
git clone https://github.com/bremenq/db-fitness-tracker.git
cd db-fitness-tracker
git checkout HW6
```

### Step 2: Read the Plan

Open and read: **`HW6/HW6_Search_Implementation_Plan.md`**

This file contains:
- ✅ Aleksandr's completed work (use as example!)
- 🚧 Your specific tasks
- 📝 Suggested implementation steps
- 💡 Database queries to use

### Step 3: Study My Implementation (Aleksandr's completed work)

**Look at these 3 files to understand the pattern:**

1. **Search Form:** `fittrack_cgi/forms/search_user_activity.html`
   - See how the form is structured
   - Note: `action="../search_user_activity.py"` (points to root, not cgi-bin!)
   - Note: `method="GET"` (search uses GET, not POST)

2. **Search Results CGI:** `fittrack_cgi/search_user_activity.py`
   - See how it processes GET parameters
   - See how it builds SQL queries
   - See how it returns HTML with results table
   - See how "View Details" links work

3. **Detail Page CGI:** `fittrack_cgi/user_detail.py`
   - See how it accepts `user_id` parameter
   - See how it queries multiple tables
   - See how it displays comprehensive information

### Step 4: Implement Your Search

**For Lee (Gym Member Search):**

1. Update `fittrack_cgi/forms/search_gym_members.html`:
   - Add filters: gym dropdown, membership type, status, dates
   - Set `action="../search_gym_members.py"` and `method="GET"`

2. Create `fittrack_cgi/search_gym_members.py`:
   - Copy structure from `search_user_activity.py`
   - Query: JOIN gym_member, user, gym, staff tables
   - Display: member name, gym name, membership type, manager
   - Add "View Details" links with member_id

3. Create `fittrack_cgi/gym_member_detail.py`:
   - Copy structure from `user_detail.py`
   - Accept `member_id` parameter
   - Show: member info, gym details, class bookings

**For Arslan (Exercise Performance Search):**

1. Create `fittrack_cgi/forms/search_exercise_performance.html`:
   - Add filters: exercise category, difficulty, muscle group, dates
   - Set `action="../search_exercise_performance.py"` and `method="GET"`

2. Create `fittrack_cgi/search_exercise_performance.py`:
   - Copy structure from `search_user_activity.py`
   - Query: JOIN exercise, workout_exercise, workout tables
   - Display: exercise name, category, total sessions, avg duration
   - Add "View Details" links with exercise_id

3. Create `fittrack_cgi/exercise_detail.py`:
   - Copy structure from `user_detail.py`
   - Accept `exercise_id` parameter
   - Show: exercise info, instructions, session history

### Step 5: Test Locally (Optional)

You can test the HTML forms locally by opening them in a browser, but the CGI scripts need to be on the server to work.

### Step 6: Deploy to ClamV Server

Follow the instructions in: **`fittrack_cgi/DEPLOYMENT_INSTRUCTIONS.md`**

Quick deploy command:
```bash
cd fittrack_cgi

# Set your credentials
USERNAME="your_username"
PASSWORD="your_password"

# Deploy everything
sshpass -p "$PASSWORD" scp -r ./* ${USERNAME}@clabsql.clamv.constructor.university:~/public_html/ && \
sshpass -p "$PASSWORD" ssh ${USERNAME}@clabsql.clamv.constructor.university "chmod +x ~/public_html/*.py"
```

### Step 7: Test on Server

Visit: `https://clabsql.clamv.constructor.university/~your_username/forms/search_hub.html`

Test your search functionality!

---

## Important Notes

⚠️ **CGI scripts go in ROOT directory, NOT in cgi-bin!**
- ✅ Correct: `~/public_html/search_gym_members.py`
- ❌ Wrong: `~/public_html/cgi-bin/search_gym_members.py`

⚠️ **Forms use GET method for search, not POST!**
- ✅ Search forms: `method="GET"`
- ✅ Add forms (HW5): `method="POST"`

⚠️ **Database credentials:**
- Host: `localhost` (not clabsql.clamv.constructor.university)
- Database: `db_your_username`
- Check Aleksandr's scripts for the exact pattern

⚠️ **Test data available:**
- 28 users in database
- 110 workouts
- Multiple gym members
- Various exercises

---

## Need Help?

1. **Read the implementation plan:** `HW6/HW6_Search_Implementation_Plan.md`
2. **Study my code:** It's your best example!
3. **Check deployment guide:** `fittrack_cgi/DEPLOYMENT_INSTRUCTIONS.md`
4. **Ask in the team chat:** I'm here to help!

---

## Deadline

**2025-10-30 23:59**

My part is done (33% complete). We need Lee and Arslan to complete their searches to finish HW6!

Good luck! 🚀

