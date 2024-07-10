class Point:

    def __init__(self, x, y):
        print(f"Creating a new point with coordinates {x} & {y}")
        self.x = x
        self.y = y

    def shift(self, x, y):
        self.x = self.x + x
        self.y = self.y + y    
        
p = Point(10, 20)

p.shift(2, 3) 
print(p.x) 
print(p.y) 

p2 = Point(20, 50)

print(p2.x, p2.y)