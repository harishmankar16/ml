employess = LOAD 'employee.csv' USING PigStorage(",") as (eno:INT,ename:CHARARRAY,salary:FLOAT,dept:CHARARRAY,age:INT);
DUMP employee;

compt_emp = FILTER employess by dept == "Computer";
DUMP compt_emp;

age_under_30 = FILTER employess by age < 30;
DUMP age_under_30;

grouped_by_dept = GROUP employess by dept;
DUMP grouped_by_dept;

max_age_per_dept = FOREACH grouped_by_dept{
    max_age = MAX(employess.age)
    dept_employess = FILTER employess by age == max_age;
    GENERATE group as dept,dept_employess
}
DUMP max_age_per_dept