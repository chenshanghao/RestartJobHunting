# Write your MySQL query statement below
update salary
set sex = Case when sex = 'm' then 'f'
               else 'm' end;