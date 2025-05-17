/* Write your PL/SQL query statement below */
with all_trips as (
    select
        request_at,
        sum(
            case 
                when t.status != 'completed'
                then 1
                else 0
            end
        ) as cancelled_trips,
        sum(1) as total_trips
    from trips t
    join users c on t.client_id = c.users_id and c.banned != 'Yes'
    join users d on t.driver_id = d.users_id and d.banned != 'Yes'
    where to_date(t.request_at, 'yyyy-mm-dd') between to_date('2013-10-01', 'yyyy-mm-dd') and to_date('2013-10-03', 'yyyy-mm-dd') 
    group by t.request_at
)
select
    request_at as "day",
    round(cancelled_trips / total_trips, 2) as "Cancellation Rate"
from all_trips;

