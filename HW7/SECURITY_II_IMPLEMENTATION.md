# Security II - Web Service Authentication Implementation

**Assignment:** Databases Project 2025 - Assignment 7 (Security II)  
**Team:** Aleksandr Zinovev, Siwoo Lee, Arslan Ahmet Berk  
**Date:** November 2025

---

## Overview

This document describes the implementation of user authentication and access control for the FitTrack Pro web service. The system protects all maintenance/write operations (INSERT/UPDATE/DELETE) while keeping search/read operations (SELECT) publicly accessible.

---

## Architecture

### Authentication Approach

**Session-Based Authentication:**
- User credentials stored in database with hashed passwords (SHA2-256)
- Session tokens stored in browser cookies
- File-based session storage in `/tmp/fittrack_sessions/`
- Session duration: 30 minutes (1800 seconds)
- Python CGI scripts validate session before allowing write operations

### Security Model

**Public Access (No Authentication Required):**
- Search pages (SELECT queries only)
  - User Activity Search
  - Gym Member Search
  - Exercise Performance Search
  - Detail pages (user_detail.py, member_detail.py, exercise_detail.py)
  - Data retrieval for dropdowns (get_data.py)

**Protected Access (Authentication Required):**
- All maintenance/write operations
  - add_user.py
  - add_gym.py
  - add_gym_member.py
  - add_exercise.py
  - add_workout.py
  - add_workout_exercise.py
  - add_class.py
  - add_class_booking.py
  - add_progress.py

---

## Database Schema

### admin_user Table

```sql
CREATE TABLE IF NOT EXISTS admin_user (
    admin_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL,
    is_active BOOLEAN DEFAULT TRUE,
    
    CONSTRAINT chk_username_length CHECK (LENGTH(username) >= 3)
);
```

### user_session Table (Optional)

For database-backed sessions (currently using file-based):

```sql
CREATE TABLE IF NOT EXISTS user_session (
    session_id VARCHAR(64) PRIMARY KEY,
    admin_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL,
    ip_address VARCHAR(45),
    user_agent TEXT,
    
    FOREIGN KEY (admin_id) REFERENCES admin_user(admin_id) ON DELETE CASCADE,
    INDEX idx_expires (expires_at)
);
```

---

## Implementation Components

### 1. Authentication Module (`auth_utils.py`)

Core authentication library providing:

**Functions:**
- `hash_password(password)` - SHA2-256 hashing
- `verify_password(password, password_hash)` - Password verification
- `generate_session_token()` - Secure random token generation
- `get_session_cookie()` - Extract session from HTTP cookies
- `create_session(username, admin_id)` - Create new session
- `check_session()` - Validate existing session
- `destroy_session()` - Logout/clear session
- `authenticate_user(username, password)` - Login verification
- `require_auth()` - CGI script protection wrapper
- `print_login_status()` - HTML status indicator

**Session Storage:**
- Location: `/tmp/fittrack_sessions/`
- Format: Plain text files with admin_id, username, timestamp
- Permissions: 0600 (owner read/write only)
- Automatic expiration after 30 minutes

### 2. Login System

**login.html:**
- Clean, corporate-styled login form
- Username and password fields
- Error message display
- Default credentials shown for testing
- Client-side validation

**login.py:**
- POST request handler
- Authenticates against admin_user table
- Creates session on success
- Redirects to maintenance.html or shows error

**logout.py:**
- Destroys session
- Clears cookie
- Redirects to index.html

### 3. Protected CGI Scripts

All 9 write-operation scripts include authentication check:

```python
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import auth_utils

# Check authentication BEFORE any output
user = auth_utils.require_auth()

# If user is None, require_auth() already sent 401 error and exited
# Continue with normal script logic...
```

**Protected Scripts:**
1. add_user.py - User creation
2. add_gym.py - Gym creation
3. add_gym_member.py - Member registration
4. add_exercise.py - Exercise definition
5. add_workout.py - Workout logging
6. add_workout_exercise.py - Exercise-workout linking
7. add_class.py - Class scheduling
8. add_class_booking.py - Class booking
9. add_progress.py - Progress tracking

### 4. Maintenance Page Updates

**maintenance.html:**
- Login status indicator (JavaScript-based)
- Shows "Logged in" with Logout button when authenticated
- Shows "Not logged in" with Login button when not authenticated
- Cookie-based status check (no server round-trip)

---

## Default Credentials

**For Testing and TA Review:**

- **Username:** `admin`
- **Password:** `fittrack2025`
- **Full Name:** System Administrator
- **Email:** admin@fittrack.local

