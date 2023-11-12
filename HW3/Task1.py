# 1) Переписать код в соответствии с Single Responsibility Principle:
# Подсказка: вынесите метод calculateNetSalary() в отдельный класс

from datetime import date


class Employee:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def get_emp_info(self):
        return f"name - {self.name}, dob - {self.dob}"


class SalaryCalculator:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_net_salary(self):
        tax = int(self.base_salary / 4)  # рассчитать налог другим способом
        return self.base_salary - tax
