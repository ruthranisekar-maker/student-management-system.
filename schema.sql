CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    course VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO students (name, email, course) VALUES
('John Doe', 'john@gmailcom', 'Computer Science'),
('Jane Smith', 'jane@email.com', 'Mathematics');
select * from students;