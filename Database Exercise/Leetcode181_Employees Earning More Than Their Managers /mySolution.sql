# Write your MySQL query statement below
Select E3.Name as Employee
From
(
Select E1.Id, E1.Name, E1.Salary, E1.ManagerId, E2.Salary as ManagerSalary
From Employee E1 left join Employee E2
On E1.ManagerId = E2. Id
) as E3
Where E3.Salary > E3.ManagerSalary;
