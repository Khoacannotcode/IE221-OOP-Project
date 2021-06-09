from employee import *

# -----------------------------
# class des kế thừa từ class employee
# -----------------------------
class des(employee):

  # Phương thức khởi tạo mặc định ghi đè
  def __init__(self, id, full_name, dob, phone, salary, shifts, per):
    # Gọi lại phương thức khởi tạo của lớp cha
    super().__init__(id, full_name, dob, phone, salary, shifts)
    # Khởi tạo các thuộc tính mới
    self.per = per
  
  # Phương thức nhập thông tin từ bàn phím ghi đè
  def import_info(self):
    self.__init__(id = None,
                  full_name = None,
                  dob = None,
                  phone = None,
                  salary = None,
                  shifts = None,
                  per = None)
    print("--Nhập thông tin của des--")
    self.id = input("id: ")
    self.full_name = input("full_name: ")
    self.dob = input("dob: ")
    self.phone = input("phone: ")
    self.salary = input("salary: ")
    self.shifts = input("shifts: ")
    self.per = input("per: ")
    return self

  # Phương thức xuất thông tin
  def export_info(self):
    return [self.id, self.full_name, self.dob, self.phone, self.salary, self.shifts, self.per]

  # Phương thức tính lương ghi đè
  def calculate_salary(self):
    extra = self.shifts*220000 + self.salary*self.per
    total = self.salary + extra
    return [extra, total]