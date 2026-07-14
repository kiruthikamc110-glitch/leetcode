-- Last updated: 14/07/2026, 15:27:29
# Write your MySQL query statement below
WITH StreakCheck AS (
    SELECT 
        id,
        visit_date,
        people,
        LAG(people, 2) OVER (ORDER BY id) AS prev_2,
        LAG(people, 1) OVER (ORDER BY id) AS prev_1,
        LEAD(people, 1) OVER (ORDER BY id) AS next_1,
        LEAD(people, 2) OVER (ORDER BY id) AS next_2
    FROM Stadium
)
SELECT id, visit_date, people
FROM StreakCheck
WHERE people >= 100 AND (
    (prev_2 >= 100 AND prev_1 >= 100) OR -- It's the 3rd row in a streak
    (prev_1 >= 100 AND next_1 >= 100) OR -- It's the middle row in a streak
    (next_1 >= 100 AND next_2 >= 100)    -- It's the 1st row in a streak
)
ORDER BY visit_date ASC;