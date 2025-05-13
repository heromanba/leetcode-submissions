select (
    (
        select distinct salary
        from (
            select 
                salary,
                dense_rank() over ( order by salary desc ) as rnk
            from Employee
        )
        where rnk = 2
    )
) as SecondHighestSalary
from dual
