-- Last updated: 14/07/2026, 15:27:19
SELECT 
    CASE 
        WHEN id % 2 <> 0 AND id = (SELECT MAX(id) FROM Seat) THEN id
        WHEN id % 2 <> 0 THEN id + 1
        ELSE id - 1
    END AS id,
    student
FROM 
    Seat
ORDER BY 
    id ASC;