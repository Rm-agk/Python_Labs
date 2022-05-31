class Employee:
    def __init__(self, name, job_desc, salary):
        self.name = name
        self.job_desc = job_desc
        self.salary = salary

    def net_salary(self):
        net_salary = float(self.salary) * 0.8
        return "Net Salary: " + str(net_salary)

name = input("Enter the employee name:\n")
job_desc = input("Enter the employee job description:\n")
salary = input("Enter the employee salary:\n")

ObjectName = Employee(name, job_desc, salary)
net_salary = ObjectName.net_salary()
print(str(net_salary))