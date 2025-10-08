
-- Gyms Table
CREATE TABLE GYM (
    gym_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(100)
);

INSERT INTO GYM (name, address, phone, email)
VALUES
('GetBuff Gym', '123 buff strasse', '123-456-7890', 'info@getbuff.com'),
('Muscle hustle', '42 mooscle Rd', '987-654-3210', 'info@musclemuscle.com'),
('Ex60 gym', '60 Lumiere', '555-123-4567', 'info@expedition60.com');


-- Users
CREATE TABLE USER (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    password_hash VARCHAR(255),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    gender ENUM('M','F','Other'),
    registration_date DATE,
    profile_picture VARCHAR(255)
);

INSERT INTO USER (username, email, password_hash, first_name, last_name, date_of_birth, gender, registration_date)
VALUES
('swu', 'siwoo72@mail.com', 'hashed_pw', 'Siwoo', 'Lee', '2003-07-02', 'M', '2023-01-10'),
('jackson', 'jacked@mail.com', 'hashed_pw', 'Jack', 'Sonn', '2000-09-21', 'M', '2023-01-15'),
('xcal', 'sword@mail.com', 'hashed_pw', 'Alexander', 'Dawn', '2004-03-08', 'M', '2023-02-01'),
('alicia', 'iliketodraw@mail.com', 'hashed_pw', 'Maelle', 'Verso', '2010-12-05', 'F', '2023-02-20'),
('curator', 'aline@mail.com', 'hashed_pw', 'Renoir', 'Dessendre', '1992-07-30', 'F', '2023-03-01');




-- Staff members 

CREATE TABLE STAFF (
    user_id INT PRIMARY KEY,
    employee_id VARCHAR(20),
    position VARCHAR(50),  -- 'Trainer', 'Manager', 'Receptionist'
    hire_date DATE,
    salary DECIMAL(10,2),
    gym_id INT,
    FOREIGN KEY (user_id) REFERENCES USER(user_id),
    FOREIGN KEY (gym_id) REFERENCES GYM(gym_id)
);

INSERT INTO STAFF (user_id, employee_id, position, hire_date, salary, gym_id)
VALUES
(1, 'CLEA33', 'Trainer', '2021-05-15', 3200.00, 1),
(2, 'ALINE34', 'Manager', '2020-01-10', 5000.00, 1),
(3, 'CWOO72', 'Receptionist', '2022-03-01', 2800.00, 2),
(4, 'MAELLE16', 'Manager', '2019-11-20', 5200.00, 2),
(5, 'GUSTAVE32', 'Trainer', '2022-06-10', 3500.00, 3);
