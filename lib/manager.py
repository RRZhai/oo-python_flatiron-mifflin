from lib.employee import Employee

class Manager:
    all = []
    all_departments = []
    def __init__(self, name, department, age):
        self.name = name
        self.department = department
        self.age = age
        type(self).all.append(self)
        if self.department not in type(self).all_departments:
            type(self).all_departments.append(self.department) 

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str:
            self._name = name 
        else:
            raise TypeError('name must be a str')

    @property
    def department(self):
        return self._department
    
    @department.setter
    def department(self, department):
        if type(department) == str:
            self._department = department
        else:
            raise TypeError('department must be a str')

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if type(age) == int:
            self._age = age
        else:
            raise TypeError('age must be a int')

    def employees(self):
        return [employee for employee in Employee.all if employee.manager_name == self]
    
    def hire_employee(self, name = '', salary = 0):
        return Employee(name, salary, self.name)
    
    def average_age():
        return sum((manager.age for manager in Manager.all))/len(Manager.all)