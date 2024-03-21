# Write your MySQL query statement below
select distinct a.Num as ConsecutiveNums from Logs a
join Logs b on a.id=b.id+1 and a.Num=b.Num
join Logs c on a.id=c.id+2 and a.Num=c.Num