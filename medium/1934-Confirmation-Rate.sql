-- The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested 
-- confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0. 
-- Round the confirmation rate to two decimal places.

-- Write a solution to find the confirmation rate of each user.

-- Return the result table in any order.


-- Write your MySQL query statement below
SELECT s.user_id, ROUND(AVG(IF(c.action = 'confirmed', 1, 0)), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON c.user_id = s.user_id
GROUP BY s.user_id
