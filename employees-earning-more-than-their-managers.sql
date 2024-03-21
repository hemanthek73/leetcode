# Write your MySQL query statement below
select e1.name as Employee
from Employee e1
left join Employee e2 on e2.id=e1.managerId
where e2.salary<e1.salary