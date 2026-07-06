# python code

import csv
import json

class Person:
  def __init__(self, name, emp_id):
    self.name = name 
    self.id = emp_id
class Employee(Person):
  def __init__(self, name, emp_id, salary):
    super().__init__(name, emp_id)
    self.salary = float(salary)
  def calculate_salary(self):
    return self.salary
class Manager(Employee):
  def ___init__(self, name, emp_id, salary, bonus):
    super().__init__(name, emp_id, salary)
    self.bonus = float(bonus)

  def calculate_salary(self):
    return self.salary + self.bonus
class FileHandler:
  def read_csv(self, filename):
    try:
      with open(filename, "r") as f:
      return list(csv.DictReader(f)) 
    except Exception as e:
      print(e)
      return[]
  def read_json(self, filename):
    try:
      with open(filename, "r") as f:
        return json.load(f)
    except Exception as e:
      print(e)
      return {}
class ReportGenerator:
  def generate_summary(self, employees):
    for emp in employees:
      salary =  emp.calculate_salary()
      status = "Hihg Income" if salary > 50000 else "Normal"
      print(emp.name, salary, status)
  def save_output(self, employees):
    with open("report.txt","w") as f:
      for emp in employees:
        salary =  emp.calculate_salary()
        status = "Hogh Income" if salary > 50000 else "Normal"
        f.write(f"{emp.name},{salary},{status}\n")
  fh = FileHandler()
  employees_data = fh.read_csv("employee.csv")
  bonus_data = fh.read_json("bonus.json")

employees = []
for row in employees_data:
  try:
    bonus = bonus_data.get(row["id"], 0)
    emp = Manager(row["name"],row["id"], row["salary"], bonus)
    employees.append(emp)
  except Exception:
    print("Invalid data")

report = ReportGenerator()
report.generate_summary(employees)
report.save_output(employees)

