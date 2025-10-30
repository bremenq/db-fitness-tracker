#!/usr/bin/python3
import sys
import pymysql
import cgi
import cgitb

cgitb.enable()

DB_CONFIG = {
    'host': 'localhost',
    'user': 'azinovev',
    'password': '****',
    'database': 'db_azinovev',
    'charset': 'utf8mb4'
}

def print_header():
    print("Content-Type: text/html; charset=utf-8\n")

def get_exercise_details(exercise_id):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        
        cursor.execute("""
            SELECT 
                exercise_id,
                name,
                category,
                difficulty,
                muscle_groups,
                equipment_needed,
                instructions
            FROM exercise
            WHERE exercise_id = %s
        """, (exercise_id,))
        
        exercise = cursor.fetchone()
        
        cursor.execute("""
            SELECT 
                COUNT(DISTINCT we.workout_id) as total_workouts,
                COUNT(DISTINCT w.user_id) as total_users,
                AVG(we.sets) as avg_sets,
                AVG(we.reps) as avg_reps,
                AVG(we.weight) as avg_weight,
                MAX(we.sets) as max_sets,
                MAX(we.reps) as max_reps,
                MAX(we.weight) as max_weight
            FROM workout_exercise we
            JOIN workout w ON we.workout_id = w.workout_id
            WHERE we.exercise_id = %s
        """, (exercise_id,))
        
        stats = cursor.fetchone()
        
        cursor.execute("""
            SELECT 
                u.user_id,
                u.first_name,
                u.last_name,
                u.email,
                COUNT(we.workout_id) as workout_count,
                AVG(we.sets) as avg_sets,
                AVG(we.reps) as avg_reps,
                AVG(we.weight) as avg_weight,
                MAX(we.weight) as max_weight
            FROM workout_exercise we
            JOIN workout w ON we.workout_id = w.workout_id
            JOIN user u ON w.user_id = u.user_id
            WHERE we.exercise_id = %s
            GROUP BY u.user_id, u.first_name, u.last_name, u.email
            ORDER BY workout_count DESC, max_weight DESC
            LIMIT 10
        """, (exercise_id,))
        
        top_performers = cursor.fetchall()
        
        cursor.execute("""
            SELECT 
                w.workout_id,
                w.workout_name,
                w.date,
                u.first_name,
                u.last_name,
                we.sets,
                we.reps,
                we.weight
            FROM workout_exercise we
            JOIN workout w ON we.workout_id = w.workout_id
            JOIN user u ON w.user_id = u.user_id
            WHERE we.exercise_id = %s
            ORDER BY w.date DESC
            LIMIT 15
        """, (exercise_id,))
        
        recent_activities = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return exercise, stats, top_performers, recent_activities
    except Exception as e:
        return None, None, None, None

def format_date(date_obj):
    if date_obj:
        return date_obj.strftime('%Y-%m-%d')
    return 'N/A'

def main():
    print_header()
    
    form = cgi.FieldStorage()
    exercise_id = form.getvalue('exercise_id')
    
    if not exercise_id:
        print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Error - FitTrack Pro</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <h2>Error</h2>
        <p>No exercise ID provided.</p>
        <a href="forms/search_exercise_performance.html" class="btn btn-primary">Back to Search</a>
    </div>
