# Write your MySQL query statement below
SELECT machine_id, ROUND(AVG(diff), 3) processing_time
FROM
    (SELECT a1.machine_id, a1.process_id, (a2.timestamp - a1.timestamp) diff
    FROM Activity a1 
    JOIN Activity a2
    ON a1.machine_id = a2.machine_id
    AND a1.process_id = a2.process_id
    AND a1.activity_type = 'start' AND a2.activity_type = 'end') t
GROUP BY(machine_id);