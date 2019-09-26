# Write your MySQL query statement below
Select C.Name as Customers
From Customers as C left join Orders as O on C.Id = O.CustomerId
Where O.CustomerId is Null

