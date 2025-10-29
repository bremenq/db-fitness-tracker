#!/usr/bin/python3
print('Content-Type: text/html; charset=utf-8')
print()

import cgi
import sys
from datetime import datetime
import pymysql

DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': '****',
    'database': 'db_your_username',
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

def add_class_booking(form_data):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        member_id = form_data.getvalue('user_id', '')  # Form uses user_id but DB uses member_id
        class_id = form_data.getvalue('class_id', '')
        booking_date = form_data.getvalue('booking_date', '')
        status = form_data.getvalue('status', 'Booked')
        
        if not all([member_id, class_id, booking_date]):
            raise ValueError("Missing required fields")
        
        # Convert date format if needed
        if booking_date:
            try:
                # Convert YYYY-MM-DD to proper timestamp
                booking_date = f"{booking_date} 00:00:00"
            except:
                pass
        
        sql = "INSERT INTO class_booking (member_id, class_id, booking_date, status) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (member_id, class_id, booking_date, status))
        conn.commit()
        
        booking_id = cursor.lastrowid
        cursor.close()
        conn.close()
        
        return True, booking_id, f"Member {member_id} - Class {class_id}"
        
    except pymysql.Error as e:
        return False, None, f"Database error: {str(e)}"
    except Exception as e:
        return False, None, f"Error: {str(e)}"

form = cgi.FieldStorage()
success, booking_id, message = add_class_booking(form)

print_html_start("Add Class Booking Result")

if success:
    print(f'''
        <section class="feedback-section">
            <div class="success-message">
                <h1>✅ Class Booking Added Successfully!</h1>
                <div class="feedback-details">
                    <p><strong>Booking ID:</strong> {booking_id}</p>
                    <p><strong>Link:</strong> {message}</p>
                    <p><strong>Booking Date:</strong> {form.getvalue('booking_date', '')}</p>
                    <p><strong>Status:</strong> {form.getvalue('status', 'Booked')}</p>
                </div>
                <div class="feedback-actions">
                    <a href="/~azinovev/forms/add_class_booking.html" class="btn-primary">Add Another Booking</a>
                    <a href="/~azinovev/maintenance.html" class="btn-secondary">Back to Maintenance</a>
                </div>
            </div>
        </section>
    ''')
else:
    print(f'''
        <section class="feedback-section">
            <div class="error-message">
                <h1>❌ Error Adding Class Booking</h1>
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
