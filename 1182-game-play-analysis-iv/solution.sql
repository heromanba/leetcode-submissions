/* Write your PL/SQL query statement below */
with target_user as (
    select
        player_id,
        first_value(event_date) over (partition by player_id order by event_date) as first_login,
        nth_value(event_date, 2) over (partition by player_id order by event_date) as second_login
    from activity
)
select round(
    (select count(distinct player_id) from target_user where first_login = second_login - 1)/(select count(distinct player_id) from activity),
    2
) as fraction
from dual;
