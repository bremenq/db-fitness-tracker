


import cgi
import pymysql  
import cgitb
cgitb.enable()

print("Content-Type: text/html\n")


form = cgi.FieldStorage()
gym_name = form.getvalue("gym_name", "")
membership_type = form.getvalue("membership_type", "")


try:
    conn = pymysql.connect(
        host="localhost",
        user="****",        
        password="****",     
        database="****",   
        cursorclass=pymysql.cursors.DictCursor
    )
except Exception as e:
    print(f"<h3>Database connection failed: {e}</h3>")
    exit()

cursor = conn.cursor()


query = """
SELECT u.user_id, CONCAT(u.first_name, ' ', u.last_name) AS full_name,
       g.name AS gym_name, gm.membership_type, gm.start_date, gm.end_date
FROM user u
JOIN gym_member gm ON u.user_id = gm.user_id
JOIN gym g ON gm.gym_id = g.gym_id
WHERE (%s = '' OR g.name LIKE %s)
  AND (%s = '' OR gm.membership_type = %s)
ORDER BY g.name, full_name
"""

cursor.execute(query, (gym_name, f"%{gym_name}%", membership_type, membership_type))
results = cursor.fetchall()
conn.close()


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
        print(f'<li><a href="member_detail.py?user_id={row["user_id"]}">{row["full_name"]}</a> - {row["gym_name"]} ({row["membership_type"]})</li>')
    print("</ul>")
else:
    print("<p>No results found for the given filters.</p>")

print("""
    <br>
    <a href="search_user_activity.py">🔙 Back to Search</a>
</body>
</html>
""")
