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

13.  find all employeees whose name contains the word 'Rich' regardless of the case \
select name from employee
where lower(name) like 'rich'

14. is it safe to use **Rowid** to locate a record i Oracle SQL?

15. what is pseudocolumn? \
Rowid and rownum are two popular pseudocolumns

16. what are the reasons for denormalizing the data? \
For better performance especially when we join tables

17. what is the feature in sql for writing if/else statements? \
**case**

18. the difference between **delete** and **truncate**? \
Delete: data manipulation language; Delete one or more rows; after delete we have to issue **commit** or **rollback** to confirm changes
truncate: data definition language: delete all the rows; no need to **commit** and changes done cannot be rolled back.

19. what is the difference among ddl and dml? \
ddl: create and define the data; (create,alter, drop, truncate,rename); need **commit**; since each ddl is permanent, we cannot run multiple ddl statements in a group like **Transaction**; After ddl, no triggers are fired; 
dml: manage the data; (select,  insert, delete, update, merge, call); no need **commit**; after dml, relevant triggers are fired;

20. why do we use escape characterss in sql queries? \
some characters like '&' has meaning in sql

21. the difference between unique key and foreign key? \
number \
null value \
unique identifier \
changes \
usage 

22. what is the difference between inner join and outer join? \
23. the difference between left outer join and right outer join? \
24. what is the data type for rowid? \
string 

25. the difference between where and having? \
26. what is the cardinality in sql? \
in sql, cardinality is the uniquenesss of data valuesin a column. if cardinality is low, then a column will have more duplicated values

27.  ** merge** statement: \
28. ** union ** and **union all**:

29. when we do **select**, we get null value also.

30. alias cannot be used in **where** clause.

31. **where** clause doesn't automatically conditioned on **Null** values \
select * from employee \
where id NOT IN ( \
select depid from department \
where depid IS NOT NULL)
 
32. what is the use of execution plan in sql?

33. select * from a, b return len(a) * len(b) records. **Cartesian product**

34. switch \
Update employee **SET** deptid = **case** deptid when 2 then 1 when 1 then 2

35. get employee name, manager id and number of employees in the department. \
**self join** \
with d_count as ( \
select deptid, count(*) as d_count \
from employee \
group by deptid) \
select e.name as employZee_name, \
m.name as Manager_name, dc.d_count as dept_count \
from employee e, \
d_count dc, \
employee m \
where e.deptid = dc.deptid and e.mgrid = m.id

36. find duplicate rows in a database \
**ask the duplicate criteria** \
use **group by** then **count()**

37. delete duplicates: **deduplicate**\
oracle: use **rowid** \
delete from table table a\
where a.rowid > \
any( select b.rowid from table b \
where a.column_1 = b.column_1 \
and \
a.column_2 = b.column_2) 

38.  the difference betweeen NVL and NVL2 \
NVL(item to check, alternative_value): if item to check is NULL, then alternate value is returned. If item to check is not NULL, then item to check is returned. \
NVL2(item to check, alternate_value1, alternate_value2): if null, alternate_value2. else alternate_valu1

39. **ACID** properties in a sql transaction: \
Atomicity: all or nothing. If any part of transaction is failed, then whole of the transaction is rolled back. If all the parts of transactions are successful, then only Transaction is commited. \
consistency: once the transaction is complete, it should satisfy all the constraints, triggers, rules etc. \
isolation: each transaction can be executed separately; \
durability: transactions are permanent.

40. difference between **rank** and **dense_rank**: \
(10,10,20,30,30,40) \
rank: 1,1,3,4,4,6 \
dense rank: 1,1,2,3,3,4

41. what is the use of **WITH** clause in sql: \
**With** is used to create a subquery or view for a set of data \
With fin_employee as (select * from employee where dep_name = 'Finance') \
select * from fin_employee where age <30 union all \
select * from fin_employee where gender = 'Female'

42. which sql feature can be used to view data in a table sequentially?
sequence based on column value: order by \
sequence based on rows from data: **CURSOR**

43. get student name and number of students in same grade: \
select a.grade, a.count(*) as student_number from table a left outer join (select name, grade from table b) \
where a.grade = b.grade \
group by grade

44. get the list of grades with total score more than average score. \

 


