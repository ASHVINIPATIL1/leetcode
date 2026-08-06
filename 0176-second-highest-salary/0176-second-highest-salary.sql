# Write your MySQL query statement below
SELECT max(salary) AS SecondHighestSalary
FROM Employee
where salary < (SELECT MAX(salary)
FROM Employee );
