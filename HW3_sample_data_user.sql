-- User Hierarchy Tables

CREATE TABLE user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    gender ENUM('Male', 'Female', 'Other'),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    profile_picture VARCHAR(255)
);

INSERT INTO user (username, email, password_hash, first_name, last_name, date_of_birth, gender, registration_date, profile_picture)
VALUES
('fitness_alex', 'alex.fitness@email.com', 'hash123', 'Alex', 'Johnson', '1995-03-15', 'Male', '2024-01-15 10:30:00', 'alex_profile.jpg'),
('yoga_sarah', 'sarah.yoga@email.com', 'hash456', 'Sarah', 'Williams', '1988-07-22', 'Female', '2024-02-01 14:20:00', 'sarah_profile.jpg'),
('runner_mike', 'mike.run@email.com', 'hash789', 'Mike', 'Davis', '1992-11-08', 'Male', '2024-02-15 09:45:00', 'mike_profile.jpg'),
('strong_emma', 'emma.strong@email.com', 'hash101', 'Emma', 'Brown', '1990-05-30', 'Female', '2024-03-01 16:15:00', 'emma_profile.jpg'),
('gym_john', 'john.gym@email.com', 'hash202', 'John', 'Smith', '1985-12-10', 'Male', '2024-01-20 11:00:00', 'john_profile.jpg'),
('member_anna', 'anna.member@email.com', 'hash303', 'Anna', 'Garcia', '1993-08-18', 'Female', '2024-02-10 13:30:00', 'anna_profile.jpg'),
('premium_david', 'david.premium@email.com', 'hash404', 'David', 'Miller', '1987-04-25', 'Male', '2024-03-05 15:45:00', 'david_profile.jpg'),
('vip_lisa', 'lisa.vip@email.com', 'hash505', 'Lisa', 'Wilson', '1991-09-12', 'Female', '2024-03-15 12:20:00', 'lisa_profile.jpg'),
('basic_tom', 'tom.basic@email.com', 'hash606', 'Tom', 'Anderson', '1989-06-03', 'Male', '2024-04-01 10:15:00', 'tom_profile.jpg'),
('trainer_mark', 'mark.trainer@email.com', 'hash707', 'Mark', 'Thompson', '1986-11-20', 'Male', '2023-05-01 09:00:00', 'mark_profile.jpg'),
('receptionist_jane', 'jane.reception@email.com', 'hash808', 'Jane', 'Roberts', '1994-02-14', 'Female', '2023-07-15 08:30:00', 'jane_profile.jpg'),
('manager_bob', 'bob.manager@email.com', 'hash909', 'Bob', 'Wilson', '1980-03-10', 'Male', '2022-01-15', 'bob_profile.jpg'),
('trainer_lisa', 'lisa.trainer@email.com', 'hash010', 'Lisa', 'Davis', '1985-09-25', 'Female', '2022-08-20', 'lisa_profile.jpg'),
('cleaner_tom', 'tom.cleaner@email.com', 'hash111', 'Tom', 'Brown', '1990-12-05', 'Male', '2023-03-10', 'tom_profile.jpg'),
('security_mike', 'mike.security@email.com', 'hash212', 'Mike', 'Taylor', '1988-06-15', 'Male', '2023-06-01', 'mike_profile.jpg'),
('admin_sara', 'sara.admin@email.com', 'hash313', 'Sara', 'Johnson', '1992-04-20', 'Female', '2023-09-15', 'sara_profile.jpg');

CREATE TABLE individual_user (
    user_id INT PRIMARY KEY,
    fitness_level ENUM('Beginner', 'Intermediate', 'Advanced') DEFAULT 'Beginner',
    primary_goals TEXT,
    workout_types VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
);

INSERT INTO individual_user (user_id, fitness_level, primary_goals, workout_types)
VALUES
(1, 'Intermediate', 'Build muscle mass and improve strength', 'Weight training, Cardio'),
(2, 'Advanced', 'Improve flexibility and mental wellness', 'Yoga, Pilates, Meditation'),
(3, 'Intermediate', 'Increase endurance and lose weight', 'Running, Cycling, Swimming'),
(4, 'Beginner', 'General fitness and strength building', 'Basic weight training, Walking');

CREATE TABLE gym_member (
    user_id INT PRIMARY KEY,
    membership_id VARCHAR(20) UNIQUE NOT NULL,
    membership_type ENUM('Basic', 'Premium', 'VIP') DEFAULT 'Basic',
    start_date DATE NOT NULL,
    end_date DATE,
    gym_id INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
);

