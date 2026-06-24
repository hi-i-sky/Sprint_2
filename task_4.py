class EmployeeSalary:

    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            calculated_hours = (7 - rest_days) * 8
        else:
            calculated_hours = hours
        return cls(name, calculated_hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            generate_email = f'{name}@email.com'
        else: generate_email = email
        return cls(name, hours, rest_days, generate_email)
    
    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment
    
    def salary(self):
        return self.hours * self.hourly_payment
    

    
#проверки:
#full_employee = EmployeeSalary('full_employee', 20, 0, 'full_employee@yandex.ru')
#print(full_employee.name, full_employee.hours, full_employee.rest_days, full_employee.email)
#print(full_employee.salary())

#full_employee_1 = EmployeeSalary.get_hours('full_employee_1', 10, 0, 'full_employee_1@yandex.ru')
#print(full_employee_1.name, full_employee_1.hours, full_employee_1.rest_days, full_employee_1.email)
#print(full_employee_1.salary())

#employee_without_hours = EmployeeSalary.get_hours('employee_without_hours', hours = None, rest_days = 1, email = 'employee_without_hours@yandex.ru')
#print(employee_without_hours.name, employee_without_hours.hours, employee_without_hours.rest_days, employee_without_hours.email)
#print(employee_without_hours.salary())

#employee_without_email = EmployeeSalary.get_email('employee_without_email', 40, 5, None)
#print(employee_without_email.name, employee_without_email.hours, employee_without_email.rest_days, employee_without_email.email)
#print(employee_without_email.salary())

#EmployeeSalary.set_hourly_payment(100)
#print(EmployeeSalary.hourly_payment)
#new_hourly_payment = full_employee.salary()
#print(new_hourly_payment)
