#!/usr/bin/python3
import sys
import pymysql
import cgi
import cgitb
from datetime import datetime

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

def get_search_results(params):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        
        query = """
            SELECT 
                gm.member_id,
                u.first_name,
                u.last_name,
                u.email,
                gm.membership_type,
                gm.start_date,
                gm.end_date,
                DATEDIFF(gm.end_date, gm.start_date) as duration_days,
                CASE 
                    WHEN gm.end_date >= CURDATE() THEN 'Active'
                    ELSE 'Expired'
                END as status
            FROM gym_member gm
            JOIN user u ON gm.member_id = u.user_id
            WHERE 1=1
        """
        
        query_params = []
        
        if params.get('membership_type'):
            query += " AND gm.membership_type = %s"
            query_params.append(params['membership_type'])
        
        if params.get('status') == 'active':
            query += " AND gm.end_date >= CURDATE()"
        elif params.get('status') == 'expired':
            query += " AND gm.end_date < CURDATE()"
        
        if params.get('start_date_from'):
            query += " AND gm.start_date >= %s"
            query_params.append(params['start_date_from'])
        
        if params.get('start_date_to'):
            query += " AND gm.start_date <= %s"
            query_params.append(params['start_date_to'])
        
        if params.get('min_duration'):
            query += " AND DATEDIFF(gm.end_date, gm.start_date) >= %s"
            query_params.append(int(params['min_duration']))
        
        sort_by = params.get('sort_by', 'start_date_desc')
        sort_mapping = {
            'start_date_desc': 'gm.start_date DESC',
            'start_date_asc': 'gm.start_date ASC',
            'end_date_desc': 'gm.end_date DESC',
            'end_date_asc': 'gm.end_date ASC',
            'duration_desc': 'duration_days DESC',
            'duration_asc': 'duration_days ASC'
        }
        query += f" ORDER BY {sort_mapping.get(sort_by, 'gm.start_date DESC')}"
        
        cursor.execute(query, query_params)
        results = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return results
    except Exception as e:
        return None

def format_date(date_obj):
    if date_obj:
        return date_obj.strftime('%Y-%m-%d')
    return 'N/A'

def main():
    print_header()
    
    form = cgi.FieldStorage()
    
    params = {
        'membership_type': form.getvalue('membership_type', ''),
        'status': form.getvalue('status', ''),
        'start_date_from': form.getvalue('start_date_from', ''),
        'start_date_to': form.getvalue('start_date_to', ''),
        'min_duration': form.getvalue('min_duration', ''),
        'sort_by': form.getvalue('sort_by', 'start_date_desc')
    }
    
    results = get_search_results(params)
    
    print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gym Member Search Results - FitTrack Pro</title>
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
                <a href="forms/search_gym_members.html" class="btn btn-secondary">← Back to Search</a>
                <a href="forms/search_hub.html" class="btn btn-secondary">Search Hub</a>
            </div>

            <h2>Gym Member Search Results</h2>
    """)
    
    if results is None:
        print("""
            <div class="error-message">
                <p>An error occurred while searching. Please try again.</p>
            </div>
        """)
    elif len(results) == 0:
        print("""
            <div class="no-results">
                <p>No gym members found matching your criteria.</p>
                <p>Try adjusting your search filters.</p>
            </div>
        """)
    else:
        print(f"""
            <div class="results-summary">
                <p>Found <strong>{len(results)}</strong> gym member(s)</p>
            </div>

            <div class="results-table">
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>Member Name</th>
                            <th>Email</th>
                            <th>Membership Type</th>
                            <th>Start Date</th>
                            <th>End Date</th>
                            <th>Duration (days)</th>
                            <th>Status</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
        """)
        
        for row in results:
            status_class = 'active' if row['status'] == 'Active' else 'expired'
            print(f"""
                        <tr>
                            <td>{row['first_name']} {row['last_name']}</td>
                            <td>{row['email']}</td>
                            <td>{row['membership_type']}</td>
                            <td>{format_date(row['start_date'])}</td>
                            <td>{format_date(row['end_date'])}</td>
                            <td>{row['duration_days']}</td>
                            <td><span class="status-badge status-{status_class}">{row['status']}</span></td>
                            <td><a href="member_detail.py?member_id={row['member_id']}" class="btn btn-small">View Details</a></td>
                        </tr>
            """)
        
        print("""
                    </tbody>
                </table>
            </div>
        """)
    
    print("""
            <div class="search-help">
                <h3>About This Search</h3>
                <ul>
                    <li><strong>Active:</strong> Membership end date is today or in the future</li>
                    <li><strong>Expired:</strong> Membership end date has passed</li>
                    <li><strong>Duration:</strong> Number of days between start and end date</li>
                    <li>Click "View Details" to see complete member information</li>
                </ul>
            </div>
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

