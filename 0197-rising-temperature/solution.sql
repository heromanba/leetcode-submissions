/* Write your PL/SQL query statement below */
with cte as (
    select
        id,
        recordDate as curr_date,
        temperature as curr_temp,
        lag(recordDate, 1) over (order by recordDate) as prev_date,
        lag(temperature, 1) over (order by recordDate) as prev_temp
    from weather
)
select 
    * 
from (
    select id
    from cte
    where curr_temp > prev_temp
    and curr_date = prev_date + 1
);

