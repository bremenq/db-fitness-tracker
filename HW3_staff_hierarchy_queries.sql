-- Query 1: List all Gym Members with their Gym details
SELECT 
    u.user_id,
    CONCAT(u.first_name, ' ', u.last_name) AS full_name,
    g.name AS gym_name,
    gm.membership_type,
    gm.start_date,
    gm.end_date
FROM USER u
JOIN GYM_MEMBER gm ON u.user_id = gm.user_id
JOIN GYM g ON gm.gym_id = g.gym_id
ORDER BY g.name, full_name;


-- Query 2: Count how many users belong to each gender
SELECT 
    gender,
    COUNT(user_id) AS total_users
FROM USER
GROUP BY gender
HAVING COUNT(user_id) > 0;



-- Query 3: Find staff members who manage the most members in their gym
SELECT 
    g.gym_id,
    g.name AS gym_name,
    CONCAT(u_s.first_name, ' ', u_s.last_name) AS manager_name,
    COUNT(gm.user_id) AS total_members
FROM STAFF s
JOIN USER u_s ON s.user_id = u_s.user_id
JOIN GYM g ON s.gym_id = g.gym_id
JOIN GYM_MEMBER gm ON gm.gym_id = g.gym_id
WHERE s.position = 'Manager'
GROUP BY g.gym_id, s.user_id, u_s.first_name, u_s.last_name
HAVING COUNT(gm.user_id) = (
    SELECT MAX(member_count)
    FROM (
        SELECT COUNT(gm2.user_id) AS member_count
        FROM STAFF s2
        JOIN GYM_MEMBER gm2 ON s2.gym_id = gm2.gym_id
        WHERE s2.position = 'Manager'
        GROUP BY s2.user_id
    ) AS subquery
);


