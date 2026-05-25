#12-m
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary

m1 = Employee("John", 20000)
print(m1.salary)

res = m1.salary
print(res)

m1.salary = 1000
print(m1.salary)
