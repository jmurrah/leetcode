-- We define query quality as:

--     The average of the ratio between query rating and its position.

-- We also define poor query percentage as:

--     The percentage of all queries with rating less than 3.

-- Write a solution to find each query_name, the quality and poor_query_percentage.

-- Both quality and poor_query_percentage should be rounded to 2 decimal places.

-- Return the result table in any order.


-- Write your MySQL query statement below
SELECT 
    q1.query_name,
    ROUND(SUM(q1.rating / q1.position) / COUNT(q1.rating), 2) as quality,
    ROUND(SUM(IF(q1.rating < 3, 1, 0)) / COUNT(q1.rating) * 100, 2) AS poor_query_percentage
FROM Queries q1
WHERE q1.query_name IS NOT NULL
GROUP BY q1.query_name
