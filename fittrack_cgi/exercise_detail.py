#!/usr/bin/python3
import pymysql
import cgi
import cgitb
from html import escape

cgitb.enable()

# ====== We have to fill on these later because i cannot connect to the server ======
DB_CONFIG = {
    'host': 'localhost',
    'user': 'aharslan',         
    'password': 'WrtqlLcpgCPs0KGY',     
    'database': 'db_aharslan',   
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}
# ==========================================================================

def print_header():
    print("Content-Type: text/html; charset=utf-8\n")

def main():
    print_header()
    form = cgi.FieldStorage()
    exercise_id = form.getvalue("exercise_id")

    print("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Exercise Detail - FitTrack Pro</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="header-content">
      <a href="index.html"><img src="img/fittrack-pro-logo.svg" alt="FitTrack Pro Logo" class="logo"></a>
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
""")

    if not exercise_id:
        print("<p><strong>Error:</strong> No exercise selected.</p>")
        print("</div></main></body></html>")
        return

    try:
        conn = pymysql.connect(**DB_CONFIG)
        cur = conn.cursor()

        # 1) Basic exercise info (keep columns you actually have)
        cur.execute("""
            SELECT
              e.exercise_id,
              e.name AS exercise_name,
              e.category,
              e.difficulty,
              e.muscle_groups,
              e.equipment_needed
            FROM exercise e
            WHERE e.exercise_id = %s
        """, (exercise_id,))
        exercise = cur.fetchone()

        # 2) Aggregated stats across all sessions for this exercise
        cur.execute("""
            SELECT
              COUNT(DISTINCT we.workout_id) AS total_workouts,
              COUNT(DISTINCT w.user_id)     AS total_users,
              AVG(we.sets)                  AS avg_sets,
              AVG(we.reps)                  AS avg_reps,
              AVG(we.weight)                AS avg_weight
            FROM workout_exercise we
            LEFT JOIN workout w ON we.workout_id = w.workout_id
            WHERE we.exercise_id = %s
        """, (exercise_id,))
        stats = cur.fetchone()

        # 3) Session history (latest first)
        cur.execute("""
            SELECT
              w.workout_id,
              w.workout_date,
              u.user_id,
              CONCAT(u.first_name, ' ', u.last_name) AS user_name,
              we.sets,
              we.reps,
              we.weight
            FROM workout_exercise we
            JOIN workout w ON we.workout_id = w.workout_id
            JOIN user u     ON w.user_id    = u.user_id
            WHERE we.exercise_id = %s
            ORDER BY w.workout_date DESC, w.workout_id DESC
            LIMIT 500
        """, (exercise_id,))
        sessions = cur.fetchall()

        cur.close()
        conn.close()
    except Exception as e:
        # Minimal error surface on production; cgitb will show traceback if enabled server-side
        print("<p><strong>Error:</strong> Could not load exercise details. (DB unreachable or misconfigured)</p>")
        print("</div></main></body></html>")
        return

    if not exercise:
        print("<p>Exercise not found.</p>")
        print("</div></main></body></html>")
        return

    # Render exercise overview
    ex_name = escape(exercise.get("exercise_name") or "")
    category = escape(exercise.get("category") or "—")
    difficulty = escape(exercise.get("difficulty") or "—")
    muscles = escape(exercise.get("muscle_groups") or "—")
    equip = escape(exercise.get("equipment_needed") or "—")

    total_workouts = stats.get("total_workouts") if stats and stats.get("total_workouts") is not None else 0
    total_users    = stats.get("total_users")    if stats and stats.get("total_users")    is not None else 0
    avg_sets       = f"{stats.get('avg_sets'):.1f}"   if stats and stats.get("avg_sets")   is not None else "N/A"
    avg_reps       = f"{stats.get('avg_reps'):.1f}"   if stats and stats.get("avg_reps")   is not None else "N/A"
    avg_weight     = f"{stats.get('avg_weight'):.1f}" if stats and stats.get("avg_weight") is not None else "N/A"

    print(f"""
      <h2>{ex_name}</h2>
      <div class="card">
        <ul>
          <li><strong>Category:</strong> {category}</li>
          <li><strong>Difficulty:</strong> {difficulty}</li>
          <li><strong>Muscle Groups:</strong> {muscles}</li>
          <li><strong>Equipment Needed:</strong> {equip}</li>
        </ul>
      </div>

      <h3>Overview Stats</h3>
      <div class="card">
        <ul>
          <li><strong>Total Users:</strong> {total_users}</li>
          <li><strong>Total Workouts:</strong> {total_workouts}</li>
          <li><strong>Average Sets:</strong> {avg_sets}</li>
          <li><strong>Average Reps:</strong> {avg_reps}</li>
          <li><strong>Average Weight:</strong> {avg_weight}</li>
        </ul>
      </div>

      <h3>Session History</h3>
    """)

    if sessions:
        print("""
      <div class="results-table">
        <table class="data-table">
          <thead>
            <tr>
              <th>Date</th>
              <th>User</th>
              <th>Sets</th>
              <th>Reps</th>
              <th>Weight</th>
            </tr>
          </thead>
          <tbody>
        """)
        for s in sessions:
            date = escape(str(s.get("workout_date") or ""))
            user_id = s.get("user_id")
            user_name = escape(s.get("user_name") or "")
            sets = escape(str(s.get("sets") if s.get("sets") is not None else "—"))
            reps = escape(str(s.get("reps") if s.get("reps") is not None else "—"))
            weight = escape(str(s.get("weight") if s.get("weight") is not None else "—"))
            user_link = f"user_detail.py?user_id={user_id}" if user_id is not None else "#"

            print(f"""
            <tr>
              <td>{date}</td>
              <td><a href="{user_link}">{user_name}</a></td>
              <td>{sets}</td>
              <td>{reps}</td>
              <td>{weight}</td>
            </tr>
            """)

        print("""
          </tbody>
        </table>
      </div>
        """)
    else:
        print("<p>No sessions recorded for this exercise yet.</p>")

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
