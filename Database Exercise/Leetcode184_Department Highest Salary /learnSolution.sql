# Write your MySQL query statement below
SELECT D.name AS 'Department', E.name AS 'Employee', Salary
FROM Employee as E JOIN Department as D ON E.DepartmentId = D.Id
WHERE
    (E.DepartmentId , E.Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
    )
;