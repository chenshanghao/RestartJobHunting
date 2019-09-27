CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
Set M = N-1;
  RETURN (
      # Write your MySQL query statement below.
    Select Distinct Salary 
    From Employee 
    Order By Salary Desc 
    Limit 1 Offset M
  );
END