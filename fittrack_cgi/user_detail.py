#!/usr/bin/python3
print('Content-Type: text/html; charset=utf-8')
print()

import cgi
import sys
import os
from urllib.parse import unquote
import pymysql

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'pymysql'))

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
                    <li><a href="/~azinovev/forms/search_hub.html" class="active">Search</a></li>
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

def get_user_details(user_type):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Get individual users of the specified type
        sql = '''
        SELECT 
            u.user_id,
            CONCAT(u.first_name, ' ', u.last_name) AS full_name,
            u.email,
            u.gender,
            u.date_of_birth,
            COUNT(w.workout_id) AS total_workouts,
            ROUND(AVG(w.calories_burned), 2) AS avg_calories,
            ROUND(AVG(w.duration), 2) AS avg_duration,
            MAX(w.date) AS last_workout_date
        FROM user u
        LEFT JOIN individual_user iu ON u.user_id = iu.user_id
        LEFT JOIN gym_member gm ON u.user_id = gm.user_id  
        LEFT JOIN staff s ON u.user_id = s.user_id
        LEFT JOIN workout w ON u.user_id = w.user_id
        WHERE 
        '''
        
        if user_type == 'Individual User':
            sql += 'iu.user_id IS NOT NULL'
        elif user_type == 'Gym Member':
            sql += 'gm.user_id IS NOT NULL'
        elif user_type == 'Staff':
            sql += 's.user_id IS NOT NULL'
        else:
            sql += 'iu.user_id IS NULL AND gm.user_id IS NULL AND s.user_id IS NULL'
        
        sql += '''
        GROUP BY u.user_id, u.first_name, u.last_name, u.email, u.gender, u.date_of_birth
        ORDER BY total_workouts DESC, full_name ASC
        '''
        
        cursor.execute(sql)
        results = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return True, results, None
        
    except pymysql.Error as e:
        return False, None, f"Database error: {str(e)}"
    except Exception as e:
        return False, None, f"Error: {str(e)}"

def main():
    form = cgi.FieldStorage()
    user_type = unquote(form.getvalue('user_type', ''))
    
    success, results, error_msg = get_user_details(user_type)
    
    print_html_start(f"{user_type} Details")
    
    if success and results:
        print(f'''
        <section class="detail-section">
            <h1>👤 {user_type} Details</h1>
            <div class="results-navigation">
                <a href="javascript:history.back()" class="btn-secondary">← Back to Results</a>
                <a href="/~azinovev/forms/search_user_activity.html" class="btn-secondary">← New Search</a>
                <a href="/~azinovev/forms/search_hub.html" class="btn-secondary">← Search Hub</a>
            </div>
            
            <div class="results-summary">
                <p><strong>Found {len(results)} user(s)</strong> in the {user_type} category</p>
            </div>
            
            <div class="results-table">
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Gender</th>
                            <th>Date of Birth</th>
                            <th>Total Workouts</th>
                            <th>Avg Calories</th>
                            <th>Avg Duration (min)</th>
                            <th>Last Workout</th>
                        </tr>
                    </thead>
                    <tbody>
        ''')
        
        for row in results:
            user_id, full_name, email, gender, dob, total_workouts, avg_calories, avg_duration, last_workout = row
            
            # Format values
            avg_calories_display = f"{avg_calories:.1f}" if avg_calories else "N/A"
            avg_duration_display = f"{avg_duration:.1f}" if avg_duration else "N/A"
            last_workout_display = last_workout.strftime('%Y-%m-%d') if last_workout else "Never"
            dob_display = dob.strftime('%Y-%m-%d') if dob else "N/A"
            
            print(f'''
                        <tr>
                            <td><strong>{full_name}</strong></td>
                            <td>{email}</td>
                            <td>{gender or 'N/A'}</td>
                            <td>{dob_display}</td>
                            <td>{total_workouts}</td>
                            <td>{avg_calories_display}</td>
                            <td>{avg_duration_display}</td>
                            <td>{last_workout_display}</td>
                        </tr>
            ''')
        
        print('''
                    </tbody>
                </table>
            </div>
            
            <div class="detail-help">
                <h3>💡 Understanding User Details:</h3>
                <ul>
                    <li><strong>Total Workouts:</strong> Number of workout sessions recorded</li>
                    <li><strong>Avg Calories:</strong> Average calories burned per workout</li>
                    <li><strong>Avg Duration:</strong> Average workout duration in minutes</li>
                    <li><strong>Last Workout:</strong> Date of most recent workout session</li>
                </ul>
                
                <h3>📊 User Type Information:</h3>
        ''')
        
        if user_type == 'Individual User':
            print('''
                <p><strong>Individual Users</strong> are fitness enthusiasts who use the system independently 
                for personal workout tracking and progress monitoring.</p>
            ''')
        elif user_type == 'Gym Member':
            print('''
                <p><strong>Gym Members</strong> are users who have active memberships at registered gyms 
                and can access gym facilities and classes.</p>
            ''')
        elif user_type == 'Staff':
            print('''
                <p><strong>Staff</strong> are gym employees including trainers, managers, and receptionists 
                who help manage gym operations and assist members.</p>
            ''')
        
        print('''
            </div>
        </section>
        ''')
        
    elif success and not results:
        print(f'''
        <section class="detail-section">
            <h1>👤 {user_type} Details</h1>
            <div class="results-navigation">
                <a href="javascript:history.back()" class="btn-secondary">← Back to Results</a>
                <a href="/~azinovev/forms/search_user_activity.html" class="btn-secondary">← New Search</a>
                <a href="/~azinovev/forms/search_hub.html" class="btn-secondary">← Search Hub</a>
            </div>
            
            <div class="no-results">
                <h2>No Users Found</h2>
                <p>No users found in the {user_type} category.</p>
            </div>
        </section>
        ''')
    else:
        print(f'''
        <section class="detail-section">
            <div class="error-message">
                <h1>❌ Detail Error</h1>
                <div class="feedback-details">
                    <p><strong>Error:</strong> {error_msg}</p>
                </div>
                <div class="feedback-actions">
                    <a href="javascript:history.back()" class="btn-primary">← Go Back</a>
                    <a href="/~azinovev/forms/search_hub.html" class="btn-secondary">← Search Hub</a>
                </div>
            </div>
        </section>
        ''')
    
    print_html_end()

if __name__ == '__main__':
    main()
