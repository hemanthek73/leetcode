# Write your MySQL query statement below
select Request_at as Day,
round(sum(if(status!="completed",1,0))/count(status),2) as "Cancellation Rate"
from Trips
where Request_at between "2013-10-01" and "2013-10-03"
and Client_id not in (select Users_id from Users where Banned="yes")
and Driver_id not in (select Users_id from Users where Banned="yes")
group by Request_at