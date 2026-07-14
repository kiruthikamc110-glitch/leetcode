-- Last updated: 14/07/2026, 15:27:20
# Write your MySQL query statement below
SELECT 
    id, 
    movie, 
    description, 
    rating
FROM 
    Cinema
WHERE 
    id % 2 <> 0 
    AND description <> 'boring'
ORDER BY 
    rating DESC;