INSERT INTO gym_member (user_id, membership_id, membership_type, start_date, end_date, gym_id)
VALUES
(5, 'MEM001', 'Premium', '2024-01-20', '2025-01-20', 1),
(6, 'MEM002', 'Premium', '2024-02-10', '2025-02-10', 2),
(7, 'MEM003', 'VIP', '2024-03-05', '2025-03-05', 1),
(8, 'MEM004', 'VIP', '2024-03-15', '2025-03-15', 2),
(9, 'MEM005', 'Basic', '2024-04-01', '2025-04-01', 1);

CREATE TABLE staff (
    user_id INT PRIMARY KEY,
    employee_id VARCHAR(20) UNIQUE NOT NULL,
    position VARCHAR(50) NOT NULL,
    hire_date DATE NOT NULL,
    salary DECIMAL(10, 2),
    gym_id INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
);

INSERT INTO staff (user_id, employee_id, position, hire_date, salary, gym_id)
VALUES
(10, 'EMP006', 'Trainer', '2023-05-01', 3200.00, 1),
(11, 'EMP007', 'Receptionist', '2023-07-15', 2800.00, 2),
(12, 'EMP008', 'Manager', '2022-01-15', 4500.00, 1),
(13, 'EMP009', 'Trainer', '2022-08-20', 3400.00, 2),
(14, 'EMP010', 'Cleaner', '2023-03-10', 2200.00, 1),
(15, 'EMP011', 'Security', '2023-06-01', 2600.00, 2),
(16, 'EMP012', 'Admin', '2023-09-15', 3000.00, 1);

-- Supporting tables for queries

CREATE TABLE gym (
    gym_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100)
);

INSERT INTO gym (name, address, phone, email)
VALUES
('GetBuff Gym', '123 Fitness Street', '123-456-7890', 'info@getbuff.com'),
('Ex60 gym', '60 Lumiere Avenue', '555-123-4567', 'info@ex60.com');

CREATE TABLE workout (
    workout_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    workout_date DATE NOT NULL,
    duration INT,
    calories_burned INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
);

INSERT INTO workout (user_id, workout_date, duration, calories_burned)
VALUES
(1, '2024-10-01', 90, 450),
(1, '2024-10-03', 60, 320),
(2, '2024-10-01', 90, 280),
(2, '2024-10-04', 60, 200),
(3, '2024-10-02', 60, 400),
(3, '2024-10-05', 90, 520),
(4, '2024-10-03', 60, 250),
(4, '2024-10-06', 30, 150),
(5, '2024-10-01', 90, 380),
(5, '2024-10-04', 90, 420),
(6, '2024-10-02', 90, 350),
(7, '2024-10-03', 90, 480),
(7, '2024-10-06', 120, 600),
(8, '2024-10-04', 90, 390),
(9, '2024-10-05', 30, 180),
(10, '2024-10-02', 60, 300),
(11, '2024-10-05', 30, 150),
(12, '2024-10-01', 45, 250),
(13, '2024-10-03', 75, 350),
(14, '2024-10-04', 30, 200),
(15, '2024-10-06', 60, 280),
(16, '2024-10-02', 90, 400);

CREATE TABLE progress_tracking (
    tracking_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    date_recorded DATE NOT NULL,
    weight DECIMAL(5, 2),
    body_fat_percentage DECIMAL(4, 2),
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
);

INSERT INTO progress_tracking (user_id, date_recorded, weight, body_fat_percentage)
VALUES
(1, '2024-09-01', 75.5, 15.2),
(1, '2024-10-01', 76.2, 14.8),
(2, '2024-09-15', 62.3, 18.5),
(2, '2024-10-15', 61.8, 17.9),
(3, '2024-09-10', 82.1, 20.3),
(3, '2024-10-10', 80.5, 19.1),
(5, '2024-08-20', 78.9, 16.8),
(5, '2024-09-20', 79.8, 16.2),
(5, '2024-10-20', 80.5, 15.7),
(6, '2024-09-01', 68.2, 22.1),
(6, '2024-10-01', 67.1, 20.8),
(7, '2024-08-15', 85.3, 18.9),
(7, '2024-09-15', 86.8, 18.2),
(7, '2024-10-15', 88.1, 17.5);