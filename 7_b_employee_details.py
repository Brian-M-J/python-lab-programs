# Create Employee class. Create and display employee details and update salary
class Employee:
    def __init__(self):
        self.name = ""
        self.empId = ""
        self.dept = ""
        self.salary = ""
    
    def getEmpDetails(self):
        self.name = input("Enter Employee name: ")
        self.empId = input("Enter Employee ID: ")
        self.dept = input("Enter Employee Dept: ")
        self.salary = int(input("Enter Employee Salary: "))
    
    def showEmpDetails(self):
        print("Employee Details")
        print(f"Name: {self.name}")
        print(f"ID: {self.empId}")
        print(f"Dept: {self.dept}")
        print(f"Salary: {self.salary}")
    
    def updtSalary(self):
        self.salary = int(input("Enter new Salary: "))
        print(f"Updated Salary: {self.salary}")

e1 = Employee()
e1.getEmpDetails()
e1.showEmpDetails()
e1.updtSalary()
