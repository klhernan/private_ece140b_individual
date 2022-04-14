-- Creating a table for 'courses.csv'. 
CREATE TABLE Challenge2.Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(40) NOT NULL,
    teacher_id INT);


-- Creating a table for 'teachers.csv'. 
CREATE TABLE Challenge2.Teachers (
    teacher_id INT PRIMARY KEY,
    teacher_name VARCHAR(30) NOT NULL);


-- Creating a table for 'students.csv'. 
CREATE TABLE Challenge2.Students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(20) NOT NULL,
    student_email VARCHAR(50) NOT NULL,
    student_password VARCHAR(30) NOT NULL);


-- Creating a table for 'grades.csv'. 
-- Note that the student_id is not unique
CREATE TABLE Challenge2.Grades (
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    grade VARCHAR(10));