SELECT students.student_name, grades.*
FROM Challenge2.grades
LEFT JOIN Challenge2.students
ON Challenge2.students.student_id=Challenge2.grades.student_id;