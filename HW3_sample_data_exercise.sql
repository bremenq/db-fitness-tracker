DROP TABLE IF EXISTS workout_exercise, workout, flexibility, strength, cardio, exercise, `user`;

CREATE TABLE `user`(
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  gender ENUM('Male','Female','Other') DEFAULT 'Other'
);

CREATE TABLE exercise(
  exercise_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  category ENUM('Cardio','Strength','Flexibility') NOT NULL,
  difficulty ENUM('Easy','Medium','Hard') NOT NULL
);

CREATE TABLE cardio(
  exercise_id INT PRIMARY KEY,
  target_heart_rate INT,
  intensity_level ENUM('Low','Medium','High'),
  FOREIGN KEY (exercise_id) REFERENCES exercise(exercise_id) ON DELETE CASCADE
);

CREATE TABLE strength(
  exercise_id INT PRIMARY KEY,
  weight_range VARCHAR(50),
  rep_range VARCHAR(20),
  muscle_focus VARCHAR(100),
  FOREIGN KEY (exercise_id) REFERENCES exercise(exercise_id) ON DELETE CASCADE
);

CREATE TABLE flexibility(
  exercise_id INT PRIMARY KEY,
  stretch_duration INT,
  flexibility_level ENUM('Beginner','Intermediate','Advanced'),
  FOREIGN KEY (exercise_id) REFERENCES exercise(exercise_id) ON DELETE CASCADE
);

CREATE TABLE workout(
  workout_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  workout_name VARCHAR(100),
  date DATE NOT NULL,
  duration INT,
  FOREIGN KEY (user_id) REFERENCES `user`(user_id) ON DELETE CASCADE
);

CREATE TABLE workout_exercise(
  we_id INT AUTO_INCREMENT PRIMARY KEY,
  workout_id INT NOT NULL,
  exercise_id INT NOT NULL,
  sets INT, reps INT, weight DECIMAL(6,2),
  duration INT, rest_time INT,
  FOREIGN KEY (workout_id) REFERENCES workout(workout_id) ON DELETE CASCADE,
  FOREIGN KEY (exercise_id) REFERENCES exercise(exercise_id) ON DELETE CASCADE
);

INSERT INTO `user`(first_name,last_name,gender) VALUES
('Alex','One','Male'),('Bea','Two','Female'),('Cam','Three','Other');

INSERT INTO exercise(name,category,difficulty) VALUES
('Treadmill Run','Cardio','Medium'),
('HIIT Sprint','Cardio','Hard'),
('Back Squat','Strength','Hard'),
('Bench Press','Strength','Medium'),
('Hamstring Stretch','Flexibility','Easy');

INSERT INTO cardio(exercise_id,target_heart_rate,intensity_level) VALUES
(1,185,'High'),(2,190,'High');

INSERT INTO strength(exercise_id,weight_range,rep_range,muscle_focus) VALUES
(3,'40-200kg','1-12','Quads/Glutes'),
(4,'20-150kg','3-12','Chest/Triceps');

INSERT INTO flexibility(exercise_id,stretch_duration,flexibility_level) VALUES
(5,45,'Beginner');

INSERT INTO workout(user_id,workout_name,date,duration) VALUES
(1,'Run + Squat',CURDATE() - INTERVAL 56 DAY,60),
(1,'Intervals',CURDATE() - INTERVAL 28 DAY,30),
(1,'HIIT Sprint',CURDATE() - INTERVAL 21 DAY,25),
(1,'Run',CURDATE() - INTERVAL 14 DAY,30),
(1,'Run',CURDATE() - INTERVAL  7 DAY,32),
(2,'Leg Day',CURDATE() - INTERVAL 35 DAY,50),
(2,'Bench + Run',CURDATE() - INTERVAL 14 DAY,55),
(3,'Stretch + Run',CURDATE() - INTERVAL 20 DAY,30),
(3,'Run',CURDATE() - INTERVAL 10 DAY,26);

INSERT INTO workout_exercise(workout_id,exercise_id,sets,reps,weight,duration,rest_time) VALUES
(1,1,1,1,NULL,20,60),
(1,3,5,5,100,0,120),
(2,1,1,1,NULL,30,0),
(3,2,1,1,NULL,25,0),
(4,1,1,1,NULL,30,0),
(5,1,1,1,NULL,32,0),
(6,3,5,3,120,0,150),
(7,4,4,6, 80,0,120),
(7,1,1,1,NULL,25,0),
(8,5,1,1,NULL,10,0),
(8,1,1,1,NULL,20,0),
(9,1,1,1,NULL,26,0);
