-- Last updated: 14/07/2026, 14:56:57
# Write your MySQL query statement below
WITH PlayerLogins AS (
    SELECT 
        player_id,
        event_date,
        MIN(event_date) OVER(PARTITION BY player_id) AS first_login,
        LEAD(event_date) OVER(PARTITION BY player_id ORDER BY event_date) AS next_login
    FROM Activity
)
SELECT 
    ROUND(
        COUNT(DISTINCT CASE WHEN DATEDIFF(next_login, first_login) = 1 THEN player_id END) 
        / COUNT(DISTINCT player_id), 
        2
    ) AS fraction
FROM PlayerLogins;