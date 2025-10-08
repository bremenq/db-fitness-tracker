-- FitTrack Pro Database Schema
-- Assignment 2: Logical Database Schema
-- Team: Aleksandr Zinovev, Siwoo Lee, Arslan Ahmet Berk
-- Date: September 2025

-- Drop tables if they exist (for testing)
DROP TABLE IF EXISTS class_booking;
DROP TABLE IF EXISTS workout_exercise;
DROP TABLE IF EXISTS progress_tracking;
DROP TABLE IF EXISTS flexibility;
DROP TABLE IF EXISTS strength;
DROP TABLE IF EXISTS cardio;
DROP TABLE IF EXISTS exercise;
DROP TABLE IF EXISTS class;
DROP TABLE IF EXISTS equipment;
DROP TABLE IF EXISTS receptionist;
DROP TABLE IF EXISTS manager;
DROP TABLE IF EXISTS trainer;
DROP TABLE IF EXISTS staff;
DROP TABLE IF EXISTS gym_member;
DROP TABLE IF EXISTS individual_user;
DROP TABLE IF EXISTS workout;
DROP TABLE IF EXISTS gym;
DROP TABLE IF EXISTS user;

-- Create database
CREATE DATABASE IF NOT EXISTS fittrack_pro;
USE fittrack_pro;

-- ISA Hierarchy 1: User Entity Hierarchy
-- Superclass: User
CREATE TABLE user (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    gender ENUM('Male', 'Female', 'Other'),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    profile_picture VARCHAR(255),
    
    -- Constraints
    CONSTRAINT chk_email_format CHECK (email LIKE '%@%.%'),
    CONSTRAINT chk_username_length CHECK (LENGTH(username) >= 3)
);

-- Subclass: Individual User
CREATE TABLE individual_user (
    user_id INT PRIMARY KEY,
    fitness_level ENUM('Beginner', 'Intermediate', 'Advanced') DEFAULT 'Beginner',
    primary_goals TEXT,
    workout_types VARCHAR(255),
    
    -- Foreign key constraint
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
);

-- Gym entity (needed for gym_member and staff)
CREATE TABLE gym (
    gym_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100),
    operating_hours VARCHAR(100),
    facilities TEXT,
    
    -- Constraints
    CONSTRAINT chk_gym_email_format CHECK (email LIKE '%@%.%' OR email IS NULL)
);

-- Subclass: Gym Member
CREATE TABLE gym_member (
    user_id INT PRIMARY KEY,
    membership_id VARCHAR(50) UNIQUE NOT NULL,
    membership_type ENUM('Basic', 'Premium', 'VIP') NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    gym_id INT NOT NULL,
    
    -- Foreign key constraints
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE,
    FOREIGN KEY (gym_id) REFERENCES gym(gym_id) ON DELETE RESTRICT,
    
    -- Check constraints
    CONSTRAINT chk_membership_dates CHECK (end_date IS NULL OR end_date > start_date)
);

-- Subclass: Staff
CREATE TABLE staff (
    user_id INT PRIMARY KEY,
    employee_id VARCHAR(50) UNIQUE NOT NULL,
    position VARCHAR(50) NOT NULL,
    hire_date DATE NOT NULL,
    salary DECIMAL(10,2),
    gym_id INT NOT NULL,
    
    -- Foreign key constraints
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE,
    FOREIGN KEY (gym_id) REFERENCES gym(gym_id) ON DELETE RESTRICT,
    
    -- Check constraints
    CONSTRAINT chk_salary_positive CHECK (salary > 0),
    CONSTRAINT chk_hire_date CHECK (hire_date <= CURDATE())
);

-- ISA Hierarchy 2: Staff Specialization
-- Subclass: Trainer
CREATE TABLE trainer (
    user_id INT PRIMARY KEY,
    certification VARCHAR(100),
    specialization VARCHAR(100),
    hourly_rate DECIMAL(8,2),
    
    -- Foreign key constraint
    FOREIGN KEY (user_id) REFERENCES staff(user_id) ON DELETE CASCADE,
    
    -- Check constraints
    CONSTRAINT chk_hourly_rate_positive CHECK (hourly_rate > 0)
);

-- Subclass: Manager
CREATE TABLE manager (
    user_id INT PRIMARY KEY,
    department VARCHAR(50),
    access_level ENUM('Low', 'Medium', 'High') DEFAULT 'Medium',
    bonus_eligible BOOLEAN DEFAULT TRUE,
    
    -- Foreign key constraint
    FOREIGN KEY (user_id) REFERENCES staff(user_id) ON DELETE CASCADE
);

-- Subclass: Receptionist
CREATE TABLE receptionist (
    user_id INT PRIMARY KEY,
    shift_schedule VARCHAR(100),
    languages_spoken VARCHAR(255),
    
    -- Foreign key constraint
    FOREIGN KEY (user_id) REFERENCES staff(user_id) ON DELETE CASCADE
);

-- Workout entity
CREATE TABLE workout (
    workout_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    workout_name VARCHAR(100) NOT NULL,
    date DATE NOT NULL,
    duration INT, -- in minutes
    calories_burned INT,
    notes TEXT,
    
    -- Foreign key constraint
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE,
    
    -- Check constraints
    CONSTRAINT chk_duration_positive CHECK (duration > 0),
    CONSTRAINT chk_calories_positive CHECK (calories_burned >= 0)
);

