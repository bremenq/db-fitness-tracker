#!/usr/bin/env python3
# ISSUE: Wrong Python library - should use pymysql, not mysql.connector
# See search_user_activity.py for correct pattern
import cgi
import mysql.connector  # ❌ WRONG: Use pymysql instead
import cgitb
cgitb.enable()

print("Content-type: text/html\n")

form = cgi.FieldStorage()
gym_name = form.getvalue("gym_name", "")
membership_type = form.getvalue("membership_type", "")

# Connect to database
# ❌ ISSUE: Wrong library and exposed credentials
# Should use pymysql.connect() and mask password with ****
conn = mysql.connector.connect(
     host="localhost",
    user="enter_username",  # ❌ Should be masked in repo
    password="enter_password",  # ❌ SECURITY: Mask with **** in repo
    database="enter_database name"  # ❌ Should be masked in repo
)
cursor = conn.cursor(dictionary=True)

# Build query
# ❌ CRITICAL: Table names are WRONG - SQL is case-sensitive on our server
# Our schema from HW2 uses lowercase: user, gym, gym_member (not USER, GYM, GYM_MEMBER)
# Check fittrack_schema.sql for correct table names
query = """
SELECT u.user_id, CONCAT(u.first_name,' ',u.last_name) AS full_name,
       g.name AS gym_name, gm.membership_type, gm.start_date, gm.end_date
FROM USER u  -- ❌ WRONG: Should be 'user' (lowercase)
JOIN GYM_MEMBER gm ON u.user_id = gm.user_id  -- ❌ WRONG: Should be 'gym_member'
JOIN GYM g ON gm.gym_id = g.gym_id  -- ❌ WRONG: Should be 'gym'
WHERE (%s = '' OR g.name LIKE %s)
  AND (%s = '' OR gm.membership_type = %s)
ORDER BY g.name, full_name
"""
cursor.execute(query, (gym_name, f"%{gym_name}%", membership_type, membership_type))
results = cursor.fetchall()
conn.close()

# Generate HTML
print("""
<html>
<head>
    <title>Gym Members Results</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <h2>Search Results</h2>
""")

if results:
    print("<ul>")
    for row in results:
        print(f'<li><a href="gym_member_detail.py?user_id={row["user_id"]}">{row["full_name"]}</a> - {row["gym_name"]} ({row["membership_type"]})</li>')
    print("</ul>")
else:
    print("<p>No gym members found.</p>")

print('<a href="forms/search_gym_members.html">Back to Search</a>')
print('<br><a href="maintenance.html">Back to Maintenance</a>')
print("</body></html>")
