#!/usr/bin/python3
import cgi
import pymysql
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pymysql'))

DB_CONFIG = {
    'host': 'localhost',
    'user': 'azinovev',
    'password': 'WrtqlLcpgCPs0KGY',
    'database': 'db_azinovev'
}

def print_header():
    print('Content-Type: text/html; charset=utf-8\n')

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
                <h1>FitTrack<span class="highlight">Pro</span></h1>
            </div>
        </div>
    </header>
    <main>
        <div class="container">''')

def print_html_end():
    print('''
        </div>
    </main>
    <footer>
        <div class="container">
            <p>&copy; 2025 FitTrack Pro. Database Systems Course Project.</p>
        </div>
    </footer>
</body>
</html>''')

def add_gym_member(form_data):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        user_id = form_data.getvalue('user_id', '')
        gym_id = form_data.getvalue('gym_id', '')
        membership_id = form_data.getvalue('membership_id', '')
        membership_type = form_data.getvalue('membership_type', '')
        start_date = form_data.getvalue('start_date', '')
        end_date = form_data.getvalue('end_date', '')
        
        if not all([user_id, gym_id, membership_id, membership_type, start_date]):
            raise ValueError('Missing required fields')
        
        sql = '''INSERT INTO gym_member (user_id, gym_id, membership_id, membership_type, start_date, end_date) 
                 VALUES (%s, %s, %s, %s, %s, %s)'''
        cursor.execute(sql, (user_id, gym_id, membership_id, membership_type, start_date, end_date if end_date else None))
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return True, f'User {user_id} - Gym {gym_id}', 'gym_member'
        
    except pymysql.Error as e:
        return False, None, f'Database error: {str(e)}'
    except Exception as e:
        return False, None, f'Error: {str(e)}'

def main():
    print_header()
    
    form = cgi.FieldStorage()
    success, record_id, message = add_gym_member(form)
    
    print_html_start('Gym Member Result')
    
    if success:
        print(f'''
            <section class="feedback-section">
                <div class="success-message">
                    <h1>✅ Gym Membership Added Successfully!</h1>
                    <div class="feedback-details">
                        <p><strong>Link:</strong> {record_id}</p>
                        <p><strong>Membership ID:</strong> {form.getvalue('membership_id', 'N/A')}</p>
                        <p><strong>Type:</strong> {form.getvalue('membership_type', 'N/A')}</p>
                        <p><strong>Start Date:</strong> {form.getvalue('start_date', '')}</p>
                        <p><strong>End Date:</strong> {form.getvalue('end_date', 'N/A')}</p>
                    </div>
                    <div class="feedback-actions">
                        <a href="/~azinovev/forms/add_gym_member.html" class="btn-primary">Add Another Membership</a>
                        <a href="/~azinovev/maintenance.html" class="btn-secondary">Back to Maintenance</a>
                    </div>
                </div>
            </section>
        ''')
    else:
        print(f'''
            <section class="feedback-section">
                <div class="error-message">
                    <h1>❌ Error Adding Gym Membership</h1>
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

if __name__ == '__main__':
    main()
