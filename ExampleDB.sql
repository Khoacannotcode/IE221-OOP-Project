
create database database_thi

use database_thi

drop database database_thi

CREATE TABLE des
(
    id nvarchar(64),
	full_name nvarchar(200),
    birth_date date,
    phone varchar(16),
	salary float,
	shifts int,
	per float,
	PRIMARY KEY(id)
)

INSERT INTO des(id, full_name, birth_date, phone, salary, shifts, per) VALUES(80265, N'Nguyễn Văn Ngọc', '1990-04-15', '0996283309', 6300000, 19, 0.3)
INSERT INTO des(id, full_name, birth_date, phone, salary, shifts, per) VALUES(80266, N'Trịnh Ngọc Tân', '1991-08-20', '0936263334', 6700000, 12, 0.3)
INSERT INTO des(id, full_name, birth_date, phone, salary, shifts, per) VALUES(80267, N'Dương Văn An', '1990-04-12', '0976263889', 6300000, 11, 0.3)
INSERT INTO des(id, full_name, birth_date, phone, salary, shifts, per) VALUES(80268, N'Võ Tài Ngân', '1992-08-30', '0996263345', 6300000, 12, 0.7)
INSERT INTO des(id, full_name, birth_date, phone, salary, shifts, per) VALUES(80269, N'Châu Thanh Hùng', '1990-06-27', '0976263305', 6800000, 12, 0.3)
INSERT INTO des(id, full_name, birth_date, phone, salary, shifts, per) VALUES(80270, N'Trần Văn Thức', '1990-04-20', '0926263850', 6900000, 18, 0.3)
INSERT INTO des(id, full_name, birth_date, phone, salary, shifts, per) VALUES(80271, N'Nguyễn Bửu Hòa', '1994-02-11', '0976263355', 6200000, 45, 0.9)
INSERT INTO des(id, full_name, birth_date, phone, salary, shifts, per) VALUES(80272, N'Phạm Thanh Phương', '1990-03-10', '0926268335', 6300000, 12, 5.3)
INSERT INTO des(id, full_name, birth_date, phone, salary, shifts, per) VALUES(80273, N'Thái Hồng Ngọc', '1997-08-28', '0956263355', 6100000, 15, 0.3)
INSERT INTO des(id, full_name, birth_date, phone, salary, shifts, per) VALUES(80264, N'Vũ Thị Phương', '1990-01-20', '0936268349', 6400000, 10, 1.3)

select * from des



CREATE TABLE dev
(
    id nvarchar(64),
	full_name nvarchar(200),
    birth_date date,
    phone nvarchar(16),
	salary float,
	shifts int,
	PRIMARY KEY(id)
)

INSERT INTO dev(id, full_name, birth_date, phone, salary, shifts) VALUES(80281, N'Phạm Ngọc Trâm', '1988-05-19', '0796213309', 6900000, 16)
INSERT INTO dev(id, full_name, birth_date, phone, salary, shifts) VALUES(80282, N'Nguyễn Lan Hương', '1987-04-15', '0996288309', 6300000, 11)
INSERT INTO dev(id, full_name, birth_date, phone, salary, shifts) VALUES(80283, N'Thái Vân Hân', '1989-02-27', '0996283309', 6100000, 24)
INSERT INTO dev(id, full_name, birth_date, phone, salary, shifts) VALUES(80284, N'Đào Ngọc Hùng', '1995-04-15', '0796283309', 6300000, 19)
INSERT INTO dev(id, full_name, birth_date, phone, salary, shifts) VALUES(80285, N'Phi Hùng Tâm', '1994-01-10', '0916213309', 6800000, 90)
INSERT INTO dev(id, full_name, birth_date, phone, salary, shifts) VALUES(80286, N'Đoàn Thanh Tân', '1990-04-25', '0996288309', 6500000, 23)
INSERT INTO dev(id, full_name, birth_date, phone, salary, shifts) VALUES(80287, N'Lý Vĩnh Hưng', '1988-06-19', '0796283389', 7800000, 10)
INSERT INTO dev(id, full_name, birth_date, phone, salary, shifts) VALUES(80288, N'Vương Kiều Đạt', '1986-09-23', '0916283389', 1000000, 45)

select * from dev

DROP TABLE dev
DROP TABLE des


GO
DROP TABLE IF EXISTS employee_salary;
GO
CREATE TABLE employee_salary(
[id] nvarchar(64),
[full_name] nvarchar(200),
[dob] date,
[phone] nvarchar(16),
[salary] float,
[extra] float,
[total] float
)

SELECT * FROM employee_salary

INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80264,N'Vũ Thị Phương','1990-01-20','0936268349',6400000,10520000,16920000)
INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80265,N'Nguyễn Văn Ngọc','1990-04-15','0996283309',6300000,6070000,12370000)
INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80266,N'Trịnh Ngọc Tân','1991-08-20','0936263334',6700000,4650000,11350000)
INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80267,N'Dương Văn An','1990-04-12','0976263889',6300000,4310000,10610000)
INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80268,N'Võ Tài Ngân','1992-08-30','0996263345',6300000,7050000,13350000)
INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80269,N'Châu Thanh Hùng','1990-06-27','0976263305',6800000,4680000,11480000)
INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80270,N'Trần Văn Thức','1990-04-20','0926263850',6900000,6030000,12930000)
INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80271,N'Nguyễn Bửu Hòa','1994-02-11','0976263355',6200000,15480000,21680000)
INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80272,N'Phạm Thanh Phương','1990-03-10','0926268335',6300000,36030000,42330000)
INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80273,N'Thái Hồng Ngọc','1997-08-28','0956263355',6100000,5130000,11230000)
INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80281,N'Phạm Ngọc Trâm','1988-05-19','0796213309',6900000,6400000,13300000)
INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80282,N'Nguyễn Lan Hương','1987-04-15','0996288309',6300000,4400000,10700000)
INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80283,N'Thái Vân Hân','1989-02-27','0996283309',6100000,9600000,15700000)
INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80284,N'Đào Ngọc Hùng','1995-04-15','0796283309',6300000,7600000,13900000)
INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80285,N'Phi Hùng Tâm','1994-01-10','0916213309',6800000,36000000,42800000)
INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80286,N'Đoàn Thanh Tân','1990-04-25','0996288309',6500000,9200000,15700000)
INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80287,N'Lý Vĩnh Hưng','1988-06-19','0796283389',7800000,4000000,11800000)
INSERT INTO employee_salary (id,full_name,dob,phone,salary,extra,total) VALUES(80288,N'Vương Kiều Đạt','1986-09-23','0916283389',1000000,18000000,19000000)
