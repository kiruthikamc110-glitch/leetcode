-- Last updated: 14/07/2026, 15:27:36
SELECT name
FROM Customer
WHERE referee_id != 2 
   OR referee_id IS NULL;