-- Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".

-- Return the result table ordered by rating in descending order.


-- Write your MySQL query statement below
SELECT *
FROM Cinema c
WHERE c.id % 2 = 1 AND c.description != 'boring'
ORDER BY c.rating DESC
