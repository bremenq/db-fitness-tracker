#!/usr/bin/python3
print('Content-Type: text/html; charset=utf-8')
print()

import cgi
import sys
import os
from datetime import datetime
import pymysql

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'pymysql'))

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

def search_user_activity(form_data):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Get form parameters
        user_type_filter = form_data.getvalue('user_type', '').strip()
        min_users = int(form_data.getvalue('min_users', '1') or '1')
        date_from = form_data.getvalue('date_from', '').strip()
        date_to = form_data.getvalue('date_to', '').strip()
        min_calories = form_data.getvalue('min_calories', '').strip()
        sort_by = form_data.getvalue('sort_by', 'total_users').strip()
        
        # Build the base query
        sql = '''
        SELECT 
            CASE 
                WHEN iu.user_id IS NOT NULL THEN 'Individual User'
                WHEN gm.user_id IS NOT NULL THEN 'Gym Member'  
                WHEN s.user_id IS NOT NULL THEN 'Staff'
                ELSE 'Other'
            END AS user_type,
            COUNT(DISTINCT u.user_id) AS total_users,
            COUNT(w.workout_id) AS total_workouts,
            ROUND(AVG(w.calories_burned), 2) AS avg_calories
        FROM user u
        LEFT JOIN individual_user iu ON u.user_id = iu.user_id
        LEFT JOIN gym_member gm ON u.user_id = gm.user_id  
        LEFT JOIN staff s ON u.user_id = s.user_id
        LEFT JOIN workout w ON u.user_id = w.user_id
        '''
        
        # Add WHERE conditions
        where_conditions = []
        params = []
        
        if date_from:
            where_conditions.append('w.date >= %s')
            params.append(date_from)
            
        if date_to:
            where_conditions.append('w.date <= %s')
            params.append(date_to)
        
        if where_conditions:
            sql += ' WHERE ' + ' AND '.join(where_conditions)
        
        sql += ' GROUP BY user_type'
        
        # Add HAVING conditions
        having_conditions = [f'total_users >= {min_users}']
        
        if min_calories:
            having_conditions.append(f'avg_calories >= {float(min_calories)}')
        
        sql += ' HAVING ' + ' AND '.join(having_conditions)
        
        # Add user type filter after GROUP BY if specified
        if user_type_filter:
            sql += f" AND user_type = '{user_type_filter}'"
        
        # Add ORDER BY
        sort_mapping = {
            'total_users': 'total_users DESC',
            'total_workouts': 'total_workouts DESC', 
            'avg_calories': 'avg_calories DESC',
            'user_type': 'user_type ASC'
        }
        sql += f' ORDER BY {sort_mapping.get(sort_by, "total_users DESC")}'
        
        cursor.execute(sql, params)
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
    success, results, error_msg = search_user_activity(form)
    
    print_html_start("User Activity Search Results")
    
    if success and results:
        print(f'''
        <section class="search-results-section">
            <h1>👥 User Activity Search Results</h1>
            <div class="results-navigation">
                <a href="/~azinovev/forms/search_user_activity.html" class="btn-secondary">← New Search</a>
                <a href="/~azinovev/forms/search_hub.html" class="btn-secondary">← Search Hub</a>
            </div>
            
            <div class="results-summary">
                <p><strong>Found {len(results)} user group(s)</strong> matching your criteria</p>
            </div>
            
            <div class="results-table">
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>User Type</th>
                            <th>Total Users</th>
                            <th>Total Workouts</th>
                            <th>Avg Calories</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
        ''')
        
        for row in results:
            user_type, total_users, total_workouts, avg_calories = row
            avg_calories_display = f"{avg_calories:.1f}" if avg_calories else "N/A"
            
            print(f'''
                        <tr>
                            <td><strong>{user_type}</strong></td>
                            <td>{total_users}</td>
                            <td>{total_workouts}</td>
                            <td>{avg_calories_display}</td>
                            <td>
                                <a href="/~azinovev/user_detail.py?user_type={user_type.replace(' ', '%20')}" 
                                   class="btn-small">View Details</a>
                            </td>
                        </tr>
            ''')
        
        print('''
                    </tbody>
                </table>
            </div>
            
            <div class="results-help">
                <h3>💡 Understanding Results:</h3>
                <ul>
                    <li><strong>User Type:</strong> Category of users in the system</li>
                    <li><strong>Total Users:</strong> Number of users in this category</li>
                    <li><strong>Total Workouts:</strong> All workouts performed by this group</li>
                    <li><strong>Avg Calories:</strong> Average calories burned per workout</li>
                    <li><strong>View Details:</strong> See individual users in this category</li>
                </ul>
            </div>
        </section>
        ''')
        
    elif success and not results:
        print(f'''
        <section class="search-results-section">
            <h1>👥 User Activity Search Results</h1>
            <div class="results-navigation">
                <a href="/~azinovev/forms/search_user_activity.html" class="btn-secondary">← New Search</a>
                <a href="/~azinovev/forms/search_hub.html" class="btn-secondary">← Search Hub</a>
            </div>
            
            <div class="no-results">
                <h2>No Results Found</h2>
                <p>No user groups match your search criteria. Try:</p>
                <ul>
                    <li>Reducing the minimum users filter</li>
                    <li>Expanding the date range</li>
                    <li>Lowering the minimum calories threshold</li>
                    <li>Selecting a different user type</li>
                </ul>
            </div>
        </section>
        ''')
    else:
        print(f'''
        <section class="search-results-section">
            <div class="error-message">
                <h1>❌ Search Error</h1>
                <div class="feedback-details">
                    <p><strong>Error:</strong> {error_msg}</p>
                </div>
                <div class="feedback-actions">
                    <a href="/~azinovev/forms/search_user_activity.html" class="btn-primary">← Try Again</a>
                    <a href="/~azinovev/forms/search_hub.html" class="btn-secondary">← Search Hub</a>
                </div>
            </div>
        </section>
        ''')
    
    print_html_end()

if __name__ == '__main__':
    main()
