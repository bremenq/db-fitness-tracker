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

def get_search_results(params):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        
        query = """
            SELECT 
                e.exercise_id,
                e.name as exercise_name,
                e.category,
                e.difficulty,
                e.muscle_groups,
                e.equipment_needed,
                COUNT(DISTINCT we.workout_id) as total_workouts,
                COUNT(DISTINCT w.user_id) as total_users,
                AVG(we.sets) as avg_sets,
                AVG(we.reps) as avg_reps,
                AVG(we.weight) as avg_weight
            FROM exercise e
            LEFT JOIN workout_exercise we ON e.exercise_id = we.exercise_id
            LEFT JOIN workout w ON we.workout_id = w.workout_id
            WHERE 1=1
        """
        
        query_params = []
        
        if params.get('category'):
            query += " AND e.category = %s"
            query_params.append(params['category'])
        
        if params.get('difficulty'):
            query += " AND e.difficulty = %s"
            query_params.append(params['difficulty'])
        
        if params.get('muscle_group'):
            query += " AND e.muscle_groups LIKE %s"
            query_params.append(f"%{params['muscle_group']}%")
        
        query += " GROUP BY e.exercise_id, e.name, e.category, e.difficulty, e.muscle_groups, e.equipment_needed"
        
        if params.get('min_users'):
            query += " HAVING COUNT(DISTINCT w.user_id) >= %s"
            query_params.append(int(params['min_users']))
        
        if params.get('min_avg_sets'):
            if params.get('min_users'):
                query += " AND AVG(we.sets) >= %s"
            else:
                query += " HAVING AVG(we.sets) >= %s"
            query_params.append(float(params['min_avg_sets']))
        
        if params.get('min_avg_reps'):
            if params.get('min_users') or params.get('min_avg_sets'):
                query += " AND AVG(we.reps) >= %s"
            else:
                query += " HAVING AVG(we.reps) >= %s"
            query_params.append(float(params['min_avg_reps']))
        
        sort_by = params.get('sort_by', 'users_desc')
        sort_mapping = {
            'users_desc': 'total_users DESC',
            'users_asc': 'total_users ASC',
            'avg_sets_desc': 'avg_sets DESC',
            'avg_sets_asc': 'avg_sets ASC',
            'avg_reps_desc': 'avg_reps DESC',
            'avg_reps_asc': 'avg_reps ASC',
            'name_asc': 'e.name ASC'
        }
        query += f" ORDER BY {sort_mapping.get(sort_by, 'total_users DESC')}"
        
        cursor.execute(query, query_params)
        results = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return results
    except Exception as e:
        return None

def main():
    print_header()
    
    form = cgi.FieldStorage()
    
    params = {
        'category': form.getvalue('category', ''),
        'difficulty': form.getvalue('difficulty', ''),
        'muscle_group': form.getvalue('muscle_group', ''),
        'min_users': form.getvalue('min_users', ''),
        'min_avg_sets': form.getvalue('min_avg_sets', ''),
        'min_avg_reps': form.getvalue('min_avg_reps', ''),
        'sort_by': form.getvalue('sort_by', 'users_desc')
    }
    
    results = get_search_results(params)
    
    print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercise Performance Results - FitTrack Pro</title>
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
                <a href="forms/search_exercise_performance.html" class="btn btn-secondary">← Back to Search</a>
                <a href="forms/search_hub.html" class="btn btn-secondary">Search Hub</a>
            </div>

            <h2>Exercise Performance Results</h2>
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
                <p>No exercises found matching your criteria.</p>
                <p>Try adjusting your search filters.</p>
            </div>
        """)
    else:
        print(f"""
            <div class="results-summary">
                <p>Found <strong>{len(results)}</strong> exercise(s)</p>
            </div>

            <div class="results-table">
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>Exercise Name</th>
                            <th>Category</th>
                            <th>Difficulty</th>
                            <th>Muscle Groups</th>
                            <th>Total Users</th>
                            <th>Total Workouts</th>
                            <th>Avg Sets</th>
                            <th>Avg Reps</th>
                            <th>Avg Weight</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
        """)
        
        for row in results:
            avg_sets = f"{row['avg_sets']:.1f}" if row['avg_sets'] else 'N/A'
            avg_reps = f"{row['avg_reps']:.1f}" if row['avg_reps'] else 'N/A'
            avg_weight = f"{row['avg_weight']:.1f}" if row['avg_weight'] else 'N/A'
            
            print(f"""
                        <tr>
                            <td>{row['exercise_name']}</td>
                            <td>{row['category']}</td>
                            <td>{row['difficulty']}</td>
                            <td>{row['muscle_groups'] if row['muscle_groups'] else 'N/A'}</td>
                            <td>{row['total_users']}</td>
                            <td>{row['total_workouts']}</td>
                            <td>{avg_sets}</td>
                            <td>{avg_reps}</td>
                            <td>{avg_weight}</td>
                            <td><a href="exercise_detail.py?exercise_id={row['exercise_id']}" class="btn btn-small">View Details</a></td>
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
                    <li><strong>Total Users:</strong> Number of unique users who performed this exercise</li>
                    <li><strong>Total Workouts:</strong> Number of workouts including this exercise</li>
                    <li><strong>Avg Sets/Reps/Weight:</strong> Average performance metrics across all users</li>
                    <li>Click "View Details" to see complete exercise information and top performers</li>
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

