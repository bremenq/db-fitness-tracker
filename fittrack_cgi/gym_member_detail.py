#!/usr/bin/env python3
import cgi
import mysql.connector
import cgitb
cgitb.enable()

print("Content-type: text/html\n")

form = cgi.FieldStorage()
user_id = form.getvalue("user_id")

if not user_id:
    print("<html><body><p>No member selected.</p></body></html>")
    exit()

# Connect to database
conn = mysql.connector.connect(
    host="localhost",
    user="silee",
    password="21tB6ZF25rowHtCl",
    database="db_silee"
)
cursor = conn.cursor(dictionary=True)

query = """
SELECT u.user_id, u.first_name, u.last_name, u.email, u.date_of_birth,
       g.name AS gym_name, g.address, gm.membership_type, gm.start_date, gm.end_date
FROM USER u
JOIN GYM_MEMBER gm ON u.user_id = gm.user_id
JOIN GYM g ON gm.gym_id = g.gym_id
WHERE u.user_id = %s
"""
cursor.execute(query, (user_id,))
member = cursor.fetchone()
conn.close()

print("""
<html>
<head>
    <title>Gym Member Detail</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
""")

if member:
    print(f"<h2>{member['first_name']} {member['last_name']}</h2>")
    print("<ul>")
    print(f"<li>Email: {member['email']}</li>")
    print(f"<li>Date of Birth: {member['date_of_birth']}</li>")
    print(f"<li>Gym: {member['gym_name']} - {member['address']}</li>")
    print(f"<li>Membership Type: {member['membership_type']}</li>")
    print(f"<li>Start Date: {member['start_date']}</li>")
    print(f"<li>End Date: {member['end_date']}</li>")
    print("</ul>")
else:
    print("<p>Member not found.</p>")

print('<a href="forms/search_gym_members.html">Back to Search</a>')
print('<br><a href="maintenance.html">Back to Maintenance</a>')
print("</body></html>")
