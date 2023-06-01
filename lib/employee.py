

class Employee:
    all = []
    def __init__(self, name, salary, manager_name):
        self.name = name
        self.salary = salary
        self._manager_name = manager_name
        type(self).all.append(self)

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
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if type(salary) == int:
            self._salary = salary 
        else:
            raise TypeError('salary must be a str')
        
    @property
    def manager_name(self):
        return self._manager_name
    
    @manager_name.setter
    def manager_name(self, manager_name):
        if type(manager_name) == str:
            self._manager_name = manager_name
        else:
            raise TypeError('manager_name must be a str')
        
    def paid_over(sal = 0):
        return [employee.name for employee in Employee.all if employee.salary > sal]
    
    def find_by_department(search = ''):
        from lib.manager import Manager
        for manager in Manager.all:
            if manager.department == search:
                return manager.employees()[0]
            
    def tax_bracket(self):
        return [employee for employee in type(self).all if self.name != employee.name and abs(self.salary - employee.salary) <= 1000]