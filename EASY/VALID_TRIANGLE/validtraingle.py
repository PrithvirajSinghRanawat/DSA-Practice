class Answer:
    def checktriangle(self, side1, side2, side3):
        if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1): #checking the triangle inequality theorem
            return "Invalid Triangle"
        else:
            return "Valid Triangle"
        
a = Answer()
print(f"Sides of the triangle are 3, 4, 5: {a.checktriangle(3, 4, 5)}") # Valid Triangle
print(f"Sides of the triangle are 1, 2, 3: {a.checktriangle(1, 2, 3)}") # Invalid Triangle
print(f"Sides of the triangle are 5, 5, 5: {a.checktriangle(5, 5, 5)}") # Valid Triangle
print(f"Sides of the triangle are 0, 4, 5: {a.checktriangle(0, 4, 5)}") # Invalid Triangle