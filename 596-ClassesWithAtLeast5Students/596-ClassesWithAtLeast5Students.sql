-- Last updated: 14/07/2026, 15:27:30
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;