**Password Hash (SHA2-256):**
```
8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
```

---

## Installation & Setup

### 1. Create Database Schema

```bash
# On ClamV server
mysql -u your_username -p db_your_username < HW7/security_ii_schema.sql
```

### 2. Deploy Files

```bash
# From local machine
cd db1/fittrack_cgi

# Upload authentication files
scp auth_utils.py login.html login.py logout.py your_username@clamv.constructor.university:~/public_html/

# Upload updated CGI scripts (all 9 add_*.py files)
scp add_*.py your_username@clamv.constructor.university:~/public_html/

# Upload updated maintenance.html
scp maintenance.html your_username@clamv.constructor.university:~/public_html/
```

### 3. Set Permissions

```bash
# On ClamV server
chmod 755 ~/public_html/*.py
chmod 644 ~/public_html/login.html
chmod 644 ~/public_html/maintenance.html
```

### 4. Create Session Directory

```bash
# On ClamV server (if needed)
mkdir -p /tmp/fittrack_sessions
chmod 700 /tmp/fittrack_sessions
```

---

## Usage

### For Users

1. **Access Maintenance Page:**
   - Navigate to `maintenance.html`
   - See login status indicator

2. **Login:**
   - Click "Login" button
   - Enter username and password
   - Redirected to maintenance page on success

3. **Add Data:**
   - Click any "Add" button
   - Form submits to protected CGI script
   - Data is saved if authenticated

4. **Logout:**
   - Click "Logout" button in maintenance page
   - Session destroyed, redirected to home

### For Administrators

**Add New Admin User:**

```sql
INSERT INTO admin_user (username, password_hash, full_name, email) 
VALUES (
    'newadmin', 
    SHA2('password123', 256), 
    'New Administrator', 
    'newadmin@fittrack.local'
);
```

**Deactivate User:**

```sql
UPDATE admin_user 
SET is_active = FALSE 
WHERE username = 'oldadmin';
```

**View Login History:**

```sql
SELECT username, full_name, last_login, is_active 
FROM admin_user 
ORDER BY last_login DESC;
```

---

## Security Features

### Password Security
- **Hashing:** SHA2-256 (not plaintext)
- **No password recovery:** Admins must reset via SQL
- **Minimum length:** 3 characters (enforced at DB level for username)

### Session Security
- **Random tokens:** 64-character hexadecimal (256-bit entropy)
- **HttpOnly cookies:** Not accessible via JavaScript
- **Expiration:** 30-minute timeout
- **File permissions:** 0600 (owner-only access)

### Error Handling
- **401 Unauthorized:** Not logged in
- **Graceful errors:** User-friendly error pages
- **No information leakage:** Generic "invalid credentials" message

### SQL Injection Prevention
- **Parameterized queries:** All database interactions use placeholders
- **Input validation:** Form data validated before processing

---

## Testing

### Test Authentication Flow

1. **Test Unauthenticated Access:**
   ```
   Visit: add_user.html
   Fill form and submit
   Expected: 401 error with login link
   ```

2. **Test Login:**
   ```
   Visit: login.html
   Username: admin
   Password: fittrack2025
   Expected: Redirect to maintenance.html with "Logged in" status
   ```

3. **Test Authenticated Access:**
   ```
   After login, visit: add_user.html
   Fill form and submit
   Expected: User created successfully
   ```

4. **Test Logout:**
   ```
   Click "Logout" button
   Expected: Redirect to index.html, session cleared
   ```

5. **Test Session Expiration:**
   ```
   Login and wait 31 minutes
   Try to add data
   Expected: 401 error (session expired)
   ```

6. **Test Public Access:**
   ```
   Without login, visit: forms/search_hub.html
   Perform searches
   Expected: All search functions work without authentication
   ```

### Test Invalid Credentials

1. **Wrong Password:**
   ```
   Username: admin
   Password: wrongpassword
   Expected: "Invalid username or password" error
   ```

2. **Non-existent User:**
   ```
   Username: nonexistent
   Password: anything
   Expected: "Invalid username or password" error
   ```

3. **Inactive User:**
   ```
   SQL: UPDATE admin_user SET is_active = FALSE WHERE username = 'admin';
   Try to login
   Expected: "Your account has been deactivated" error
   ```

---

## Troubleshooting

### Problem: "Module auth_utils not found"

**Solution:**
- Verify `auth_utils.py` is in the same directory as CGI scripts
- Check file permissions: `chmod 644 auth_utils.py`
- Verify `sys.path.insert(0, ...)` line is present in CGI script

