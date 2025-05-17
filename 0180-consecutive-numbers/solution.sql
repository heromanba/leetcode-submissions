-- /* Write your PL/SQL query statement below */
with temp as (
    select 
        id,
        num,
        lag(num, 1) over(order by id) num_first,
        lag(num, 2) over(order by id) num_last
    from Logs
)
select * from (
    select
        distinct num as ConsecutiveNums
    from temp
    where num_first = num
    and num_last = num
    and id >= 3
);

