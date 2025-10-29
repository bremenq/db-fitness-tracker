Executing command on clabsql.clamv.constructor.university: cat ~/public_html/get_data.py
#!/usr/bin/python3
import cgi
import pymysql
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pymysql'))

DB_CONFIG = {
    'host': 'localhost',
    'user': 'azinovev',
    'password': 'WrtqlLcpgCPs0KGY',
    'database': 'db_azinovev'
}

def get_users():
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('SELECT user_id, first_name, last_name, email FROM user ORDER BY first_name, last_name')
    users = [{'id': row[0], 'name': f'{row[1]} {row[2]}', 'email': row[3]} for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return users

def get_gyms():
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('SELECT gym_id, name, address FROM gym ORDER BY name')
    gyms = [{'id': row[0], 'name': row[1], 'address': row[2]} for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return gyms

def get_exercises():
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('SELECT exercise_id, name, category FROM exercise ORDER BY name')
    exercises = [{'id': row[0], 'name': row[1], 'category': row[2]} for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return exercises

def get_workouts():
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('SELECT workout_id, workout_name, date FROM workout ORDER BY date DESC LIMIT 50')
    workouts = [{'id': row[0], 'name': row[1], 'date': str(row[2])} for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return workouts

def get_classes():
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('SELECT class_id, name, schedule_time FROM class ORDER BY schedule_time DESC LIMIT 50')
    classes = [{'id': row[0], 'name': row[1], 'time': str(row[2])} for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return classes

def main():
    print('Content-Type: application/json; charset=utf-8')
    print('Access-Control-Allow-Origin: *')
    print()
    
    form = cgi.FieldStorage()
    data_type = form.getvalue('type', 'users')
    
    try:
        if data_type == 'users':
            data = get_users()
        elif data_type == 'gyms':
            data = get_gyms()
        elif data_type == 'exercises':
            data = get_exercises()
        elif data_type == 'workouts':
            data = get_workouts()
        elif data_type == 'classes':
            data = get_classes()
        else:
            data = {'error': 'Invalid type'}
        
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(json.dumps({'error': str(e)}))

if __name__ == '__main__':
    main()
