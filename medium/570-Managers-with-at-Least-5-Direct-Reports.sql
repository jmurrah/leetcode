-- Write a solution to find managers with at least five direct reports.

-- Return the result table in any order.


-- Write your MySQL query statement below
SELECT e.name
FROM Employee m, Employee e
WHERE e.id = m.managerId
GROUP BY m.managerId
HAVING COUNT(*) > 4
