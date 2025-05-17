/* Write your PL/SQL query statement below */
select
    ee.name as Employee
from Employee ee
join Employee manager on ee.managerId = manager.id and ee.salary > manager.salary
