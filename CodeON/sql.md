1. get the second highest salary among all employees: \
select max(salary) from employee \
order by salary desc \
limit 1  \
where salary NOT IN ( \
select max(salary) from exmployee) \
Otherwise: \
select max(salary) from employee \
where salary <> ( \
select max(salary) from employee

2. How can we retrieve alternate records from a table in oracle? \
**functions: rownum()  mod()** \
to get even number records: \
select * from (select rownum, id, name from employee) \
where mod(rownum,2)=0

3. find max salary and department name from each department \  
select d.name, max(e.salary) as max_salary from Department d left outer join employee e \
on e.depid = d.id \
group by d.name

4. find records in table a that are not in table b without using NOT IN operator \
select * from a \
**Minus** \
select * from b \

5. In sql, null cannot be compared with itself. Therefore, null =  null is not true. We can compare null with a 
non-null value to check whether a value **is null**

6. find employees having the same name and email: **find duplicates**  
select name, count(*) from employee \
group by name, email \
**having** count(*) >1 \

7. find max salary from each department
select depid, max(salary) from department \
group by depid

8. get the nth hghest salary among all employees
* use subquery: 
select max(salary) from employee \
where salary NOT IN (select salary from employee order by salary desc limit n-1) \

9. find 10 employees with odd number as employee id \
select id from employee \
where mod(id, 2) != 0 \
limit 10 \
select id from employee \
where id%2 =1 and rownum<11

10. get the names of employees whose date of birth is between 01/01/1990 to 31/21/2000 \
select name from employee \
where dob **between** '01/01/1990' **and** '31/12/2000'

11. get the **quarter** from date \
select **to_char**(**to_date**('3/31/2006', 'M/DD/YYYY'),'Q') AS quarter \
from dual

12. find employees with duplicate email \
select name, count(email) as cnt from employee \
group by name \
**having** cnt>1

13. 


