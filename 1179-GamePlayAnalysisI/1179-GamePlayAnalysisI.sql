-- Last updated: 14/07/2026, 14:56:58
# Write your MySQL query statement below
SELECT 
    player_id, 
    MIN(event_date) AS first_login
FROM 
    Activity
GROUP BY 
    player_id;