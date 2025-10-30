#!/usr/bin/env python3
import cgi
import mysql.connector
import cgitb
cgitb.enable()

print("Content-type: text/html\n")

form = cgi.FieldStorage()
gym_name = form.getvalue("gym_name", "")
membership_type = form.getvalue("membership_type", "")

# Connect to database
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor(dictionary=True)

# Build query
query = """
SELECT u.user_id, CONCAT(u.first_name,' ',u.last_name) AS full_name,
       g.name AS gym_name, gm.membership_type, gm.start_date, gm.end_date
FROM USER u
JOIN GYM_MEMBER gm ON u.user_id = gm.user_id
JOIN GYM g ON gm.gym_id = g.gym_id
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
