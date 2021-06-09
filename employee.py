# -----------------------------
#       CLASS employee
# -----------------------------
class employee:

  # Phương thức khởi tạo mặc định
  def __init__(self, id, full_name, dob, phone, salary, shifts):
    self.id = id
    self.full_name = full_name
    self.dob = dob
    self.phone = phone
    self.salary = salary
    self.shifts = shifts

  # Phương thức ảo nhập thông tin
  def import_info(self):
    pass

  # Phương thức ảo xuất thông tin
  def export_info(self):
    pass

  # Phương thức ảo cập nhật thông tin
  def update_info(self):
    pass

  # Phương thức ảo tính lương
  def calculate_salary(self):
    pass