-- Last updated: 14/07/2026, 14:56:52
# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT DISTINCT 
    author_id AS id
FROM 
    Views
WHERE 
    author_id = viewer_id
ORDER BY 
    id ASC;