### Problem: "Permission denied" when creating session

**Solution:**
- Create session directory: `mkdir -p /tmp/fittrack_sessions`
- Set permissions: `chmod 700 /tmp/fittrack_sessions`
- Or modify `SESSIONS_DIR` in `auth_utils.py` to writable location

### Problem: Login succeeds but immediately logged out

**Solution:**
- Check cookie settings in browser (must allow cookies)
- Verify cookie path is set to `/`
- Check if browser blocks third-party cookies

### Problem: Session expires too quickly

**Solution:**
- Increase `SESSION_DURATION` in `auth_utils.py` (default: 1800 seconds = 30 minutes)
- Example: `SESSION_DURATION = 3600` for 1 hour

### Problem: Can't login with default credentials

**Solution:**
- Verify admin user exists: `SELECT * FROM admin_user WHERE username = 'admin';`
- Re-run schema: `mysql -u user -p database < HW7/security_ii_schema.sql`
- Check password hash matches: `SHA2('fittrack2025', 256)`

---

## Assignment Requirements Checklist

- ✅ **User management table created:** `admin_user` table with hashed passwords
- ✅ **Maintenance pages have login fields:** `login.html` with username/password
- ✅ **Read pages (SELECT) remain public:** All search pages accessible without login
- ✅ **Write pages (INSERT/UPDATE/DELETE) require authentication:** All 9 add_*.py scripts protected
- ✅ **Unauthorized requests rejected:** 401 error page with login link
- ✅ **Admin user added via INSERT:** Default admin in `security_ii_schema.sql`
- ✅ **Website accessible via web browser:** All pages functional on ClamV
- ✅ **Code in repository:** All files committed to GitHub

---

## Future Enhancements

**Potential Improvements:**
1. **Database-backed sessions:** Use `user_session` table instead of files
2. **Password strength requirements:** Enforce minimum length, complexity
3. **Multi-factor authentication:** SMS or email verification
4. **Role-based access control:** Different permission levels (admin, editor, viewer)
5. **Audit logging:** Track all data modifications with user attribution
6. **Password reset functionality:** Email-based password recovery
7. **HTTPS enforcement:** Redirect HTTP to HTTPS
8. **CSRF protection:** Tokens to prevent cross-site request forgery
9. **Rate limiting:** Prevent brute-force login attempts
10. **Session management UI:** View/revoke active sessions

---

## Files in This Implementation

**New Files:**
- `fittrack_cgi/auth_utils.py` - Authentication library
- `fittrack_cgi/login.html` - Login form
- `fittrack_cgi/login.py` - Login handler
- `fittrack_cgi/logout.py` - Logout handler
- `HW7/security_ii_schema.sql` - Database schema
- `HW7/SECURITY_II_IMPLEMENTATION.md` - This documentation

**Modified Files:**
- `fittrack_cgi/maintenance.html` - Added login status indicator
- `fittrack_cgi/add_user.py` - Added authentication check
- `fittrack_cgi/add_gym.py` - Added authentication check
- `fittrack_cgi/add_gym_member.py` - Added authentication check
- `fittrack_cgi/add_exercise.py` - Added authentication check
- `fittrack_cgi/add_workout.py` - Added authentication check
- `fittrack_cgi/add_workout_exercise.py` - Added authentication check
- `fittrack_cgi/add_class.py` - Added authentication check
- `fittrack_cgi/add_class_booking.py` - Added authentication check
- `fittrack_cgi/add_progress.py` - Added authentication check

**Unchanged Files (Public Access):**
- `fittrack_cgi/search_user_activity.py`
- `fittrack_cgi/search_gym_members.py`
- `fittrack_cgi/search_exercise_performance.py`
- `fittrack_cgi/user_detail.py`
- `fittrack_cgi/member_detail.py`
- `fittrack_cgi/exercise_detail.py`
- `fittrack_cgi/get_data.py`

---

## References

- **Assignment:** `hw/dbws_hw07.pdf` - Security II requirements
- **Lecture:** `lectures/a0_security.pdf` - Database access control concepts
- **Schema:** `fittrack_schema.sql` - Database structure
- **Deployment:** `fittrack_cgi/DEPLOYMENT_INSTRUCTIONS.md` - Server deployment guide

---

**Last Updated:** November 6, 2025  
**Author:** Aleksandr Zinovev  
**Course:** Databases & Web Services (CO-560-B)  
**Status:** ✅ Implementation Complete