</body>
</html>""")
        return
    
    exercise, stats, top_performers, recent_activities = get_exercise_details(exercise_id)
    
    print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercise Details - FitTrack Pro</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <div class="header-content">
            <a href="index.html">
                <img src="img/fittrack-pro-logo.svg" alt="FitTrack Pro Logo" class="logo">
            </a>
            <nav>
                <a href="index.html">Home</a>
                <a href="maintenance.html">Forms</a>
                <a href="forms/search_hub.html">Search</a>
                <a href="imprint.html">Imprint</a>
            </nav>
        </div>
    </header>

    <main>
        <div class="container">
            <div class="navigation-actions">
                <a href="javascript:history.back()" class="btn btn-secondary">← Back to Results</a>
                <a href="forms/search_exercise_performance.html" class="btn btn-secondary">New Search</a>
            </div>
    """)
    
    if exercise is None:
        print("""
            <h2>Error</h2>
            <div class="error-message">
                <p>Unable to retrieve exercise details. Please try again.</p>
            </div>
        """)
    else:
        print(f"""
            <h2>Exercise Details: {exercise['name']}</h2>
            
            <div class="detail-section">
                <h3>Exercise Information</h3>
                <table class="data-table">
                    <tr>
                        <th>Name</th>
                        <td>{exercise['name']}</td>
                    </tr>
                    <tr>
                        <th>Category</th>
                        <td>{exercise['category']}</td>
                    </tr>
                    <tr>
                        <th>Difficulty</th>
                        <td>{exercise['difficulty']}</td>
                    </tr>
                    <tr>
                        <th>Muscle Groups</th>
                        <td>{exercise['muscle_groups'] if exercise['muscle_groups'] else 'N/A'}</td>
                    </tr>
                    <tr>
                        <th>Equipment Needed</th>
                        <td>{exercise['equipment_needed'] if exercise['equipment_needed'] else 'None'}</td>
                    </tr>
                    <tr>
                        <th>Instructions</th>
                        <td>{exercise['instructions'] if exercise['instructions'] else 'N/A'}</td>
                    </tr>
                </table>
            </div>

            <div class="detail-section">
                <h3>Performance Statistics</h3>
                <div class="user-stats-grid">
                    <div class="stat-card">
                        <div class="stat-value">{stats['total_users'] if stats['total_users'] else 0}</div>
                        <div class="stat-label">Total Users</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{stats['total_workouts'] if stats['total_workouts'] else 0}</div>
                        <div class="stat-label">Total Workouts</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{f"{stats['avg_sets']:.1f}" if stats['avg_sets'] else 'N/A'}</div>
                        <div class="stat-label">Avg Sets</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{f"{stats['avg_reps']:.1f}" if stats['avg_reps'] else 'N/A'}</div>
                        <div class="stat-label">Avg Reps</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{f"{stats['avg_weight']:.1f}" if stats['avg_weight'] else 'N/A'}</div>
                        <div class="stat-label">Avg Weight</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{stats['max_weight'] if stats['max_weight'] else 'N/A'}</div>
                        <div class="stat-label">Max Weight</div>
                    </div>
                </div>
            </div>
        """)
        
        if top_performers and len(top_performers) > 0:
            print("""
            <div class="detail-section">
                <h3>Top Performers</h3>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>User</th>
                            <th>Email</th>
                            <th>Workouts</th>
                            <th>Avg Sets</th>
                            <th>Avg Reps</th>
                            <th>Avg Weight</th>
                            <th>Max Weight</th>
                        </tr>
                    </thead>
                    <tbody>
            """)
            
            for performer in top_performers:
                print(f"""
                        <tr>
                            <td>{performer['first_name']} {performer['last_name']}</td>
                            <td>{performer['email']}</td>
                            <td>{performer['workout_count']}</td>
                            <td>{f"{performer['avg_sets']:.1f}" if performer['avg_sets'] else 'N/A'}</td>
                            <td>{f"{performer['avg_reps']:.1f}" if performer['avg_reps'] else 'N/A'}</td>
                            <td>{f"{performer['avg_weight']:.1f}" if performer['avg_weight'] else 'N/A'}</td>
                            <td>{performer['max_weight'] if performer['max_weight'] else 'N/A'}</td>
                        </tr>
                """)
            
            print("""
                    </tbody>
                </table>
            </div>
            """)
        else:
            print("""
            <div class="detail-section">
                <h3>Top Performers</h3>
                <p class="no-results">No performance data available yet.</p>
            </div>
            """)
        
        if recent_activities and len(recent_activities) > 0:
            print("""
            <div class="detail-section">
                <h3>Recent Activity</h3>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Workout</th>
                            <th>User</th>
                            <th>Sets</th>
                            <th>Reps</th>
                            <th>Weight</th>
                        </tr>
                    </thead>
                    <tbody>
            """)
            
            for activity in recent_activities:
                print(f"""
                        <tr>
                            <td>{format_date(activity['date'])}</td>
                            <td>{activity['workout_name']}</td>
                            <td>{activity['first_name']} {activity['last_name']}</td>
                            <td>{activity['sets'] if activity['sets'] else 'N/A'}</td>
                            <td>{activity['reps'] if activity['reps'] else 'N/A'}</td>
                            <td>{activity['weight'] if activity['weight'] else 'N/A'}</td>
                        </tr>
                """)
            
            print("""
                    </tbody>
                </table>
            </div>
            """)
        else:
            print("""
            <div class="detail-section">
                <h3>Recent Activity</h3>
                <p class="no-results">No recent activity found.</p>
            </div>
            """)
    
    print("""
        </div>
    </main>

    <footer>
        <p>&copy; 2025 FitTrack Pro. All rights reserved.</p>
    </footer>
</body>
</html>
    """)

if __name__ == "__main__":
    main()

