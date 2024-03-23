# Write your MySQL query statement below
select Department.name as "Department",e.name as "Employee",e.Salary from
(select DepartmentId,name,Salary,dense_rank() over(partition by DepartmentId order by Salary desc)as r
from Employee) e
join Department on e.DepartmentId=Department.Id
where r<=3