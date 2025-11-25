#!/usr/bin/python3
print('Content-Type: application/json; charset=utf-8')
print()

import cgi
import pymysql
import json
import sys

DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': '****',
    'database': 'db_your_username',
    'charset': 'utf8mb4'
}

def search_users(term):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        sql = """
            SELECT user_id, first_name, last_name, email 
            FROM user 
            WHERE CONCAT(first_name, ' ', last_name) LIKE %s 
               OR email LIKE %s 
            ORDER BY first_name, last_name 
            LIMIT 20
        """
        search_term = f'%{term}%'
        cursor.execute(sql, (search_term, search_term))
        results = [
            {
                'id': row[0], 
                'value': f'{row[1]} {row[2]}', 
                'label': f'{row[1]} {row[2]} ({row[3]})'
            }
            for row in cursor.fetchall()
        ]
        cursor.close()
        conn.close()
        return results
    except Exception as e:
        return []

def search_gyms(term):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        sql = """
            SELECT gym_id, name, address 
            FROM gym 
            WHERE name LIKE %s OR address LIKE %s 
            ORDER BY name 
            LIMIT 20
        """
        search_term = f'%{term}%'
        cursor.execute(sql, (search_term, search_term))
        results = [
            {
                'id': row[0], 
                'value': row[1], 
                'label': f'{row[1]} - {row[2]}'
            }
            for row in cursor.fetchall()
        ]
        cursor.close()
        conn.close()
        return results
    except Exception as e:
        return []

def search_exercises(term):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        sql = """
            SELECT exercise_id, name, category 
            FROM exercise 
            WHERE name LIKE %s OR category LIKE %s 
            ORDER BY name 
            LIMIT 20
        """
        search_term = f'%{term}%'
        cursor.execute(sql, (search_term, search_term))
        results = [
            {
                'id': row[0], 
                'value': row[1], 
                'label': f'{row[1]} ({row[2]})'
            }
            for row in cursor.fetchall()
        ]
        cursor.close()
        conn.close()
        return results
    except Exception as e:
        return []

def search_workouts(term):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        sql = """
            SELECT workout_id, workout_name, date 
            FROM workout 
            WHERE workout_name LIKE %s 
            ORDER BY date DESC 
            LIMIT 20
        """
        search_term = f'%{term}%'
        cursor.execute(sql, (search_term,))
        results = [
            {
                'id': row[0], 
                'value': row[1], 
                'label': f'{row[1]} ({row[2]})'
            }
            for row in cursor.fetchall()
        ]
        cursor.close()
        conn.close()
        return results
    except Exception as e:
        return []

def search_classes(term):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        sql = """
            SELECT class_id, name, schedule_time 
            FROM class 
            WHERE name LIKE %s 
            ORDER BY schedule_time DESC 
            LIMIT 20
        """
        search_term = f'%{term}%'
        cursor.execute(sql, (search_term,))
        results = [
            {
                'id': row[0], 
                'value': row[1], 
                'label': f'{row[1]} ({row[2]})'
            }
            for row in cursor.fetchall()
        ]
        cursor.close()
        conn.close()
        return results
    except Exception as e:
        return []

form = cgi.FieldStorage()
data_type = form.getvalue('type', '')
term = form.getvalue('term', '')

try:
    if data_type == 'users':
        results = search_users(term)
    elif data_type == 'gyms':
        results = search_gyms(term)
    elif data_type == 'exercises':
        results = search_exercises(term)
    elif data_type == 'workouts':
        results = search_workouts(term)
    elif data_type == 'classes':
        results = search_classes(term)
    else:
        results = []
    
    print(json.dumps(results, indent=2))
except Exception as e:
    print(json.dumps({'error': str(e)}))


