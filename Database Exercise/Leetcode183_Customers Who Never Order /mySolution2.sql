# Write your MySQL query statement below
Select Name as Customers
From Customers
Where Id not in (Select Distinct CustomerId From Orders);