-- ISA Hierarchy 3: Exercise Categories
-- Superclass: Exercise
CREATE TABLE exercise (
    exercise_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    muscle_groups VARCHAR(255),
    difficulty ENUM('Easy', 'Medium', 'Hard') DEFAULT 'Medium',
    instructions TEXT,
    equipment_needed VARCHAR(255)
);

-- Subclass: Cardio
CREATE TABLE cardio (
    exercise_id INT PRIMARY KEY,
    target_heart_rate INT,
    intensity_level ENUM('Low', 'Medium', 'High') DEFAULT 'Medium',
    
    -- Foreign key constraint
    FOREIGN KEY (exercise_id) REFERENCES exercise(exercise_id) ON DELETE CASCADE,
    
    -- Check constraints
    CONSTRAINT chk_heart_rate_range CHECK (target_heart_rate BETWEEN 60 AND 220)
);

-- Subclass: Strength
CREATE TABLE strength (
    exercise_id INT PRIMARY KEY,
    weight_range VARCHAR(50),
    rep_range VARCHAR(20),
    muscle_focus VARCHAR(100),
    
    -- Foreign key constraint
    FOREIGN KEY (exercise_id) REFERENCES exercise(exercise_id) ON DELETE CASCADE
);

-- Subclass: Flexibility
CREATE TABLE flexibility (
    exercise_id INT PRIMARY KEY,
    stretch_duration INT, -- in seconds
    flexibility_level ENUM('Beginner', 'Intermediate', 'Advanced') DEFAULT 'Beginner',
    
    -- Foreign key constraint
    FOREIGN KEY (exercise_id) REFERENCES exercise(exercise_id) ON DELETE CASCADE,
    
    -- Check constraints
    CONSTRAINT chk_stretch_duration_positive CHECK (stretch_duration > 0)
);

-- Many-to-Many Relationship: Workout-Exercise
CREATE TABLE workout_exercise (
    workout_id INT,
    exercise_id INT,
    sets INT,
    reps INT,
    weight DECIMAL(6,2),
    duration INT, -- in minutes
    rest_time INT, -- in seconds
    
    -- Composite primary key
    PRIMARY KEY (workout_id, exercise_id),
    
    -- Foreign key constraints
    FOREIGN KEY (workout_id) REFERENCES workout(workout_id) ON DELETE CASCADE,
    FOREIGN KEY (exercise_id) REFERENCES exercise(exercise_id) ON DELETE CASCADE,
    
    -- Check constraints
    CONSTRAINT chk_sets_positive CHECK (sets > 0),
    CONSTRAINT chk_reps_positive CHECK (reps > 0),
    CONSTRAINT chk_weight_positive CHECK (weight >= 0)
);

-- Equipment entity
CREATE TABLE equipment (
    equipment_id INT PRIMARY KEY AUTO_INCREMENT,
    gym_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50),
    status ENUM('Available', 'In Use', 'Maintenance', 'Out of Order') DEFAULT 'Available',
    purchase_date DATE,
    maintenance_schedule VARCHAR(100),
    
    -- Foreign key constraint
    FOREIGN KEY (gym_id) REFERENCES gym(gym_id) ON DELETE CASCADE
);

-- Class entity
CREATE TABLE class (
    class_id INT PRIMARY KEY AUTO_INCREMENT,
    gym_id INT NOT NULL,
    trainer_id INT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    schedule_time DATETIME NOT NULL,
    duration INT NOT NULL, -- in minutes
    max_capacity INT DEFAULT 20,
    
    -- Foreign key constraints
    FOREIGN KEY (gym_id) REFERENCES gym(gym_id) ON DELETE CASCADE,
    FOREIGN KEY (trainer_id) REFERENCES trainer(user_id) ON DELETE SET NULL,
    
    -- Check constraints
    CONSTRAINT chk_class_duration_positive CHECK (duration > 0),
    CONSTRAINT chk_max_capacity_positive CHECK (max_capacity > 0)
);

-- Many-to-Many Relationship: Member-Class Booking
CREATE TABLE class_booking (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    class_id INT NOT NULL,
    member_id INT NOT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Booked', 'Attended', 'Cancelled', 'No Show') DEFAULT 'Booked',
    
    -- Foreign key constraints
    FOREIGN KEY (class_id) REFERENCES class(class_id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES gym_member(user_id) ON DELETE CASCADE,
    
    -- Unique constraint to prevent double booking
    UNIQUE KEY unique_member_class (class_id, member_id)
);

-- Progress Tracking entity
CREATE TABLE progress_tracking (
    tracking_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    date DATE NOT NULL,
    weight DECIMAL(5,2),
    body_fat_percentage DECIMAL(4,2),
    muscle_mass DECIMAL(5,2),
    measurements TEXT, -- JSON or structured text
    
    -- Foreign key constraint
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE,
    
    -- Check constraints
    CONSTRAINT chk_weight_realistic CHECK (weight BETWEEN 30 AND 300),
    CONSTRAINT chk_body_fat_percentage CHECK (body_fat_percentage BETWEEN 0 AND 50),
    
    -- Unique constraint for one record per user per date
    UNIQUE KEY unique_user_date (user_id, date)
);

-- Create indexes for better performance
CREATE INDEX idx_user_email ON user(email);
CREATE INDEX idx_user_username ON user(username);
CREATE INDEX idx_workout_user_date ON workout(user_id, date);
CREATE INDEX idx_class_schedule ON class(schedule_time);
CREATE INDEX idx_booking_status ON class_booking(status);
CREATE INDEX idx_progress_user_date ON progress_tracking(user_id, date);

-- Display table creation summary
SELECT 'FitTrack Pro Database Schema Created Successfully!' as Status;
