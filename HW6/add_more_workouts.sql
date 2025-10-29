-- Add more workouts for existing users to test search functionality
-- This assumes users with IDs 1-28 exist

-- Add workouts for users 1-10
INSERT INTO workout (user_id, workout_name, date, duration, calories_burned, notes)
VALUES
    -- User 1
    (1, 'Morning Run', '2025-09-10', 30, 300, 'Easy pace'),
    (1, 'Gym Session', '2025-09-15', 60, 450, 'Full body'),
    (1, 'Evening Walk', '2025-09-20', 45, 200, 'Recovery'),
    (1, 'Strength Training', '2025-09-25', 55, 420, 'Upper body focus'),
    (1, 'Cardio Mix', '2025-09-30', 40, 380, 'Interval training'),
    -- User 2
    (2, 'Strength Training', '2025-09-11', 75, 500, 'Heavy weights'),
    (2, 'Cardio Mix', '2025-09-18', 40, 380, 'Interval training'),
    (2, 'Leg Day', '2025-09-24', 70, 480, 'Squats and lunges'),
    (2, 'Full Body', '2025-10-01', 65, 460, 'Complete workout'),
    -- User 3
    (3, 'Yoga Flow', '2025-09-12', 60, 220, 'Vinyasa style'),
    (3, 'Pilates', '2025-09-19', 50, 260, 'Reformer class'),
    (3, 'Stretching', '2025-09-26', 40, 180, 'Flexibility'),
    (3, 'Meditation', '2025-10-02', 30, 100, 'Mindfulness'),
    -- User 4
    (4, 'CrossFit', '2025-09-13', 60, 520, 'Benchmark WOD'),
    (4, 'Running', '2025-09-21', 50, 450, '10K training'),
    (4, 'Swimming', '2025-09-27', 45, 400, 'Lap swimming'),
    (4, 'Cycling', '2025-10-03', 55, 480, 'Hill training'),
    -- User 5
    (5, 'Swimming', '2025-09-14', 45, 340, 'Endurance training'),
    (5, 'Yoga', '2025-09-22', 50, 200, 'Relaxation'),
    (5, 'Cardio', '2025-09-28', 40, 360, 'Treadmill run'),
    (5, 'Strength', '2025-10-04', 60, 440, 'Weight training'),
    -- User 6
    (6, 'Boxing', '2025-09-15', 50, 480, 'Heavy bag work'),
    (6, 'Core Workout', '2025-09-22', 30, 200, 'Ab focused'),
    (6, 'HIIT', '2025-09-29', 35, 420, 'High intensity'),
    -- User 7
    (7, 'Zumba', '2025-09-16', 55, 400, 'High energy'),
    (7, 'Barre', '2025-09-23', 45, 280, 'Challenging'),
    (7, 'Dance Fitness', '2025-09-30', 50, 380, 'Fun workout'),
    -- User 8
    (8, 'Powerlifting', '2025-09-17', 90, 600, 'Competition prep'),
    (8, 'Mobility Work', '2025-09-24', 30, 150, 'Recovery day'),
    (8, 'Heavy Lifting', '2025-10-01', 85, 580, 'Max effort'),
    -- User 9
    (9, 'Spin Class', '2025-09-18', 45, 420, 'Great instructor'),
    (9, 'TRX Training', '2025-09-25', 40, 350, 'Full body'),
    (9, 'HIIT', '2025-10-02', 35, 400, 'High intensity'),
    -- User 10
    (10, 'Martial Arts', '2025-09-19', 60, 480, 'Sparring session'),
    (10, 'Stretching', '2025-09-26', 30, 120, 'Flexibility work'),
    (10, 'Kickboxing', '2025-10-03', 55, 500, 'Technique practice');

-- Add workouts for users 11-20
INSERT INTO workout (user_id, workout_name, date, duration, calories_burned, notes)
VALUES
    (11, 'Morning Cardio', '2025-09-15', 45, 350, 'Great energy'),
    (11, 'Evening Yoga', '2025-09-20', 60, 200, 'Relaxing'),
    (11, 'HIIT Training', '2025-09-25', 30, 400, 'Intense'),
    (12, 'Strength Training', '2025-09-16', 60, 450, 'Personal best'),
    (12, 'Leg Day', '2025-09-23', 75, 500, 'Heavy squats'),
    (12, 'Upper Body', '2025-09-28', 60, 420, 'Good pump'),
    (13, 'Pilates', '2025-09-17', 50, 250, 'Core focused'),
    (13, 'Dance Cardio', '2025-09-24', 45, 380, 'Fun class'),
    (14, 'CrossFit WOD', '2025-09-18', 60, 550, 'Tough'),
    (14, 'Running', '2025-09-25', 40, 400, '5K run'),
    (15, 'Swimming', '2025-09-19', 45, 320, 'Lap swimming'),
    (15, 'Cycling', '2025-09-26', 60, 450, 'Outdoor ride'),
    (16, 'Boxing', '2025-09-20', 50, 480, 'Heavy bag'),
    (16, 'Core Workout', '2025-09-27', 30, 200, 'Ab work'),
    (17, 'Zumba', '2025-09-21', 55, 400, 'High energy'),
    (17, 'Barre', '2025-09-28', 45, 280, 'Challenging'),
    (18, 'Powerlifting', '2025-09-22', 90, 600, 'Competition'),
    (18, 'Mobility', '2025-09-29', 30, 150, 'Recovery'),
    (19, 'Spin Class', '2025-09-23', 45, 420, 'Great class'),
    (19, 'TRX', '2025-09-30', 40, 350, 'Full body'),
    (20, 'Martial Arts', '2025-09-24', 60, 480, 'Sparring'),
    (20, 'Stretching', '2025-10-01', 30, 120, 'Flexibility');

-- Add workouts for users 21-28
INSERT INTO workout (user_id, workout_name, date, duration, calories_burned, notes)
VALUES
    (21, 'Morning Run', '2025-09-15', 35, 320, 'Easy pace'),
    (21, 'Gym Session', '2025-09-22', 55, 430, 'Full body'),
    (22, 'Yoga', '2025-09-16', 50, 210, 'Relaxing'),
    (22, 'Strength', '2025-09-23', 60, 440, 'Upper body'),
    (23, 'Cardio', '2025-09-17', 40, 370, 'Intervals'),
    (23, 'Swimming', '2025-09-24', 45, 350, 'Endurance'),
    (24, 'CrossFit', '2025-09-18', 55, 510, 'WOD'),
    (24, 'Running', '2025-09-25', 45, 420, '8K'),
    (25, 'Boxing', '2025-09-19', 50, 470, 'Training'),
    (25, 'HIIT', '2025-09-26', 35, 410, 'Intense'),
    (26, 'Pilates', '2025-09-20', 50, 240, 'Core'),
    (26, 'Dance', '2025-09-27', 45, 370, 'Fun'),
    (27, 'Strength', '2025-09-21', 70, 490, 'Heavy'),
    (27, 'Cardio', '2025-09-28', 40, 360, 'Mix'),
    (28, 'Yoga', '2025-09-22', 55, 200, 'Flow'),
    (28, 'Swimming', '2025-09-29', 45, 330, 'Laps');

COMMIT;

SELECT 'Workouts added successfully!' as status;
SELECT COUNT(*) as total_workouts FROM workout;

