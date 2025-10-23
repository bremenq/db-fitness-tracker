#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CGI Script to add a new exercise to the library
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

def add_exercise(form_data):
    """Add exercise to database"""
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        name = form_data.getvalue('name', '')
        category = form_data.getvalue('category', None)
        muscle_groups = form_data.getvalue('muscle_groups', None)
        difficulty = form_data.getvalue('difficulty', None)
        instructions = form_data.getvalue('instructions', None)
        equipment_needed = form_data.getvalue('equipment_needed', None)
        
        # Validate required fields
        if not all([name]):
            raise ValueError("Missing required fields")
        
        # Insert data
        sql = """
            INSERT INTO exercise (name, category, muscle_groups, difficulty, instructions, equipment_needed)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (name, category if category else None, muscle_groups if muscle_groups else None, difficulty if difficulty else None, instructions if instructions else None, equipment_needed if equipment_needed else None))
        conn.commit()
        
        result_id = cursor.lastrowid
        
        cursor.close()
        conn.close()
        
        return True, result_id, "Exercise added"
        
    except pymysql.Error as e:
        return False, None, f"Database error: {str(e)}"
    except Exception as e:
        return False, None, f"Error: {str(e)}"


def main():
    print_header()
    form = cgi.FieldStorage()
    success, result_id, message = add_exercise(form)
    
    print_html_start("Exercise Result")
    
    if success:
        print(f"""
            <section class="feedback-section">
                <div class="success-message">
                    <h1>✅ Exercise Added Successfully!</h1>
                    <div class="feedback-details">
                        <p><strong>ID:</strong> {result_id}</p>
                        <p><strong>Name:</strong> {form.getvalue("name", "N/A")}</p>
                        <p><strong>Category:</strong> {form.getvalue("category", "N/A")}</p>
                        <p><strong>Muscle Groups:</strong> {form.getvalue("muscle_groups", "N/A")}</p>
                    </div>
                    <div class="feedback-actions">
                        <a href="/~azinovev/forms/add_exercise.html" class="btn-primary">Add Another Exercise</a>
                        <a href="/~azinovev/maintenance.html" class="btn-secondary">Back to Maintenance</a>
                    </div>
                </div>
            </section>
        """)
    else:
        print(f"""
            <section class="feedback-section">
                <div class="error-message">
                    <h1>❌ Error Adding Exercise</h1>
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
