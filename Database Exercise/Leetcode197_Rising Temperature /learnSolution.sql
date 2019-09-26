# Write your MySQL query statement below

SELECT t1.Id
FROM Weather as t1 INNER JOIN Weather as t2
ON TO_DAYS(t1.RecordDate) = TO_DAYS(t2.RecordDate) + 1
WHERE t1.Temperature > t2.Temperature;