class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@email.com"
        self.pay = pay

        Employee.num_of_emps += 1

    def __repr__(self):
        return str(
            {
                "FullName": f"{self.first} {self.last}",
                "Email": self.email,
                "Pay": self.pay,
            }
        )

    # This method will only change the raise_amt for the instance
    def applyraise(self):
        self.raise_amt = 1.05
        self.pay = int(self.pay * self.raise_amt)

    def applyraise2(self):
        Employee.raise_amt = 1.06
        self.pay = int(self.pay * Employee.raise_amt)


emp_1 = Employee("John", "Smith", 50000)
emp_2 = Employee("Joe", "Blogs", 60000)

print(repr(emp_1))

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print("\n")

# emp_1.applyraise()
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print("\n")

emp_2.applyraise2()
print(Employee.raise_amt)
print(emp_1.raise_amt)  # Will retain its value for raise_amt to 1.05
print(emp_2.raise_amt)
print("\n")

Employee.raise_amt = 1.07
print(Employee.raise_amt)
print(emp_1.raise_amt)  # Will retain its value for raise_amt to 1.05
print(emp_2.raise_amt)
print("\n")

emp_1.raise_amt = 1.08
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print("\n")


emp_2.raise_amt = 1.09
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print("\n")

print(Employee.num_of_emps)
print("\n")

print(dir(emp_1))
print(dir(emp_2))

# print(emp_1)
# print(emp_2)
