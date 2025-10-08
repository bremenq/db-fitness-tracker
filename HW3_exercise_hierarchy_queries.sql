SELECT e.exercise_id,e.name,
       COUNT(*) AS sessions,
       COUNT(DISTINCT w.user_id) AS unique_users
FROM workout_exercise we
JOIN workout  w ON w.workout_id=we.workout_id
JOIN exercise e ON e.exercise_id=we.exercise_id
JOIN cardio   c ON c.exercise_id=e.exercise_id
WHERE w.date >= (CURDATE() - INTERVAL 30 DAY)
GROUP BY e.exercise_id,e.name
HAVING sessions>=1
ORDER BY sessions DESC,unique_users DESC,e.name;

SELECT YEARWEEK(w.date,3) AS iso_yearweek,
       u.gender,
       e.exercise_id,e.name,
       SUM(COALESCE(we.sets,0)*COALESCE(we.reps,0)*COALESCE(we.weight,0)) AS total_volume
FROM workout_exercise we
JOIN workout  w ON w.workout_id=we.workout_id
JOIN `user`   u ON u.user_id=w.user_id
JOIN exercise e ON e.exercise_id=we.exercise_id
JOIN strength s ON s.exercise_id=e.exercise_id
WHERE w.date >= (CURDATE() - INTERVAL 56 DAY)
GROUP BY iso_yearweek,u.gender,e.exercise_id,e.name
HAVING total_volume>0
ORDER BY iso_yearweek DESC,total_volume DESC;

SELECT u.user_id,
       CONCAT(u.first_name,' ',u.last_name) AS user_name,
       COUNT(*) AS hi_sessions,
       MAX(w.date) AS last_session_date
FROM workout_exercise we
JOIN workout  w ON w.workout_id=we.workout_id
JOIN `user`   u ON u.user_id=w.user_id
JOIN exercise e ON e.exercise_id=we.exercise_id
JOIN cardio   c ON c.exercise_id=e.exercise_id
WHERE w.date >= (CURDATE() - INTERVAL 30 DAY)
  AND c.target_heart_rate>180
GROUP BY u.user_id,user_name
HAVING hi_sessions>=4
ORDER BY hi_sessions DESC,last_session_date DESC;
