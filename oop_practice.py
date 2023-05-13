class Point(object):
    def __new__(cls, *args, **kwargs):
        print("From new")
        print(cls)
        obj = super().__new__(cls)
        return obj

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print(self)

    def distance(self):
        """Find distance from origin"""
        return (self.x**2 + self.y**2) ** 0.5


p1 = Point(4, 2)
print(p1.distance())
print(Point.distance(p1))

print(type(Point.distance))
print(type(p1.distance))
