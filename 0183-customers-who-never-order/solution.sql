/* Write your PL/SQL query statement below */
select 
    c.name as Customers
from Customers c 
where NOT EXISTS (select * from Orders where customerId=c.id)
