#!/usr/bin/python3
import sys
import pymysql
import cgi
import cgitb

cgitb.enable()

DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': '****',
    'database': 'db_your_username',
    'charset': 'utf8mb4'
}

def print_header():
    print("Content-Type: text/html; charset=utf-8\n")

def get_member_details(member_id):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        
        cursor.execute("""
            SELECT 
                u.user_id,
                u.first_name,
                u.last_name,
                u.email,
                u.date_of_birth,
                u.gender,
                u.username,
                gm.membership_type,
                gm.start_date,
                gm.end_date,
                DATEDIFF(gm.end_date, gm.start_date) as duration_days,
                CASE 
                    WHEN gm.end_date >= CURDATE() THEN 'Active'
                    ELSE 'Expired'
                END as status
            FROM user u
            JOIN gym_member gm ON u.user_id = gm.user_id
            WHERE gm.user_id = %s
        """, (member_id,))
        
        member = cursor.fetchone()
        
        cursor.execute("""
            SELECT 
                w.workout_id,
                w.workout_name,
                w.date,
                w.duration,
                w.calories_burned
            FROM workout w
            WHERE w.user_id = %s
            ORDER BY w.date DESC
            LIMIT 10
        """, (member_id,))
        
        workouts = cursor.fetchall()
        
        cursor.execute("""
            SELECT 
                cb.booking_id,
                c.name as class_name,
                c.schedule_time,
                c.duration,
                cb.status,
                cb.booking_date
            FROM class_booking cb
            JOIN class c ON cb.class_id = c.class_id
            WHERE cb.user_id = %s
            ORDER BY c.schedule_time DESC
            LIMIT 10
        """, (member_id,))
        
        bookings = cursor.fetchall()
        
        cursor.execute("""
            SELECT 
                COUNT(*) as total_workouts,
                SUM(duration) as total_duration,
                SUM(calories_burned) as total_calories,
                AVG(calories_burned) as avg_calories
            FROM workout
            WHERE user_id = %s
        """, (member_id,))
        
        stats = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        return member, workouts, bookings, stats
    except Exception as e:
        return None, None, None, None

def format_date(date_obj):
    if date_obj:
        return date_obj.strftime('%Y-%m-%d')
    return 'N/A'

def format_datetime(datetime_obj):
    if datetime_obj:
        return datetime_obj.strftime('%Y-%m-%d %H:%M')
    return 'N/A'

def main():
    print_header()
    
    form = cgi.FieldStorage()
    member_id = form.getvalue('member_id')
    
    if not member_id:
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
        <p>No member ID provided.</p>
        <a href="forms/search_gym_members.html" class="btn btn-primary">Back to Search</a>
    </div>
</body>
</html>""")
        return
    
    member, workouts, bookings, stats = get_member_details(member_id)
    
    print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Member Details - FitTrack Pro</title>
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
                <a href="forms/search_gym_members.html" class="btn btn-secondary">New Search</a>
            </div>
    """)
    
    if member is None:
        print("""
            <h2>Error</h2>
            <div class="error-message">
                <p>Unable to retrieve member details. Please try again.</p>
            </div>
        """)
    else:
        status_class = 'active' if member['status'] == 'Active' else 'expired'
        
        print(f"""
            <h2>Member Details: {member['first_name']} {member['last_name']}</h2>
            
            <div class="detail-section">
                <h3>Personal Information</h3>
                <table class="data-table">
                    <tr>
                        <th>Name</th>
                        <td>{member['first_name']} {member['last_name']}</td>
                    </tr>
                    <tr>
                        <th>Email</th>
                        <td>{member['email']}</td>
                    </tr>
                    <tr>
                        <th>Username</th>
                        <td>{member['username']}</td>
                    </tr>
                    <tr>
                        <th>Date of Birth</th>
                        <td>{format_date(member['date_of_birth'])}</td>
                    </tr>
                    <tr>
                        <th>Gender</th>
                        <td>{member['gender'] if member['gender'] else 'N/A'}</td>
                    </tr>
                </table>
            </div>

            <div class="detail-section">
                <h3>Membership Information</h3>
                <table class="data-table">
                    <tr>
                        <th>Membership Type</th>
                        <td>{member['membership_type']}</td>
                    </tr>
                    <tr>
                        <th>Start Date</th>
                        <td>{format_date(member['start_date'])}</td>
                    </tr>
                    <tr>
                        <th>End Date</th>
                        <td>{format_date(member['end_date'])}</td>
                    </tr>
                    <tr>
                        <th>Duration</th>
                        <td>{member['duration_days']} days</td>
                    </tr>
                    <tr>
                        <th>Status</th>
                        <td><span class="status-badge status-{status_class}">{member['status']}</span></td>
                    </tr>
                </table>
            </div>

            <div class="detail-section">
                <h3>Activity Statistics</h3>
                <div class="user-stats-grid">
                    <div class="stat-card">
                        <div class="stat-value">{stats['total_workouts'] if stats['total_workouts'] else 0}</div>
                        <div class="stat-label">Total Workouts</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{stats['total_duration'] if stats['total_duration'] else 0}</div>
                        <div class="stat-label">Total Minutes</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{stats['total_calories'] if stats['total_calories'] else 0}</div>
                        <div class="stat-label">Total Calories</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{int(stats['avg_calories']) if stats['avg_calories'] else 0}</div>
                        <div class="stat-label">Avg Calories/Workout</div>
                    </div>
                </div>
            </div>
        """)
        
        if workouts and len(workouts) > 0:
            print("""
            <div class="detail-section">
                <h3>Recent Workouts</h3>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>Workout Name</th>
                            <th>Date</th>
                            <th>Duration (min)</th>
                            <th>Calories Burned</th>
                        </tr>
                    </thead>
                    <tbody>
            """)
            
            for workout in workouts:
                print(f"""
                        <tr>
                            <td>{workout['workout_name']}</td>
                            <td>{format_date(workout['date'])}</td>
                            <td>{workout['duration']}</td>
                            <td>{workout['calories_burned']}</td>
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
                <h3>Recent Workouts</h3>
                <p class="no-results">No workout history available.</p>
            </div>
            """)
        
        if bookings and len(bookings) > 0:
            print("""
            <div class="detail-section">
                <h3>Class Bookings</h3>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>Class Name</th>
                            <th>Schedule Time</th>
                            <th>Duration (min)</th>
                            <th>Status</th>
                            <th>Booking Date</th>
                        </tr>
                    </thead>
                    <tbody>
            """)
            
            for booking in bookings:
                print(f"""
                        <tr>
                            <td>{booking['class_name']}</td>
                            <td>{format_datetime(booking['schedule_time'])}</td>
                            <td>{booking['duration']}</td>
                            <td>{booking['status']}</td>
                            <td>{format_datetime(booking['booking_date'])}</td>
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
                <h3>Class Bookings</h3>
                <p class="no-results">No class bookings found.</p>
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

