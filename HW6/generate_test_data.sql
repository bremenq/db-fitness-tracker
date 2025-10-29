-- Generate more test data for FitTrack Pro
-- This script adds more users, workouts, and related data for testing search functionality

-- Add more individual users
INSERT INTO user (username, email, password_hash, first_name, last_name, date_of_birth, gender)
VALUES 
    ('emma.wilson', 'emma.wilson@email.com', 'hash123', 'Emma', 'Wilson', '1995-03-15', 'Female'),
    ('michael.brown', 'michael.brown@email.com', 'hash123', 'Michael', 'Brown', '1988-07-22', 'Male'),
    ('sophia.davis', 'sophia.davis@email.com', 'hash123', 'Sophia', 'Davis', '1992-11-30', 'Female'),
    ('james.miller', 'james.miller@email.com', 'hash123', 'James', 'Miller', '1985-05-18', 'Male'),
    ('olivia.garcia', 'olivia.garcia@email.com', 'hash123', 'Olivia', 'Garcia', '1998-09-25', 'Female'),
    ('william.martinez', 'william.martinez@email.com', 'hash123', 'William', 'Martinez', '1990-12-08', 'Male'),
    ('ava.rodriguez', 'ava.rodriguez@email.com', 'hash123', 'Ava', 'Rodriguez', '1994-02-14', 'Female'),
    ('ethan.hernandez', 'ethan.hernandez@email.com', 'hash123', 'Ethan', 'Hernandez', '1987-06-20', 'Male'),
    ('isabella.lopez', 'isabella.lopez@email.com', 'hash123', 'Isabella', 'Lopez', '1996-08-11', 'Female'),
    ('alexander.gonzalez', 'alexander.gonzalez@email.com', 'hash123', 'Alexander', 'Gonzalez', '1991-04-03', 'Male');

-- Get the IDs of newly inserted users (assuming sequential IDs)
SET @emma_id = LAST_INSERT_ID();
SET @michael_id = @emma_id + 1;
SET @sophia_id = @emma_id + 2;
SET @james_id = @emma_id + 3;
SET @olivia_id = @emma_id + 4;
SET @william_id = @emma_id + 5;
SET @ava_id = @emma_id + 6;
SET @ethan_id = @emma_id + 7;
SET @isabella_id = @emma_id + 8;
SET @alexander_id = @emma_id + 9;

-- Add more workouts for new users
INSERT INTO workout (user_id, workout_name, date, duration, calories_burned, notes)
VALUES
    -- Workouts for new users
    (@emma_id, 'Morning Cardio', '2025-09-15', 45, 350, 'Great energy today'),
    (@emma_id, 'Evening Yoga', '2025-09-20', 60, 200, 'Relaxing session'),
    (@emma_id, 'HIIT Training', '2025-09-25', 30, 400, 'Intense workout'),
    (@emma_id, 'Strength Training', '2025-09-28', 50, 380, 'Building muscle'),
    (@michael_id, 'Strength Training', '2025-09-16', 60, 450, 'Personal best on bench press'),
    (@michael_id, 'Leg Day', '2025-09-23', 75, 500, 'Heavy squats'),
    (@michael_id, 'Upper Body', '2025-09-28', 60, 420, 'Good pump'),
    (@michael_id, 'Full Body', '2025-10-02', 70, 480, 'Complete workout'),
    (@sophia_id, 'Pilates', '2025-09-17', 50, 250, 'Core focused'),
    (@sophia_id, 'Dance Cardio', '2025-09-24', 45, 380, 'Fun class'),
    (@sophia_id, 'Yoga Flow', '2025-09-29', 55, 220, 'Flexibility work'),
    (@james_id, 'CrossFit WOD', '2025-09-18', 60, 550, 'Tough but rewarding'),
    (@james_id, 'Running', '2025-09-25', 40, 400, '5K run'),
    (@james_id, 'Swimming', '2025-10-01', 50, 420, 'Endurance training'),
    (@olivia_id, 'Swimming', '2025-09-19', 45, 320, 'Lap swimming'),
    (@olivia_id, 'Cycling', '2025-09-26', 60, 450, 'Outdoor ride'),
    (@olivia_id, 'Yoga', '2025-10-03', 50, 200, 'Relaxation'),
    (@william_id, 'Boxing', '2025-09-20', 50, 480, 'Heavy bag work'),
    (@william_id, 'Core Workout', '2025-09-27', 30, 200, 'Ab focused'),
    (@william_id, 'Cardio Mix', '2025-10-04', 45, 400, 'Interval training'),
    (@ava_id, 'Zumba', '2025-09-21', 55, 400, 'High energy'),
    (@ava_id, 'Barre', '2025-09-28', 45, 280, 'Challenging'),
    (@ava_id, 'Dance Fitness', '2025-10-05', 50, 380, 'Fun workout'),
    (@ethan_id, 'Powerlifting', '2025-09-22', 90, 600, 'Competition prep'),
    (@ethan_id, 'Mobility Work', '2025-09-29', 30, 150, 'Recovery day'),
    (@ethan_id, 'Heavy Lifting', '2025-10-06', 85, 580, 'Max effort'),
    (@isabella_id, 'Spin Class', '2025-09-23', 45, 420, 'Great instructor'),
    (@isabella_id, 'TRX Training', '2025-09-30', 40, 350, 'Full body'),
    (@isabella_id, 'HIIT', '2025-10-07', 35, 400, 'High intensity'),
    (@alexander_id, 'Martial Arts', '2025-09-24', 60, 480, 'Sparring session'),
    (@alexander_id, 'Stretching', '2025-10-01', 30, 120, 'Flexibility work'),
    (@alexander_id, 'Kickboxing', '2025-10-08', 55, 500, 'Technique practice');

