class Myclass:
    def method(self):
        return 'instance method called', self
    
    @classmethod
    def classmethod(cls):
        return 'class method called', cls
    
    @staticmethod
    def staticmethod():
        return 'static method called'


obj = Myclass()

print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())

print(Myclass.staticmethod())
print(Myclass.classmethod())
print(Myclass.method(obj))

#This will not work as it requires the instance of the class
#print(Myclass.method())
