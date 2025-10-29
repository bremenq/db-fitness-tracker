#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
CGI Script to add progress tracking entry
"""

import cgi
import cgitb
import pymysql
import sys

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

def add_progress(form_data):
    """Add progress entry to database"""
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        user_id = form_data.getvalue('user_id', '')
        date = form_data.getvalue('date', '')
        weight = form_data.getvalue('weight', None)
        body_fat_percentage = form_data.getvalue('body_fat_percentage', None)
        muscle_mass = form_data.getvalue('muscle_mass', None)
        measurements = form_data.getvalue('measurements', None)
        
        # Validate required fields
        if not all([user_id, date]):
            raise ValueError("Missing required fields")
        
        # Insert data
        sql = """
            INSERT INTO progress_tracking (user_id, date, weight, body_fat_percentage, muscle_mass, measurements)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (user_id, date, weight if weight else None, body_fat_percentage if body_fat_percentage else None, muscle_mass if muscle_mass else None, measurements if measurements else None))
        conn.commit()
        
        result_id = cursor.lastrowid
        
        cursor.close()
        conn.close()
        
        return True, result_id, "Progress Entry added"
        
    except pymysql.Error as e:
        return False, None, f"Database error: {str(e)}"
    except Exception as e:
        return False, None, f"Error: {str(e)}"


def main():
    print_header()
    form = cgi.FieldStorage()
    success, result_id, message = add_progress(form)
    
    print_html_start("Progress Entry Result")
    
    if success:
        print(f"""
            <section class="feedback-section">
                <div class="success-message">
                    <h1>✅ Progress Entry Added Successfully!</h1>
                    <div class="feedback-details">
                        <p><strong>ID:</strong> {result_id}</p>
                        <p><strong>User Id:</strong> {form.getvalue("user_id", "N/A")}</p>
                        <p><strong>Date:</strong> {form.getvalue("date", "N/A")}</p>
                        <p><strong>Weight:</strong> {form.getvalue("weight", "N/A")}</p>
                    </div>
                    <div class="feedback-actions">
                        <a href="/~azinovev/forms/add_progress.html" class="btn-primary">Add Another Progress Entry</a>
                        <a href="/~azinovev/maintenance.html" class="btn-secondary">Back to Maintenance</a>
                    </div>
                </div>
            </section>
        """)
    else:
        print(f"""
            <section class="feedback-section">
                <div class="error-message">
                    <h1>❌ Error Adding Progress Entry</h1>
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
