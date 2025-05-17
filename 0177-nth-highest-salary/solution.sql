CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    select
        salary
    into result
    from (
        with ranked_salary as (
            select
                salary,
                dense_rank() over (order by salary desc) rnk
            from Employee
        )
        select
            distinct salary as salary
        from ranked_salary
        where rnk = N
    );
    RETURN result;
END;
