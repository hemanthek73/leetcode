# Write your MySQL query statement below
-- select s1.score, (select count(distinct score) from scores s2 where s2.score>=s1.score)  "Rank"
-- from scores s1
-- order by s1.score desc
select score,dense_rank() over(order by score desc)  "Rank" from scores