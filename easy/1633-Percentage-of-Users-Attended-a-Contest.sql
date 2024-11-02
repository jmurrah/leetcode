-- Write a solution to find the percentage of the users registered in each contest rounded to two decimals.

-- Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.


-- Write your MySQL query statement below
SELECT r.contest_id, ROUND(COUNT(r.user_id) / (SELECT COUNT(*) FROM Users u), 4) * 100 AS percentage
FROM Register r
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC
