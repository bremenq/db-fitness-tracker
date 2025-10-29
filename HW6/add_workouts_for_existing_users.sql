-- Add workouts for existing users (IDs: 1-10, 12, 14-30)

INSERT INTO workout (user_id, workout_name, date, duration, calories_burned, notes)
VALUES
    -- User 1
    (1, 'Morning Run', '2025-09-10', 30, 300, 'Easy pace'),
    (1, 'Gym Session', '2025-09-15', 60, 450, 'Full body'),
    (1, 'Evening Walk', '2025-09-20', 45, 200, 'Recovery'),
    (1, 'Strength Training', '2025-09-25', 55, 420, 'Upper body'),
    -- User 2
    (2, 'Strength Training', '2025-09-11', 75, 500, 'Heavy weights'),
    (2, 'Cardio Mix', '2025-09-18', 40, 380, 'Intervals'),
    (2, 'Leg Day', '2025-09-24', 70, 480, 'Squats'),
    -- User 3
    (3, 'Yoga Flow', '2025-09-12', 60, 220, 'Vinyasa'),
    (3, 'Pilates', '2025-09-19', 50, 260, 'Reformer'),
    (3, 'Stretching', '2025-09-26', 40, 180, 'Flexibility'),
    -- User 4
    (4, 'CrossFit', '2025-09-13', 60, 520, 'WOD'),
    (4, 'Running', '2025-09-21', 50, 450, '10K'),
    (4, 'Swimming', '2025-09-27', 45, 400, 'Laps'),
    -- User 5
    (5, 'Swimming', '2025-09-14', 45, 340, 'Endurance'),
    (5, 'Yoga', '2025-09-22', 50, 200, 'Relaxation'),
    (5, 'Cardio', '2025-09-28', 40, 360, 'Treadmill'),
    -- User 6
    (6, 'Boxing', '2025-09-15', 50, 480, 'Heavy bag'),
    (6, 'Core Workout', '2025-09-22', 30, 200, 'Abs'),
    (6, 'HIIT', '2025-09-29', 35, 420, 'Intense'),
    -- User 7
    (7, 'Zumba', '2025-09-16', 55, 400, 'High energy'),
    (7, 'Barre', '2025-09-23', 45, 280, 'Challenging'),
    (7, 'Dance', '2025-09-30', 50, 380, 'Fun'),
    -- User 8
    (8, 'Powerlifting', '2025-09-17', 90, 600, 'Competition'),
    (8, 'Mobility', '2025-09-24', 30, 150, 'Recovery'),
    (8, 'Heavy Lifting', '2025-10-01', 85, 580, 'Max effort'),
    -- User 9
    (9, 'Spin Class', '2025-09-18', 45, 420, 'Great class'),
    (9, 'TRX', '2025-09-25', 40, 350, 'Full body'),
    (9, 'HIIT', '2025-10-02', 35, 400, 'Intense'),
    -- User 10
    (10, 'Martial Arts', '2025-09-19', 60, 480, 'Sparring'),
    (10, 'Stretching', '2025-09-26', 30, 120, 'Flexibility'),
    (10, 'Kickboxing', '2025-10-03', 55, 500, 'Technique'),
    -- User 12
    (12, 'Morning Cardio', '2025-09-15', 45, 350, 'Great energy'),
    (12, 'Evening Yoga', '2025-09-20', 60, 200, 'Relaxing'),
    (12, 'HIIT', '2025-09-25', 30, 400, 'Intense'),
    -- User 14
    (14, 'Strength', '2025-09-16', 60, 450, 'Personal best'),
    (14, 'Leg Day', '2025-09-23', 75, 500, 'Heavy'),
    (14, 'Upper Body', '2025-09-28', 60, 420, 'Good pump'),
    -- User 15
    (15, 'Pilates', '2025-09-17', 50, 250, 'Core'),
    (15, 'Dance Cardio', '2025-09-24', 45, 380, 'Fun'),
    -- User 16
    (16, 'CrossFit', '2025-09-18', 60, 550, 'Tough'),
    (16, 'Running', '2025-09-25', 40, 400, '5K'),
    -- User 17
    (17, 'Swimming', '2025-09-19', 45, 320, 'Laps'),
    (17, 'Cycling', '2025-09-26', 60, 450, 'Outdoor'),
    -- User 18
    (18, 'Boxing', '2025-09-20', 50, 480, 'Heavy bag'),
    (18, 'Core', '2025-09-27', 30, 200, 'Abs'),
    -- User 19
    (19, 'Zumba', '2025-09-21', 55, 400, 'Energy'),
    (19, 'Barre', '2025-09-28', 45, 280, 'Challenge'),
    -- User 20
    (20, 'Powerlifting', '2025-09-22', 90, 600, 'Competition'),
    (20, 'Mobility', '2025-09-29', 30, 150, 'Recovery'),
    -- User 21 (emma.wilson)
    (21, 'Morning Cardio', '2025-09-15', 45, 350, 'Great energy'),
    (21, 'Evening Yoga', '2025-09-20', 60, 200, 'Relaxing'),
    (21, 'HIIT', '2025-09-25', 30, 400, 'Intense'),
    -- User 22 (michael.brown)
    (22, 'Strength Training', '2025-09-16', 60, 450, 'Personal best'),
    (22, 'Leg Day', '2025-09-23', 75, 500, 'Heavy squats'),
    (22, 'Upper Body', '2025-09-28', 60, 420, 'Good pump'),
    -- User 23 (sophia.davis)
    (23, 'Pilates', '2025-09-17', 50, 250, 'Core focused'),
    (23, 'Dance Cardio', '2025-09-24', 45, 380, 'Fun class'),
    -- User 24 (james.miller)
    (24, 'CrossFit WOD', '2025-09-18', 60, 550, 'Tough'),
    (24, 'Running', '2025-09-25', 40, 400, '5K run'),
    -- User 25 (olivia.garcia)
    (25, 'Swimming', '2025-09-19', 45, 320, 'Lap swimming'),
    (25, 'Cycling', '2025-09-26', 60, 450, 'Outdoor ride'),
    -- User 26 (william.martinez)
    (26, 'Boxing', '2025-09-20', 50, 480, 'Heavy bag'),
    (26, 'Core Workout', '2025-09-27', 30, 200, 'Ab focused'),
    -- User 27 (ava.rodriguez)
    (27, 'Zumba', '2025-09-21', 55, 400, 'High energy'),
    (27, 'Barre', '2025-09-28', 45, 280, 'Challenging'),
    -- User 28 (ethan.hernandez)
    (28, 'Powerlifting', '2025-09-22', 90, 600, 'Competition prep'),
    (28, 'Mobility Work', '2025-09-29', 30, 150, 'Recovery'),
    -- User 29 (isabella.lopez)
    (29, 'Spin Class', '2025-09-23', 45, 420, 'Great instructor'),
    (29, 'TRX Training', '2025-09-30', 40, 350, 'Full body'),
    -- User 30 (alexander.gonzalez)
    (30, 'Martial Arts', '2025-09-24', 60, 480, 'Sparring'),
    (30, 'Stretching', '2025-10-01', 30, 120, 'Flexibility');

COMMIT;

SELECT 'Workouts added successfully!' as status;
SELECT COUNT(*) as total_workouts FROM workout;
SELECT user_type, COUNT(DISTINCT u.user_id) as user_count, COUNT(w.workout_id) as workout_count
FROM user u
LEFT JOIN gym_member gm ON u.user_id = gm.user_id
LEFT JOIN staff s ON u.user_id = s.user_id
LEFT JOIN workout w ON u.user_id = w.user_id
WHERE u.user_id IN (1,2,3,4,5,6,7,8,9,10,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
GROUP BY CASE 
    WHEN gm.user_id IS NOT NULL THEN 'Gym Member'
    WHEN s.user_id IS NOT NULL THEN 'Staff'
    ELSE 'Individual'
END;

