-- Add more gym members for testing
-- First, let's add some users who will become gym members

-- Add users (IDs 42-51)
INSERT INTO user (user_id, first_name, last_name, email, date_of_birth, gender, username, password_hash) VALUES
(42, 'Michael', 'Chen', 'michael.chen@gym.com', '1988-03-15', 'Male', 'mchen88', 'hash_mchen'),
(43, 'Sarah', 'Johnson', 'sarah.j@fitness.com', '1992-07-22', 'Female', 'sjohnson', 'hash_sjohnson'),
(44, 'David', 'Martinez', 'david.m@workout.com', '1985-11-08', 'Male', 'dmartinez', 'hash_dmartinez'),
(45, 'Emily', 'Taylor', 'emily.t@gym.com', '1995-02-14', 'Female', 'etaylor', 'hash_etaylor'),
(46, 'James', 'Anderson', 'james.a@fitness.com', '1990-06-30', 'Male', 'janderson', 'hash_janderson'),
(47, 'Lisa', 'White', 'lisa.w@workout.com', '1987-09-18', 'Female', 'lwhite', 'hash_lwhite'),
(48, 'Robert', 'Brown', 'robert.b@gym.com', '1993-04-25', 'Male', 'rbrown', 'hash_rbrown'),
(49, 'Jennifer', 'Davis', 'jennifer.d@fitness.com', '1991-12-03', 'Female', 'jdavis', 'hash_jdavis'),
(50, 'William', 'Garcia', 'william.g@workout.com', '1989-08-17', 'Male', 'wgarcia', 'hash_wgarcia'),
(51, 'Amanda', 'Wilson', 'amanda.w@gym.com', '1994-01-20', 'Female', 'awilson', 'hash_awilson');

-- Add gym members with various membership types and dates
INSERT INTO gym_member (user_id, membership_id, membership_type, start_date, end_date, gym_id) VALUES
-- Active Basic memberships
(42, 'GM-2025-001', 'Basic', '2025-01-15', '2026-01-15', 1),
(43, 'GM-2025-002', 'Basic', '2025-03-01', '2025-12-01', 1),
(44, 'GM-2025-003', 'Basic', '2025-06-10', '2025-12-10', 1),

-- Active Premium memberships
(45, 'GM-2025-004', 'Premium', '2025-02-20', '2026-02-20', 1),
(46, 'GM-2025-005', 'Premium', '2025-05-15', '2026-05-15', 1),
(47, 'GM-2025-006', 'Premium', '2025-08-01', '2026-08-01', 1),

-- Active VIP memberships
(48, 'GM-2025-007', 'VIP', '2025-01-01', '2027-01-01', 1),
(49, 'GM-2025-008', 'VIP', '2025-04-10', '2027-04-10', 1),

-- Expired memberships
(50, 'GM-2024-001', 'Basic', '2024-01-15', '2025-01-15', 1),
(51, 'GM-2024-002', 'Premium', '2024-06-01', '2025-06-01', 1);

-- Add some workouts for these gym members
INSERT INTO workout (user_id, workout_name, date, duration, calories_burned) VALUES
-- Michael Chen workouts
(42, 'Morning Cardio', '2025-10-15', 45, 350),
(42, 'Strength Training', '2025-10-17', 60, 420),
(42, 'Evening Run', '2025-10-20', 30, 280),

-- Sarah Johnson workouts
(43, 'Yoga Session', '2025-10-16', 60, 200),
(43, 'HIIT Workout', '2025-10-18', 45, 400),
(43, 'Pilates', '2025-10-22', 50, 250),

-- David Martinez workouts
(44, 'Weight Training', '2025-10-14', 75, 500),
(44, 'Boxing', '2025-10-19', 60, 550),
(44, 'Core Workout', '2025-10-23', 40, 300),

-- Emily Taylor workouts
(45, 'Spin Class', '2025-10-15', 50, 450),
(45, 'Swimming', '2025-10-20', 45, 380),
(45, 'Dance Fitness', '2025-10-24', 55, 420),

-- James Anderson workouts
(46, 'CrossFit', '2025-10-16', 60, 600),
(46, 'Running', '2025-10-21', 40, 400),
(46, 'Strength Circuit', '2025-10-25', 50, 480),

-- Lisa White workouts
(47, 'Barre Class', '2025-10-17', 55, 320),
(47, 'Cycling', '2025-10-22', 45, 380),
(47, 'Stretching', '2025-10-26', 30, 150),

-- Robert Brown workouts
(48, 'Personal Training', '2025-10-18', 60, 520),
(48, 'Basketball', '2025-10-23', 90, 650),
(48, 'Functional Training', '2025-10-27', 55, 480),

-- Jennifer Davis workouts
(49, 'Zumba', '2025-10-19', 60, 450),
(49, 'Aqua Aerobics', '2025-10-24', 45, 300),
(49, 'TRX Training', '2025-10-28', 50, 420),

-- William Garcia workouts (expired member)
(50, 'Morning Jog', '2024-12-15', 30, 250),
(50, 'Gym Session', '2025-01-10', 60, 400),

-- Amanda Wilson workouts (expired member)
(51, 'Yoga', '2025-05-20', 60, 200),
(51, 'Cardio', '2025-05-28', 45, 350);

SELECT 'Data insertion completed successfully!' as status;
SELECT CONCAT('Total gym members: ', COUNT(*)) as result FROM gym_member;

