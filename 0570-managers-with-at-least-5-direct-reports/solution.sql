/* Write your PL/SQL query statement below */
select 
    mgr.name
from employee ee
join employee mgr on ee.managerId = mgr.id
group by mgr.id, mgr.name
having count(1) >= 5
