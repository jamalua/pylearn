class ProgStaff:
    companyName = 'ProgramingLab'

    def __init__(self,pSalary):
        self.salary = pSalary

    def printInfo(self):
        print("Company name is ",self.companyName)
        print("Salary is ",self.salary)

    @staticmethod
    def test():
        print("hello")


peter = ProgStaff(2500)
john = ProgStaff(3000)

print(peter.companyName)
print(john.companyName)

ProgStaff.companyName = "ProgrammingSchool"

print(peter.companyName)
print(john.companyName)

ProgStaff.salary = 500

print(peter.salary)
print(john.salary)

peter.printInfo()
john.printInfo()