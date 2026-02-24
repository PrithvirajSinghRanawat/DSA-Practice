class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Answer():
    def isRectangleOverlap(self, L1, R1, L2, R2):
        # If one rectangle is on left side of other
        if L1.x >= R2.x or L2.x >= R1.x:
            return False

        # If one rectangle is above other
        if L1.y <= R2.y or L2.y <= R1.y:
            return False

        return True
    

a = Answer()
print(f"L1(0,10), R1(10,0), L2(5,5), R2(15,0) Does Rectangle Overlap: {a.isRectangleOverlap(Point(0, 10), Point(10, 0), Point(5, 5), Point(15, 0))}") 
print(f"L1(0,10), R1(10,0), L2(10,10), R2(20,0) Does Rectangle Overlap: {a.isRectangleOverlap(Point(0, 10), Point(10, 0), Point(10, 10), Point(20, 0))}")