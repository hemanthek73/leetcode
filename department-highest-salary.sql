# Write your MySQL query statement below
select Department.name as Department,Employee.Name as Employee,Salary
from Employee Join Department on Employee.DepartmentId=Department.Id
where
(select DepartmentId, max(Salary) from Employee
group by DepartmentId)