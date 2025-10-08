-- HW3: Sample Data for User Hierarchy

-- Note: This file creates sample data for the User ISA hierarchy:
-- USER (superclass) -> INDIVIDUAL_USER, GYM_MEMBER, STAFF (subclasses)

USE fittrack_pro;

-- Insert sample data for USER (superclass)
INSERT INTO user (username, email, password_hash, first_name, last_name, date_of_birth, gender, registration_date, profile_picture)
VALUES
-- Individual Users (fitness enthusiasts)
('fitness_alex', 'alex.fitness@email.com', 'hash123', 'Alex', 'Johnson', '1995-03-15', 'Male', '2024-01-15 10:30:00', 'alex_profile.jpg'),
('yoga_sarah', 'sarah.yoga@email.com', 'hash456', 'Sarah', 'Williams', '1988-07-22', 'Female', '2024-02-01 14:20:00', 'sarah_profile.jpg'),
('runner_mike', 'mike.run@email.com', 'hash789', 'Mike', 'Davis', '1992-11-08', 'Male', '2024-02-15 09:45:00', 'mike_profile.jpg'),
('strong_emma', 'emma.strong@email.com', 'hash101', 'Emma', 'Brown', '1990-05-30', 'Female', '2024-03-01 16:15:00', 'emma_profile.jpg'),

-- Gym Members (people with gym memberships)
('gym_john', 'john.gym@email.com', 'hash202', 'John', 'Smith', '1985-12-10', 'Male', '2024-01-20 11:00:00', 'john_profile.jpg'),
('gym_lisa', 'lisa.gym@email.com', 'hash303', 'Lisa', 'Wilson', '1993-04-18', 'Female', '2024-02-10 13:30:00', 'lisa_profile.jpg'),
('gym_david', 'david.gym@email.com', 'hash404', 'David', 'Miller', '1987-09-25', 'Male', '2024-02-20 08:45:00', 'david_profile.jpg'),
('gym_anna', 'anna.gym@email.com', 'hash505', 'Anna', 'Garcia', '1991-01-12', 'Female', '2024-03-05 15:20:00', 'anna_profile.jpg'),
('gym_tom', 'tom.gym@email.com', 'hash606', 'Tom', 'Anderson', '1989-08-03', 'Male', '2024-03-10 12:10:00', 'tom_profile.jpg'),

-- Staff Members 
('staff_maria', 'maria.staff@email.com', 'hash707', 'Maria', 'Rodriguez', '1986-06-14', 'Female', '2023-05-01 09:00:00', 'maria_profile.jpg'),
('staff_peter', 'peter.staff@email.com', 'hash808', 'Peter', 'Thompson', '1984-10-20', 'Male', '2023-07-15 10:30:00', 'peter_profile.jpg');

-- Insert sample data for INDIVIDUAL_USER (subclass)
INSERT INTO individual_user (user_id, fitness_level, primary_goals, workout_types)
VALUES
(1, 'Intermediate', 'Build muscle mass and improve strength', 'Weight training, Cardio'),
(2, 'Advanced', 'Increase flexibility and mental wellness', 'Yoga, Pilates, Meditation'),
(3, 'Beginner', 'Improve cardiovascular health and lose weight', 'Running, Walking, Light cardio'),
(4, 'Advanced', 'Powerlifting competition preparation', 'Heavy lifting, Strength training');

