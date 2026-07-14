-- Last updated: 14/07/2026, 15:27:39
SELECT m.name
FROM Employee e
JOIN Employee m 
  ON e.managerId = m.id
GROUP BY m.id, m.name
HAVING COUNT(e.id) >= 5;