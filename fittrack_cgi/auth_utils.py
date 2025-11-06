#!/usr/bin/env python3

import os
import sys
import hashlib
import secrets
import time
from http import cookies
import pymysql

DB_CONFIG = {
    'host': 'localhost',
    'user': 'azinovev',
    'password': 'WrtqlLcpgCPs0KGY',
    'database': 'db_azinovev',
    'charset': 'utf8mb4'
}

SESSION_DURATION = 1800
SESSIONS_DIR = '/tmp/fittrack_sessions'

def get_db_connection():
    try:
        return pymysql.connect(**DB_CONFIG)
    except Exception as e:
        return None

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, password_hash):
    return hash_password(password) == password_hash

def generate_session_token():
    return secrets.token_hex(32)

def get_session_cookie():
    cookie = cookies.SimpleCookie()
    cookie_string = os.environ.get('HTTP_COOKIE', '')
    if cookie_string:
        cookie.load(cookie_string)
        if 'fittrack_session' in cookie:
            return cookie['fittrack_session'].value
    return None

def create_session(username, admin_id):
    session_token = generate_session_token()
    
    if not os.path.exists(SESSIONS_DIR):
        try:
            os.makedirs(SESSIONS_DIR, mode=0o700)
        except:
            pass
    
    session_file = os.path.join(SESSIONS_DIR, session_token)
    try:
        with open(session_file, 'w') as f:
            f.write(f"{admin_id}\n")
            f.write(f"{username}\n")
            f.write(f"{int(time.time())}\n")
        os.chmod(session_file, 0o600)
    except:
        pass
    
    cookie = cookies.SimpleCookie()
    cookie['fittrack_session'] = session_token
    cookie['fittrack_session']['path'] = '/'
    cookie['fittrack_session']['max-age'] = SESSION_DURATION
    cookie['fittrack_session']['httponly'] = True
    
    return cookie.output()

def check_session():
    session_token = get_session_cookie()
    if not session_token:
        return None
    
    session_file = os.path.join(SESSIONS_DIR, session_token)
    if not os.path.exists(session_file):
        return None
    
    try:
        with open(session_file, 'r') as f:
            lines = f.readlines()
            if len(lines) < 3:
                return None
            
            admin_id = lines[0].strip()
            username = lines[1].strip()
            created_time = int(lines[2].strip())
            
            if time.time() - created_time > SESSION_DURATION:
                os.remove(session_file)
                return None
            
            return {
                'admin_id': admin_id,
                'username': username
            }
    except:
        return None

def destroy_session():
    session_token = get_session_cookie()
    if session_token:
        session_file = os.path.join(SESSIONS_DIR, session_token)
        if os.path.exists(session_file):
            try:
                os.remove(session_file)
            except:
                pass
    
    cookie = cookies.SimpleCookie()
    cookie['fittrack_session'] = ''
    cookie['fittrack_session']['path'] = '/'
    cookie['fittrack_session']['max-age'] = 0
    
    return cookie.output()

def authenticate_user(username, password):
    conn = get_db_connection()
    if not conn:
        return None
    
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        
        query = """
            SELECT admin_id, username, password_hash, full_name, is_active
            FROM admin_user
            WHERE username = %s
        """
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        
        if not user:
            return None
        
        if not user['is_active']:
            return None
        
        password_hash = hash_password(password)
        if password_hash != user['password_hash']:
            return None
        
        update_query = "UPDATE admin_user SET last_login = NOW() WHERE admin_id = %s"
        cursor.execute(update_query, (user['admin_id'],))
        conn.commit()
        
        return user
        
    except Exception as e:
        return None
    finally:
        conn.close()

def require_auth():
    user = check_session()
    if not user:
        print("Status: 401 Unauthorized")
        print("Content-Type: text/html\n")
        print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Access Denied - FitTrack Pro</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
        .error-container {
            max-width: 600px;
            margin: 100px auto;
            padding: 40px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        .error-icon {
            font-size: 64px;
            color: #e74c3c;
            margin-bottom: 20px;
        }
        .error-title {
            font-size: 32px;
            color: #2c3e50;
            margin-bottom: 10px;
        }
        .error-message {
            font-size: 18px;
            color: #7f8c8d;
            margin-bottom: 30px;
        }
        .btn-login {
            display: inline-block;
            padding: 12px 30px;
            background: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            font-size: 16px;
            transition: background 0.3s;
        }
        .btn-login:hover {
            background: #2980b9;
        }
    </style>
</head>
<body>
    <div class="error-container">
        <div class="error-icon">🔒</div>
        <h1 class="error-title">Access Denied</h1>
        <p class="error-message">You must be logged in to perform this action.</p>
        <a href="login.html" class="btn-login">Login to Continue</a>
        <p style="margin-top: 20px;">
            <a href="index.html" style="color: #3498db;">Return to Home</a>
        </p>
    </div>
</body>
</html>""")
        sys.exit(0)
    
    return user

def print_login_status():
    user = check_session()
    if user:
        return f"""
        <div class="login-status" style="padding: 10px; background: #d4edda; border: 1px solid #c3e6cb; border-radius: 4px; margin-bottom: 20px;">
            <span style="color: #155724;">✓ Logged in as: <strong>{user['username']}</strong></span>
            <a href="logout.py" style="margin-left: 20px; color: #721c24;">Logout</a>
        </div>
        """
    else:
        return """
        <div class="login-status" style="padding: 10px; background: #f8d7da; border: 1px solid #f5c6cb; border-radius: 4px; margin-bottom: 20px;">
            <span style="color: #721c24;">⚠ Not logged in</span>
            <a href="login.html" style="margin-left: 20px; color: #004085;">Login</a>
        </div>
        """

