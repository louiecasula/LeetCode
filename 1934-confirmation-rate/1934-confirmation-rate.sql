# Write your MySQL query statement below
SELECT s.user_id,
CASE 
    WHEN SUM(action='confirmed')/COUNT(*) IS NULL THEN 0
    ELSE ROUND(SUM(action='confirmed')/COUNT(*), 2)
END confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
ON c.user_id = s.user_id
GROUP BY(s.user_id);