-- Add workouts for existing users (assuming IDs 1-5 exist)
INSERT INTO workout (user_id, workout_name, date, duration, calories_burned, notes)
VALUES
    (1, 'Morning Run', '2025-09-10', 30, 300, 'Easy pace'),
    (1, 'Gym Session', '2025-09-15', 60, 450, 'Full body'),
    (1, 'Evening Walk', '2025-09-20', 45, 200, 'Recovery'),
    (1, 'Strength Training', '2025-09-25', 55, 420, 'Upper body focus'),
    (1, 'Cardio Mix', '2025-09-30', 40, 380, 'Interval training'),
    (2, 'Strength Training', '2025-09-11', 75, 500, 'Heavy weights'),
    (2, 'Cardio Mix', '2025-09-18', 40, 380, 'Interval training'),
    (2, 'Leg Day', '2025-09-24', 70, 480, 'Squats and lunges'),
    (2, 'Full Body', '2025-10-01', 65, 460, 'Complete workout'),
    (3, 'Yoga Flow', '2025-09-12', 60, 220, 'Vinyasa style'),
    (3, 'Pilates', '2025-09-19', 50, 260, 'Reformer class'),
    (3, 'Stretching', '2025-09-26', 40, 180, 'Flexibility'),
    (3, 'Meditation', '2025-10-02', 30, 100, 'Mindfulness'),
    (4, 'CrossFit', '2025-09-13', 60, 520, 'Benchmark WOD'),
    (4, 'Running', '2025-09-21', 50, 450, '10K training'),
    (4, 'Swimming', '2025-09-27', 45, 400, 'Lap swimming'),
    (4, 'Cycling', '2025-10-03', 55, 480, 'Hill training'),
    (5, 'Swimming', '2025-09-14', 45, 340, 'Endurance training'),
    (5, 'Yoga', '2025-09-22', 50, 200, 'Relaxation'),
    (5, 'Cardio', '2025-09-28', 40, 360, 'Treadmill run'),
    (5, 'Strength', '2025-10-04', 60, 440, 'Weight training');

-- Add gym memberships for some new users
-- Assuming gym_id 1 exists
INSERT INTO gym_member (user_id, gym_id, membership_id, membership_type, start_date, end_date)
VALUES
    (@michael_id, 1, 1001, 'Premium', '2025-01-01', '2025-12-31'),
    (@james_id, 1, 1002, 'Premium', '2025-03-01', '2026-02-28'),
    (@william_id, 1, 1003, 'Basic', '2025-06-01', '2025-11-30'),
    (@ethan_id, 1, 1004, 'Premium', '2025-02-15', '2026-02-14'),
    (@alexander_id, 1, 1005, 'Basic', '2025-07-01', '2025-12-31'),
    (@olivia_id, 1, 1006, 'Premium', '2025-04-01', '2026-03-31'),
    (@isabella_id, 1, 1007, 'Basic', '2025-08-01', '2026-01-31');

-- Add progress tracking for users
INSERT INTO progress (user_id, record_date, weight, body_fat_percentage, muscle_mass, notes)
VALUES
    (@emma_id, '2025-09-01', 62.5, 22.0, 45.0, 'Starting measurements'),
    (@emma_id, '2025-09-15', 61.8, 21.5, 45.5, 'Good progress'),
    (@michael_id, '2025-09-01', 85.0, 15.0, 68.0, 'Bulking phase start'),
    (@michael_id, '2025-09-20', 87.2, 15.5, 70.0, 'Gaining muscle'),
    (@sophia_id, '2025-09-01', 58.0, 24.0, 42.0, 'Baseline'),
    (@james_id, '2025-09-01', 78.5, 12.0, 65.0, 'Competition ready'),
    (@olivia_id, '2025-09-01', 65.0, 23.0, 47.0, 'Starting fitness journey'),
    (@william_id, '2025-09-01', 82.0, 18.0, 63.0, 'Cutting phase'),
    (@ava_id, '2025-09-01', 60.0, 25.0, 43.0, 'Initial assessment'),
    (@ethan_id, '2025-09-01', 95.0, 14.0, 78.0, 'Powerlifter stats'),
    (@isabella_id, '2025-09-01', 63.5, 22.5, 46.0, 'First check-in'),
    (@alexander_id, '2025-09-01', 75.0, 16.0, 60.0, 'Martial artist build');

-- Add some staff members
INSERT INTO staff (user_id, role, hire_date, salary, specialization)
VALUES
    (@sophia_id, 'Trainer', '2024-01-15', 45000.00, 'Pilates and Yoga'),
    (@ava_id, 'Trainer', '2024-03-01', 42000.00, 'Group Fitness');

COMMIT;

SELECT 'Test data generated successfully!' as status;
SELECT COUNT(*) as total_users FROM user;
SELECT COUNT(*) as total_workouts FROM workout;
SELECT COUNT(*) as total_gym_members FROM gym_member;