-- Insert sample data for GYM_MEMBER (subclass)
-- Note: gym_id references must exist in gym table (created by Lee's staff data)
INSERT INTO gym_member (user_id, membership_id, membership_type, start_date, end_date, gym_id)
VALUES
(5, 'MEM001', 'Premium', '2024-01-20', '2025-01-20', 1),  -- GetBuff Gym
(6, 'MEM002', 'Basic', '2024-02-10', '2024-08-10', 2),    -- Muscle hustle (expired)
(7, 'MEM003', 'VIP', '2024-02-20', '2025-02-20', 1),      -- GetBuff Gym
(8, 'MEM004', 'Premium', '2024-03-05', '2025-03-05', 3),  -- Ex60 gym
(9, 'MEM005', 'Basic', '2024-03-10', '2024-09-10', 2);    -- Muscle hustle (expired)

-- Insert additional staff data for User hierarchy testing
-- Note: These will also be referenced in the staff table
INSERT INTO staff (user_id, employee_id, position, hire_date, salary, gym_id)
VALUES
(10, 'EMP006', 'Trainer', '2023-05-01', 3300.00, 2),      -- Maria at Muscle hustle
(11, 'EMP007', 'Manager', '2023-07-15', 5500.00, 3);      -- Peter at Ex60 gym

-- Insert some workout data to make queries more interesting
INSERT INTO workout (user_id, workout_name, date, duration, calories_burned, notes)
VALUES
-- Individual users' workouts
(1, 'Upper Body Strength', '2024-10-01', 60, 350, 'Great session, increased weights'),
(1, 'Cardio Session', '2024-10-03', 45, 400, 'Good endurance workout'),
(2, 'Morning Yoga Flow', '2024-10-01', 75, 200, 'Very relaxing, improved flexibility'),
(2, 'Power Yoga', '2024-10-04', 90, 300, 'Challenging but rewarding'),
(3, 'Evening Run', '2024-10-02', 30, 250, 'Nice pace, felt good'),
(4, 'Deadlift Training', '2024-10-01', 90, 450, 'New PR! 180kg deadlift'),

-- Gym members' workouts
(5, 'Full Body Workout', '2024-10-02', 75, 500, 'Used premium equipment'),
(6, 'Basic Cardio', '2024-07-15', 30, 200, 'Last workout before membership expired'),
(7, 'VIP Training Session', '2024-10-03', 120, 600, 'Personal trainer session'),
(8, 'Swimming + Weights', '2024-10-04', 90, 550, 'Great pool facilities'),
(9, 'Group Class', '2024-08-20', 60, 350, 'Enjoyed the community aspect');

-- Insert progress tracking data for more complex queries
INSERT INTO progress_tracking (user_id, date, weight, body_fat_percentage, muscle_mass, measurements)
VALUES
-- Individual users progress
(1, '2024-01-15', 75.5, 15.2, 45.8, 'Chest: 98cm, Waist: 82cm, Arms: 35cm'),
(1, '2024-04-15', 78.2, 13.8, 48.1, 'Chest: 102cm, Waist: 80cm, Arms: 37cm'),
(1, '2024-07-15', 80.1, 12.5, 50.3, 'Chest: 105cm, Waist: 79cm, Arms: 38cm'),
(1, '2024-10-01', 82.0, 11.8, 52.1, 'Chest: 107cm, Waist: 78cm, Arms: 39cm'),

(2, '2024-02-01', 62.3, 18.5, 35.2, 'Flexibility improved significantly'),
(2, '2024-05-01', 61.8, 17.9, 35.8, 'Better balance and core strength'),
(2, '2024-08-01', 61.2, 17.2, 36.1, 'Advanced poses achieved'),

-- Gym members progress
(5, '2024-01-20', 85.0, 20.1, 42.5, 'Starting premium membership'),
(5, '2024-04-20', 82.5, 18.3, 44.2, 'Good progress with trainer'),
(5, '2024-07-20', 80.8, 16.8, 45.8, 'Consistent improvement'),
(5, '2024-10-01', 79.2, 15.5, 47.1, 'Excellent results'),

(7, '2024-02-20', 90.5, 22.3, 40.1, 'VIP member baseline'),
(7, '2024-05-20', 87.8, 19.8, 42.8, 'Personal training paying off'),
(7, '2024-08-20', 85.2, 17.9, 44.9, 'Great transformation'),

(8, '2024-03-05', 70.2, 16.8, 38.5, 'New member at Ex60'),
(8, '2024-06-05', 71.8, 15.2, 40.1, 'Building muscle with swimming'),
(8, '2024-09-05', 73.5, 14.1, 41.8, 'Excellent pool training results');
