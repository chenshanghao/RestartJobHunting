# Write your MySQL query statement below
Select *
From cinema
Where description != 'boring' and id % 2 = 1
Order by rating Desc;
