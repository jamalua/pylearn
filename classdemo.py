class Staff:
    def __init__(self,pPosition,pName,pPay):
        self.position = pPosition
        self.name = pName
        self.pay = pPay
        print("CreatedObject")

    def __str__(self):
        return "Position = %s, Name = %s, Pay = %d" %(self.position, self.name, self.pay)

    def calculatePay(self):
        prompt = "\nEnter number of hours worked for %s " %(self.name)
        hours = input(prompt)
        prompt = 'Enter the hourly rate for %s ' %(self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours)*int(hourlyRate)
        return self.pay


officeStaff1 = Staff('Basic','Jamal', 10)
print(officeStaff1.calculatePay())
print(officeStaff1)

