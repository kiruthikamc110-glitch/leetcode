-- Last updated: 14/07/2026, 15:27:22
# Write your MySQL query statement below
SELECT 
    MAX(num) AS num
FROM (
    SELECT 
        num
    FROM 
        MyNumbers
    GROUP BY 
        num
    HAVING 
        COUNT(num) = 1
) AS UniqueNumbers;