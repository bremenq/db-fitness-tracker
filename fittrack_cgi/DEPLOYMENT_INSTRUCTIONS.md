# 🚀 FitTrack Pro - ClamV Server Deployment Instructions

## ⚡ Quick Deploy (One Command)

```bash
# Set your credentials
USERNAME="your_username"
PASSWORD="your_password"

# Deploy everything at once
sshpass -p "$PASSWORD" scp -r -o PreferredAuthentications=password -o PubkeyAuthentication=no \
  db1/fittrack_cgi/* ${USERNAME}@clabsql.clamv.constructor.university:~/public_html/ && \
sshpass -p "$PASSWORD" ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no \
  ${USERNAME}@clabsql.clamv.constructor.university "chmod +x ~/public_html/*.py"

echo "✅ Deployment complete! Visit: https://clabsql.clamv.constructor.university/~${USERNAME}/"
```

---

## 📋 Prerequisites

Before starting, ensure you have:
- Access to a ClamV server with your student account
- SSH access to the server
- MySQL database access with your credentials
- `sshpass` installed (for password-based deployment)

## 🔧 Step 1: Server Setup

### 1.1 Connect to Your ClamV Server

**Option A: With sshpass (no password prompt)**
```bash
sshpass -p "your_password" ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no \
  your_username@clabsql.clamv.constructor.university
```

**Option B: Interactive (enter password when prompted)**
```bash
ssh your_username@clabsql.clamv.constructor.university
```

### 1.2 Create Directory Structure
```bash
cd ~
mkdir -p public_html/{forms,css,img}
```

### 1.3 Set Proper Permissions
```bash
chmod 755 ~/public_html
chmod 755 ~/public_html/forms
chmod 755 ~/public_html/css
chmod 755 ~/public_html/img
```

## 📦 Step 2: Upload Files

### 2.1 Upload All Files
Upload the entire `fittrack_cgi` folder contents to your server:

**Option A: Using SCP with password (recommended for quick deployment)**
```bash
# Set your credentials
USERNAME="your_username"
PASSWORD="your_password"

# Upload all files at once
sshpass -p "$PASSWORD" scp -r -o PreferredAuthentications=password -o PubkeyAuthentication=no \
  db1/fittrack_cgi/* ${USERNAME}@clabsql.clamv.constructor.university:~/public_html/
```

**Option B: Using SCP with interactive password**
```bash
# Upload forms
scp db1/fittrack_cgi/forms/*.html your_username@clabsql.clamv.constructor.university:~/public_html/forms/

# Upload CGI scripts to root (not cgi-bin!)
scp db1/fittrack_cgi/*.py your_username@clabsql.clamv.constructor.university:~/public_html/

# Upload assets
scp db1/fittrack_cgi/css/style.css your_username@clabsql.clamv.constructor.university:~/public_html/css/
scp db1/fittrack_cgi/img/* your_username@clabsql.clamv.constructor.university:~/public_html/img/

# Upload static pages
scp db1/fittrack_cgi/*.html your_username@clabsql.clamv.constructor.university:~/public_html/
```

**Note:** Install `sshpass` if not available:
```bash
# macOS
brew install sshpass

# Linux
sudo apt-get install sshpass
```

**Option B: Manual Upload via SSH**
```bash
# Connect to server and create files manually
ssh your_username@clabsql.clamv.constructor.university

# For each file, use: cat > filename.html << 'EOF'
# Then paste content and end with 'EOF'
```

### 2.2 Set Script Permissions

**On the server:**
```bash
chmod +x ~/public_html/*.py
```

**Or remotely with sshpass:**
```bash
sshpass -p "your_password" ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no \
  your_username@clabsql.clamv.constructor.university "chmod +x ~/public_html/*.py"
```

## 🗄️ Step 3: Database Configuration

### 3.1 Update Database Credentials
Edit each Python script in `~/public_html/` and update the database configuration:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',        # ← Change this
    'password': 'your_password',    # ← Change this
    'database': 'db_your_username', # ← Change this
    'charset': 'utf8mb4'
}
```

**Files to update:**
- `add_user.py`
- `add_class_booking.py`
- `add_workout_exercise.py`
- `add_class.py`
- `add_exercise.py`
- `add_gym_member.py`
- `add_gym.py`
- `add_progress.py`
- `add_workout.py`
- `get_data.py`

### 3.2 Install Required Python Modules
```bash
pip3 install --user pymysql
```

### 3.3 Copy PyMySQL Module (if needed)
If the above doesn't work, copy the module locally:
```bash
cp -r ~/.local/lib/python3.*/site-packages/pymysql ~/public_html/
```

### 3.4 Create Database Schema
Upload and run the database schema:
```bash
mysql -u your_username -p db_your_username < fittrack_schema.sql
```

## 🔧 Step 4: Configuration Updates

### 4.1 Update Form Actions
In each HTML form in `~/public_html/forms/`, ensure the action points to the correct script:
```html
<form method="POST" action="../script_name.py">
```

### 4.2 Update Navigation Links
In all HTML files, update navigation links to use your username:
```html
<a href="/~your_username/index.html">Home</a>
<a href="/~your_username/maintenance.html">Maintenance</a>
```

## 🧪 Step 5: Testing

### 5.1 Test Basic Access
Visit: `https://clabsql.clamv.constructor.university/~your_username/`

### 5.2 Test Forms
1. Go to: `https://clabsql.clamv.constructor.university/~your_username/maintenance.html`
2. Try the "Add User" form first
3. Check if data appears in your database

### 5.3 Test Dynamic Dropdowns
1. Test "Link Exercise to Workout" form
2. Test "Book Class for Member" form
3. Verify dropdowns populate with database data

## 🐛 Troubleshooting

### Common Issues:

**1. 500 Internal Server Error**
- Check file permissions: `chmod +x ~/public_html/*.py`
- Check shebang line: `#!/usr/bin/python3`
- Check line endings: `dos2unix ~/public_html/*.py`

**2. Module Not Found Error**
```bash
# Copy pymysql locally
cp -r ~/.local/lib/python3.*/site-packages/pymysql ~/public_html/
```

**3. Database Connection Error**
- Verify database credentials in all Python scripts
- Test connection: `mysql -u your_username -p db_your_username`

**4. Forms Download Instead of Execute**
- Ensure scripts are in `~/public_html/` root, not in `cgi-bin/`
- Check Apache configuration allows Python execution

**5. Empty Dropdowns**
- Test `get_data.py` directly: visit `/~your_username/get_data.py?type=users`
- Check database has sample data

## 📝 Quick Checklist

- [ ] Directory structure created
- [ ] All files uploaded with correct permissions
- [ ] Database credentials updated in all 10 Python scripts
- [ ] PyMySQL installed/copied
- [ ] Database schema imported
- [ ] Navigation links updated with your username
- [ ] Basic homepage loads
- [ ] Add User form works
- [ ] Dynamic dropdowns populate
- [ ] All 9 forms tested

## 🆘 Getting Help

If you encounter issues:
1. Check Apache error logs: `tail -f /var/log/apache2/error.log`
2. Test Python scripts directly: `python3 ~/public_html/add_user.py`
3. Verify database connection: `mysql -u your_username -p db_your_username`

## 📊 Expected Result

After successful deployment, you should have:
- ✅ Working homepage at `/~your_username/`
- ✅ 9 functional database forms
- ✅ Dynamic dropdowns in 2 forms
- ✅ Proper success/error feedback
- ✅ All data saving to your database

---

**Good luck with your deployment! 🎉**

*Last updated: October 2025*
