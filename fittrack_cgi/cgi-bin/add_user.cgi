#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CGI Script to add a new user to FitTrack Pro database
"""

import cgi
import cgitb
import pymysql
import sys
from datetime import datetime

# Enable CGI error reporting
cgitb.enable()

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'azinovev',
    'password': 'WrtqlLcpgCPs0KGY',
    'database': 'db_azinovev',
    'charset': 'utf8mb4'
}

def print_header():
    """Print HTTP header"""
    print("Content-Type: text/html; charset=utf-8\n")

def print_html_start(title):
    """Print HTML document start"""
    print(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - FitTrack Pro</title>
    <link rel="stylesheet" href="/~azinovev/css/style.css">
</head>
<body>
    <header>
        <div class="container">
            <div class="logo">
                <img src="/~azinovev/img/fittrack-pro-logo.svg" alt="FitTrack Pro" height="40">
                <h1>FitTrack<span class="highlight">Pro</span></h1>
            </div>
            <nav>
                <ul>
                    <li><a href="/~azinovev/index.html">Home</a></li>
                    <li><a href="/~azinovev/index.html#features">Features</a></li>
                    <li><a href="/~azinovev/maintenance.html">Maintenance</a></li>
                    <li><a href="/~azinovev/index.html#about">About</a></li>
                    <li><a href="/~azinovev/imprint.html">Imprint</a></li>
                </ul>
            </nav>
        </div>
    </header>
    <main>
        <div class="container">""")

def print_html_end():
    """Print HTML document end"""
    print("""        </div>
    </main>
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>FitTrack<span class="highlight">Pro</span></h3>
                    <p>Database Systems Project 2025</p>
                </div>
                <div class="footer-section">
                    <h4>Development Team</h4>
                    <p>Aleksandr Zinovev<br>
                    Siwoo Lee<br>
                    Arslan Ahmet Berk</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 FitTrack Pro. Database Systems Course Project.</p>
            </div>
        </div>
    </footer>
</body>
</html>""")

def add_user(form_data):
    """Add user to database"""
    try:
        # Connect to database
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Get form data
        username = form_data.getvalue('username', '')
        email = form_data.getvalue('email', '')
        password_hash = form_data.getvalue('password_hash', '')  # In production, hash this!
        first_name = form_data.getvalue('first_name', '')
        last_name = form_data.getvalue('last_name', '')
        date_of_birth = form_data.getvalue('date_of_birth', None)
        gender = form_data.getvalue('gender', None)
        
        # Validate required fields
        if not all([username, email, password_hash, first_name, last_name]):
            raise ValueError("Missing required fields")
        
        # Insert user
        sql = """
            INSERT INTO user (username, email, password_hash, first_name, last_name, 
                            date_of_birth, gender)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (username, email, password_hash, first_name, last_name, 
                           date_of_birth if date_of_birth else None, 
                           gender if gender else None))
        conn.commit()
        
        user_id = cursor.lastrowid
        
        cursor.close()
        conn.close()
        
        return True, user_id, username
        
    except pymysql.Error as e:
        return False, None, f"Database error: {str(e)}"
    except Exception as e:
        return False, None, f"Error: {str(e)}"

def main():
    """Main CGI handler"""
    print_header()
    
    # Get form data
    form = cgi.FieldStorage()
    
    # Process form submission
    success, user_id, message = add_user(form)
    
    # Display result
    print_html_start("Add User Result")
    
    if success:
        print(f"""
            <section class="feedback-section">
                <div class="success-message">
                    <h1>✅ User Added Successfully!</h1>
                    <div class="feedback-details">
                        <p><strong>User ID:</strong> {user_id}</p>
                        <p><strong>Username:</strong> {message}</p>
                        <p><strong>Email:</strong> {form.getvalue('email', '')}</p>
                        <p><strong>Name:</strong> {form.getvalue('first_name', '')} {form.getvalue('last_name', '')}</p>
                    </div>
                    <div class="feedback-actions">
                        <a href="/~azinovev/forms/add_user.html" class="btn-primary">Add Another User</a>
                        <a href="/~azinovev/maintenance.html" class="btn-secondary">Back to Maintenance</a>
                    </div>
                </div>
            </section>
        """)
    else:
        print(f"""
            <section class="feedback-section">
                <div class="error-message">
                    <h1>❌ Error Adding User</h1>
                    <div class="feedback-details">
                        <p><strong>Error:</strong> {message}</p>
                    </div>
                    <div class="feedback-actions">
                        <a href="javascript:history.back()" class="btn-primary">Go Back</a>
                        <a href="/~azinovev/maintenance.html" class="btn-secondary">Back to Maintenance</a>
                    </div>
                </div>
            </section>
        """)
    
    print_html_end()

if __name__ == '__main__':
    main()

