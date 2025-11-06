#!/usr/bin/env python3

import cgi
import cgitb
import sys
import os

cgitb.enable()

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import auth_utils

def main():
    form = cgi.FieldStorage()
    
    username = form.getvalue('username', '').strip()
    password = form.getvalue('password', '')
    
    if not username or not password:
        print("Location: login.html?error=required\n")
        return
    
    user = auth_utils.authenticate_user(username, password)
    
    if not user:
        print("Location: login.html?error=invalid\n")
        return
    
    if not user['is_active']:
        print("Location: login.html?error=inactive\n")
        return
    
    session_cookie = auth_utils.create_session(user['username'], user['admin_id'])
    
    print(session_cookie)
    print("Location: maintenance.html\n")

if __name__ == '__main__':
    main()

