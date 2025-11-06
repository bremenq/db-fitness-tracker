#!/usr/bin/python3
import cgi
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import auth_utils

user = auth_utils.require_auth()

import pymysql

DB_CONFIG = {
    'host': 'localhost',
    'user': 'azinovev',
    'password': '****',
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

def add_exercise(form_data):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        name = form_data.getvalue('name', '')
        category = form_data.getvalue('category', '')
        muscle_groups = form_data.getvalue('muscle_groups', '')
        difficulty = form_data.getvalue('difficulty_level', '')
        instructions = form_data.getvalue('instructions', '')
        equipment_needed = form_data.getvalue('equipment_needed', '')
        
        if not name:
            raise ValueError('Missing required fields')
        
        sql = '''INSERT INTO exercise (name, category, muscle_groups, difficulty, instructions, equipment_needed) 
                 VALUES (%s, %s, %s, %s, %s, %s)'''
        cursor.execute(sql, (
            name, 
            category or None,
            muscle_groups or None, 
            difficulty or None,
            instructions or None, 
            equipment_needed or None
        ))
        conn.commit()
        
        exercise_id = cursor.lastrowid
        cursor.close()
        conn.close()
        
        return True, exercise_id, name
        
    except pymysql.Error as e:
        return False, None, f'Database error: {str(e)}'
    except Exception as e:
        return False, None, f'Error: {str(e)}'

def main():
    print_header()
    
    form = cgi.FieldStorage()
    success, exercise_id, message = add_exercise(form)
    
    print_html_start('Exercise Result')
    
    if success:
        print(f'''
            <section class="feedback-section">
                <div class="success-message">
                    <h1>✅ Exercise Added Successfully!</h1>
                    <div class="feedback-details">
                        <p><strong>Exercise ID:</strong> {exercise_id}</p>
                        <p><strong>Name:</strong> {message}</p>
                        <p><strong>Category:</strong> {form.getvalue('category', 'N/A')}</p>
                    </div>
                    <div class="feedback-actions">
                        <a href="/~azinovev/forms/add_exercise.html" class="btn-primary">Add Another Exercise</a>
                        <a href="/~azinovev/maintenance.html" class="btn-secondary">Back to Maintenance</a>
                    </div>
                </div>
            </section>
        ''')
    else:
        print(f'''
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
        ''')
    
    print_html_end()

if __name__ == '__main__':
    main()
