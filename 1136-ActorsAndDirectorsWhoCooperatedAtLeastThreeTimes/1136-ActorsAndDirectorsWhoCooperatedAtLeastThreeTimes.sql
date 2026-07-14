-- Last updated: 14/07/2026, 14:57:05
# Write your MySQL query statement below
SELECT actor_id,director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3;