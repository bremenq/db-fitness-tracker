


import cgi
import pymysql  
import cgitb
cgitb.enable()


form = cgi.FieldStorage()
user_id = form.getvalue("user_id")

if not user_id:
    print("Content-Type: text/html\n")
    print("<h3>Error: No user_id provided.</h3>")
    exit()


try:
    conn = pymysql.connect(
        host="localhost",
        user="****",         
        password="****",     
        database="****",     
        cursorclass=pymysql.cursors.DictCursor
    )
except Exception as e:
    print("Content-Type: text/html\n")
    print(f"<h3>Database connection failed: {e}</h3>")
    exit()

cursor = conn.cursor()


query = """
SELECT u.user_id, u.first_name, u.last_name, u.email, u.date_of_birth,
       g.name AS gym_name, g.address, gm.membership_type, gm.start_date, gm.end_date
FROM user u
JOIN gym_member gm ON u.user_id = gm.user_id
JOIN gym g ON gm.gym_id = g.gym_id
WHERE u.user_id = %s
"""

cursor.execute(query, (user_id,))
member = cursor.fetchone()
conn.close()


print("Content-Type: text/html\n")
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
    print("<h3>No member found with that ID.</h3>")

print("</body></html>")
