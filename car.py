class Car:
    def __init__(self, pMake, pModel, pColor, pPrice):
        self.make = pMake 
        self.model = pModel 
        self.color = pColor 
        self.price = pPrice
    
    def __str__(self):
        return 'Make = %s, Model = %s, Color = %s, Price = %s' %(self.make, self.model, self.color, self.price)
    
    def selectColor(self):
        self.color = input('What is the new color? ')
    
    def calculateTax(self):
        priceWithTax = 1.1*self.price 
        return priceWithTax
    
myFirstCar = Car('Honda','Civic','White',15000)
print(myFirstCar)
myFirstCar.price = 18000
print(myFirstCar)
myFirstCar.selectColor()
tax = myFirstCar.calculateTax()
print(tax)

class Room:
    def __init__(self, pSize, pView, pType, pBasicRates):
        self.size = pSize
        self.view = pView
        self.type = pType
        self.basicrates = pBasicRates
    
    def __str__(self):
        return 'Size = %s, View = %s, Type = %s, Basic Rates = %s' %(self.size, self.view, self.type, self.basicrates)

    def calculateRates(self, day):
        if day.lower() == 'weekend':
            return self.basicrates*1.5
        elif day.lower() == 'public holidays':
            return self.basicrates*2
        elif day.lower() == 'christmas':
            return self.basicrates*2.5
        else:
            return self.basicrates
    
room1 = Room(132,'City','double',120)
print(room1)
print(room1.calculateRates('Public Holidays'))    


class HumanResource:
    def __init__(self, pName, pSalary, pBonus):
        self.name = pName
        self.salary = pSalary 
        self._bonus = pBonus

    def __str__(self):
        return 'Name = %s, Salary = %.2f, Bonus = %.2f' %(self.name, self.salary, self._bonus)

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self,value):
        if value < 0:
            return 'value cannot be less than 0'
        else:
            return value

        




