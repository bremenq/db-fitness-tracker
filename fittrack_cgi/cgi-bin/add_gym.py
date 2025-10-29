Executing command on clabsql.clamv.constructor.university: cat ~/public_html/add_gym.py
#!/usr/bin/python3
print('Content-Type: text/html; charset=utf-8')
print()

import cgi
import sys
from datetime import datetime
import pymysql

DB_CONFIG = {
    'host': 'localhost',
    'user': 'azinovev',
    'password': 'WrtqlLcpgCPs0KGY',
    'database': 'db_azinovev',
    'charset': 'utf8mb4'
}

def print_html_start(title):
    print(f'''<!DOCTYPE html>
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
        <div class="container">''')

def print_html_end():
    print('''        </div>
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
</html>''')

def add_gym(form_data):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        name = form_data.getvalue('name', '')
        address = form_data.getvalue('address', '')
        phone = form_data.getvalue('phone', '')
        email = form_data.getvalue('email', '')
        
        if not all([name, address]):
            raise ValueError("Missing required fields")
        
        sql = "INSERT INTO gym (name, address, phone, email) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, address, phone if phone else None, email if email else None))
        conn.commit()
        
        gym_id = cursor.lastrowid
        cursor.close()
        conn.close()
        
        return True, gym_id, name
        
    except pymysql.Error as e:
        return False, None, f"Database error: {str(e)}"
    except Exception as e:
        return False, None, f"Error: {str(e)}"

form = cgi.FieldStorage()
success, gym_id, message = add_gym(form)

print_html_start("Add Gym Result")

if success:
    print(f'''
        <section class="feedback-section">
            <div class="success-message">
                <h1>✅ Gym Added Successfully!</h1>
                <div class="feedback-details">
                    <p><strong>Gym ID:</strong> {gym_id}</p>
                    <p><strong>Name:</strong> {message}</p>
                    <p><strong>Address:</strong> {form.getvalue('address', '')}</p>
                    <p><strong>Phone:</strong> {form.getvalue('phone', 'N/A')}</p>
                    <p><strong>Email:</strong> {form.getvalue('email', 'N/A')}</p>
                </div>
                <div class="feedback-actions">
                    <a href="/~azinovev/forms/add_gym.html" class="btn-primary">Add Another Gym</a>
                    <a href="/~azinovev/maintenance.html" class="btn-secondary">Back to Maintenance</a>
                </div>
            </div>
        </section>
    ''')
else:
    print(f'''
        <section class="feedback-section">
            <div class="error-message">
                <h1>❌ Error Adding Gym</h1>
                <div class="feedback-details">
                    <p><strong>Error:</strong> {message}</p>
                </div>
                <div class="feedback-actions">
                    <a href="javascript:history.back()" class="btn-primary">Go Back</a>
                    <a href="/~azinovev/maintenance.html" class="btn-secondary">Back to Maintenance</a>
                </div>
            </div>
        </section>
    ''')

print_html_end()
