-- Last updated: 14/07/2026, 15:27:38
SELECT 
    e.name, 
    b.bonus
FROM Employee e
LEFT JOIN Bonus b 
    ON e.empId = b.empId
WHERE b.bonus < 1000 
   OR b.bonus IS NULL;