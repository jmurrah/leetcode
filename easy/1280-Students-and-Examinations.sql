-- Write a solution to find the number of times each student attended each exam.

-- Return the result table ordered by student_id and subject_name.


-- Write your MySQL query statement below
SELECT st.student_id, st.student_name, su.subject_name, COUNT(ex.student_id) as attended_exams
FROM Students st
CROSS JOIN Subjects su
LEFT JOIN Examinations ex ON ex.student_id = st.student_id AND ex.subject_name = su.subject_name
GROUP BY st.student_id, st.student_name, su.subject_name
ORDER BY st.student_id, st.student_name, su.subject_name
