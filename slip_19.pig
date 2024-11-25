students = LOAD '/students_data.txt' Using PigStorage(',') AS (id:INT,firstname:CHARARRAY,lastname:CHARARRAY,age:INT,phone:CHARARRAY,city:CHARARRAY)

DUMP students;

DESCRIBE students

group_by_age = GROUP students BY age
DUMP group_by_age

group_by_all_columns = GROUP students by (id,firstname,lastname,age,phone,city)
DUMP group_by_all_columns

group_by_city = GROUP students by city
city_avg_age = FOREACH group_by_city GENERATE group as city,AVG(students.age) as avg_age;
DUMP city_avg_age;