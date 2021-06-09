from employee import *

# -----------------------------
# class dev kế thừa từ class employee
# -----------------------------
class dev(employee):

  # Phương thức khởi tạo mặc định ghi đè
  def __init__(self, id, full_name, dob, phone, salary, shifts):
    # Gọi lại phương thức khởi tạo của lớp cha
    super().__init__(id, full_name, dob, phone, salary, shifts)
    # Khởi tạo các thuộc tính mới (Nếu mở rộng thêm)
  
  # Phương thức nhập thông tin từ bàn phím ghi đè
  def import_info(self):
    self.__init__(id = None,
                  full_name = None,
                  dob = None,
                  phone = None,
                  salary = None,
                  shifts = None)
    print("--Nhập thông tin của des--")
    self.id = input("id: ")
    self.full_name = input("full_name: ")
    self.dob = input("dob: ")
    self.phone = input("phone: ")
    self.salary = input("salary: ")
    self.shifts = input("shifts: ")
    return self

  # Phương thức xuất thông tin
  def export_info(self):
    return [self.id, self.full_name, self.dob, self.phone, self.salary, self.shifts]

  # Phương thức tính lương ghi đè
  def calculate_salary(self):
    extra = self.shifts*400000
    total = self.salary + extra
    return [extra, total]