#!/usr/bin/python3
import pymysql
import cgi
import cgitb
from html import escape
from datetime import datetime

cgitb.enable()

# ====== FILL THESE ON THE SERVER LATER ======
# I should fill them later because i can't access the server
DB_CONFIG = {
    'host': 'localhost',
    'user': 'aharslan',         
    'password': '****',      
    'database': 'db_aharslan',   
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}
# ============================================

def print_header():
    print("Content-Type: text/html; charset=utf-8\n")

def to_int(x):
    try:
        return int(x) if x and str(x).strip() != '' else None
    except:
        return None

def to_float(x):
    try:
        return float(x) if x and str(x).strip() != '' else None
    except:
        return None

def to_date_str(x):
    if not x or str(x).strip() == "":
        return None
    try:
        datetime.strptime(x, "%Y-%m-%d")
        return x
    except ValueError:
        return None

def get_search_results(params):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cur = conn.cursor()

        query = [
            "SELECT",
            "  e.exercise_id,",
            "  e.name AS exercise_name,",
            "  e.category,",
            "  e.difficulty,",
            "  e.muscle_groups,",
            "  e.equipment_needed,",
            "  COUNT(DISTINCT we.workout_id) AS total_workouts,",
            "  COUNT(DISTINCT w.user_id) AS total_users,",
            "  AVG(we.sets) AS avg_sets,",
            "  AVG(we.reps) AS avg_reps,",
            "  AVG(we.weight) AS avg_weight",
            "FROM exercise e",
            "LEFT JOIN workout_exercise we ON e.exercise_id = we.exercise_id",
            "LEFT JOIN workout w ON we.workout_id = w.workout_id",
            "WHERE 1=1"
        ]
        q = []
        # Filters
        if params.get('category'):
            query.append("AND e.category = %s")
            q.append(params['category'])
        if params.get('difficulty'):
            query.append("AND e.difficulty = %s")
            q.append(params['difficulty'])
        if params.get('muscle_group'):
            query.append("AND e.muscle_groups LIKE %s")
            q.append(f"%{params['muscle_group']}%")
        if params.get('start_date'):
            query.append("AND w.workout_date >= %s")
            q.append(params['start_date'])
        if params.get('end_date'):
            query.append("AND w.workout_date <= %s")
            q.append(params['end_date'])

        # Group + Having
        query.append("GROUP BY e.exercise_id, e.name, e.category, e.difficulty, e.muscle_groups, e.equipment_needed")
        having = []
        if params.get('min_users') is not None:
            having.append("COUNT(DISTINCT w.user_id) >= %s")
            q.append(params['min_users'])
        if params.get('min_avg_sets') is not None:
            having.append("AVG(we.sets) >= %s")
            q.append(params['min_avg_sets'])
        if params.get('min_avg_reps') is not None:
            having.append("AVG(we.reps) >= %s")
            q.append(params['min_avg_reps'])
        if having:
            query.append("HAVING " + " AND ".join(having))

        # Sort
        sort_map = {
            'users_desc': 'total_users DESC',
            'users_asc': 'total_users ASC',
            'avg_sets_desc': 'avg_sets DESC',
            'avg_sets_asc': 'avg_sets ASC',
            'avg_reps_desc': 'avg_reps DESC',
            'avg_reps_asc': 'avg_reps ASC',
            'name_asc': 'e.name ASC'
        }
        query.append("ORDER BY " + sort_map.get(params.get('sort_by') or 'users_desc', 'total_users DESC'))

        sql = "\n".join(query)
        cur.execute(sql, q)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except Exception:
        return None

def main():
    print_header()
    form = cgi.FieldStorage()
    params = {
        'category': (form.getvalue('category') or '').strip(),
        'difficulty': (form.getvalue('difficulty') or '').strip(),
        'muscle_group': (form.getvalue('muscle_group') or '').strip(),
        'min_users': to_int(form.getvalue('min_users')),
        'min_avg_sets': to_float(form.getvalue('min_avg_sets')),
        'min_avg_reps': to_float(form.getvalue('min_avg_reps')),
        'sort_by': (form.getvalue('sort_by') or 'users_desc').strip(),
        'start_date': to_date_str(form.getvalue('start_date')),
        'end_date': to_date_str(form.getvalue('end_date')),
    }

    results = get_search_results(params)

    print("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Exercise Performance Results - FitTrack Pro</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <h2>Exercise Performance Results</h2>
""")

    if results is None:
        print("<p><strong>Note:</strong> Database is not reachable here (GitHub). This page will work on the ClamV server once credentials are set.</p>")
    elif len(results) == 0:
        print("<p>No exercises matched your filters.</p>")
    else:
        print(f"<p>Found <strong>{len(results)}</strong> exercise(s).</p>")
        print("""
<table class="data-table" border="1">
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
        for r in results:
            print(f"""
    <tr>
      <td>{escape(r.get('exercise_name') or '')}</td>
      <td>{escape(r.get('category') or '')}</td>
      <td>{escape(r.get('difficulty') or '')}</td>
      <td>{escape(r.get('muscle_groups') or 'N/A')}</td>
      <td>{r.get('total_users') or 0}</td>
      <td>{r.get('total_workouts') or 0}</td>
      <td>{r.get('avg_sets') or 'N/A'}</td>
      <td>{r.get('avg_reps') or 'N/A'}</td>
      <td>{r.get('avg_weight') or 'N/A'}</td>
      <td><a href="exercise_detail.py?exercise_id={r.get('exercise_id')}">View Details</a></td>
    </tr>
""")
        print("""
  </tbody>
</table>
""")

    print("""
  <a href="forms/search_exercise_performance.html">Back to Search</a>
  <br><a href="forms/search_hub.html">Search Hub</a>
  <br><a href="maintenance.html">Maintenance</a>
</body>
</html>
""")

if __name__ == "__main__":
    main()
