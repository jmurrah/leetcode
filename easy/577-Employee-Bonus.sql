-- Write a solution to report the name and bonus amount of each employee with a bonus less than 1000.

-- Return the result table in any order.


-- Write your MySQL query statement below
SELECT name, bonus
FROM Employee
LEFT JOIN Bonus ON Employee.empId = Bonus.empId
WHERE bonus < 1000 OR bonus IS NULL
