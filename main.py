import pyodbc
import os
import time

import pandas as pd
import numpy as np

from tqdm import tqdm
from des import *
from dev import *

clear = lambda: os.system('cls')
def wait():
  time.sleep(0.5)
  print("\n>>>ENTER")
  temp = input()
  return

def ConnectDatabase():
  # Kết nối tới CSDL
  drive = "SQL Server"
  server = "DESKTOP-ASCMUMM\SQLEXPRESS"
  database = "database_thi"
  username = ""
  password = ""
  str_sql = "DRIVER={0};SERVER={1};DATABASE={2};UID={3};PWD={4}".format(drive, server, database, username, password)

  cnxn = pyodbc.connect(str_sql)
  cursor = cnxn.cursor()

  # Truy vấn CSDL lấy dữ liệu của des_table và dev_table
  query = """SELECT * FROM des"""
  des_table = cursor.execute(query)
  employee_dict = {}
  # print("des_table")
  for row in des_table:
    print(row)
    employee_dict[row[0]] = des(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
  query = """SELECT * FROM dev"""
  dev_table = cursor.execute(query)
  # print("dev_table")
  for row in dev_table:
    print(row)
    employee_dict[row[0]] = dev(row[0], row[1], row[2], row[3], row[4], row[5])
  
  # for key in employee_dict:
  #   print(employee_dict[key])

  return employee_dict


def Print_Des_Dataframe(employee_dict):
  des_df = pd.DataFrame(columns =["id", "full_name", "dob", "phone", "salary", "shifts", "per"], index = None)
  for id in list(employee_dict.keys()):
    if type(employee_dict[id]) == des:
      row = employee_dict[id].export_info()
      des_df = des_df.append(dict(zip(des_df.columns,
                                                np.array(row))), ignore_index=True)
  print(des_df)

def Print_Dev_Dataframe(employee_dict):
  dev_df = pd.DataFrame(columns =["id", "full_name", "dob", "phone", "salary", "shifts"], index = None)
  for id in list(employee_dict.keys()):
    if type(employee_dict[id]) == dev:
      row = employee_dict[id].export_info()
      dev_df = dev_df.append(dict(zip(dev_df.columns,
                                                np.array(row))), ignore_index=True)
  print(dev_df)

def Calculate_Salary(employee_dict):
  # Tạo dataframe lưu lương của toàn bộ nhân viên
  employee_salary_df = pd.DataFrame(columns =["id", "full_name", "dob", "phone", "salary", "extra", "total"], index = None)
  # Tính lương của mỗi nhân viên
  for key in employee_dict:
    employee = employee_dict[key]
    extra, total = employee.calculate_salary()
    record = [employee.id, employee.full_name, employee.dob, employee.phone, employee.salary, extra, total]
    employee_salary_df = employee_salary_df.append(dict(zip(employee_salary_df.columns,
                                                            np.array(record))), ignore_index=True)
  return employee_salary_df

def Upload_Salary_To_Server(employee_salary_df):
  # Kết nối tới CSDL
  drive = "SQL Server"
  server = "DESKTOP-ASCMUMM\SQLEXPRESS"
  database = "database_thi"
  username = ""
  password = ""
  str_sql = "DRIVER={0};SERVER={1};DATABASE={2};UID={3};PWD={4}".format(drive, server, database, username, password)

  cnxn = pyodbc.connect(str_sql)
  cursor = cnxn.cursor()

  query = """CREATE TABLE employee_salary (id nvarchar(64), full_name nvarchar(200), dob date, phone nvarchar(16), salary float, extra float, total float,)"""
  cursor.execute(query)
  for index, row in employee_salary_df.iterrows():
    print(row)
    # debug = (row.id, row.full_name, row.dob, row.phone, row.salary, row.extra, row.total)
    # print(debug)
    cursor.execute("INSERT INTO employee_salary(id,full_name,dob,phone,salary,extra,total) VALUES({},{},{},{},{},{},{})".format(row.id, row.full_name, row.dob, row.phone, row.salary, row.extra, row.total))
  cnxn.commit()
  cursor.close()



def menu():
  employee_dict = {}
  employee_salary_df = pd.DataFrame(columns =["id", "full_name", "dob", "phone", "salary", "extra", "total"], index = None)
  ans=True
  while ans:
    clear()
    print("""
    0. Nhập thông tin nhân viên
    1. Khởi tạo, kết nối các đối tượng trong CSDL
    2. Xuất Des, dạng dataframe
    3. Xuất Dev, dạng dataframe
    4. Tính lương
    5. Cập nhật lương lên server
    6. Xuất danh sách lương trên server
    7. Cập nhật giờ tăng ca thông qua id
    8. Cập nhật phần trăm thưởng cho des có thêm sáng kiến
    9. Thoát chương trình
    =============================================
    """)
    ans=input("Lựa chọn: ")
    if ans=="0":
      print("0. Nhập thông tin nhân viên")
      employee_type = input("Chọn lớp nhân viên cần nhập (1-designer; 2-developer): ")
      if employee_type == "1":
        new_employee = des(None, None, None, None, None, None, None)
      elif employee_type == "2":
        new_employee = dev(None, None, None, None, None, None)
      new_employee.import_info()
      employee_dict[new_employee.id] = new_employee
      print("Hoàn tất")
      wait()

    elif ans=="1":
      print("1. Khởi tạo, kết nối các đối tượng trong CSDL")
      print("Tiến hành khởi tạo")
      for i in tqdm(range(50)):
        time.sleep(0.005)
      print("Tiến hành kết nối các đối tượng trong CSDL")
      for i in tqdm(range(100)):
        time.sleep(0.002)
      employee_dict = ConnectDatabase()
      print("Hoàn tất")
      wait()

    elif ans=="2":
      print("2. Xuất Des, dạng dataframe")
      Print_Des_Dataframe(employee_dict)
      wait()

    elif ans=="3":
      print("3. Xuất Dev, dạng dataframe")
      Print_Dev_Dataframe(employee_dict)
      wait()

    elif ans=="4":
      print("4. Tính lương")
      print("Tiến hành tính lương nhân viên ...")
      for i in tqdm(range(50)):
        time.sleep(0.002)
      employee_salary_df = Calculate_Salary(employee_dict)
      print("Hoàn tất")
      wait()

    elif ans=="5":
      print("5. Cập nhật lương lên server")
      print("Tiến hành cập nhật dữ liệu lên server")
      for i in tqdm(range(50)):
        time.sleep(0.002)
      Upload_Salary_To_Server(employee_salary_df)
      print("Hoàn tất")
      wait()

    elif ans=="6":
      print("6. Xuất danh sách lương trên server")
      print("Tiến hành tính lương nhân viên ...")
      for i in tqdm(range(50)):
        time.sleep(0.002)
      employee_dict = ConnectDatabase()
      print("Hoàn tất")
      wait()
    elif ans=="9":
        print("Đang thoát chương trình...")
        time.sleep(1)
        print("Tạm biệt, hẹn gặp lại.")
        ans = None
    else:
        print("\nLựa chọn không hợp lệ, xin vui lòng nhập lại")
        wait()
menu()