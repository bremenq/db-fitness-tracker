#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
CGI Script to add a new fitness class
"""

import cgi
import cgitb
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import auth_utils

user = auth_utils.require_auth()

import pymysql

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
    print("Content-Type: text/html; charset=utf-8\n")

def print_html_start(title):
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

def add_class(form_data):
    """Add class to database"""
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        gym_id = form_data.getvalue('gym_id', '')
        trainer_id = form_data.getvalue('trainer_id', '') or None
        name = form_data.getvalue('name', '')
        description = form_data.getvalue('description', None)
        schedule_time = form_data.getvalue('schedule_time', '')
        duration = form_data.getvalue('duration', '')
        max_capacity = form_data.getvalue('max_capacity', None)
        
        # Validate required fields
        if not all([gym_id, name, schedule_time, duration]):
            raise ValueError("Missing required fields")
        
        # Insert data
        sql = """
            INSERT INTO class (gym_id, trainer_id, name, description, schedule_time, duration, max_capacity)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (gym_id, trainer_id if trainer_id else None, name, description if description else None, schedule_time, duration, max_capacity if max_capacity else None))
        conn.commit()
        
        result_id = cursor.lastrowid
        
        cursor.close()
        conn.close()
        
        return True, result_id, "Class added"
        
    except pymysql.Error as e:
        return False, None, f"Database error: {str(e)}"
    except Exception as e:
        return False, None, f"Error: {str(e)}"


def main():
    print_header()
    form = cgi.FieldStorage()
    success, result_id, message = add_class(form)
    
    print_html_start("Class Result")
    
    if success:
        print(f"""
            <section class="feedback-section">
                <div class="success-message">
                    <h1>✅ Class Added Successfully!</h1>
                    <div class="feedback-details">
                        <p><strong>ID:</strong> {result_id}</p>
                        <p><strong>Gym Id:</strong> {form.getvalue("gym_id", "N/A")}</p>
                        <p><strong>Trainer Id:</strong> {form.getvalue("trainer_id", "N/A")}</p>
                        <p><strong>Name:</strong> {form.getvalue("name", "N/A")}</p>
                    </div>
                    <div class="feedback-actions">
                        <a href="/~azinovev/forms/add_class.html" class="btn-primary">Add Another Class</a>
                        <a href="/~azinovev/maintenance.html" class="btn-secondary">Back to Maintenance</a>
                    </div>
                </div>
            </section>
        """)
    else:
        print(f"""
            <section class="feedback-section">
                <div class="error-message">
                    <h1>❌ Error Adding Class</h1>
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
