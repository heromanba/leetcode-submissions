/* Write your PL/SQL query statement below */

delete 
from person 
where id in (
    with person_to_delete as (
        select 
            id,
            email,
            row_number() over (partition by email order by id asc) as rn
        from person
    )
    select
        distinct id
    from person_to_delete
    where rn > 1
)
