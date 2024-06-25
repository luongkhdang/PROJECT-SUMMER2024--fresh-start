"""
classes

Numbers
Strings
Booleans
----
Lists
Dictionaries

point1.x = 10    this is to assign an attribute

"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1 = Point(10,20) #create the object
point1.draw()
print(point1.x)