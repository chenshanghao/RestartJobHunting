# Write your MySQL query statement below
Select p.FirstName, p.LastName, a.City, a.State
From Person as p left join Address as a
on p.PersonId = a.PersonId;