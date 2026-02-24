import math

class Answer:
    def distance_in_points(self, x1, y1, x2, y2): 
        return math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1, 2)) #math.sqrt() is used to calculate the square root of the sum of the squares of the differences in x and y coordinates, which gives the distance between the two points in a 2D plane.
    

a = Answer()
print(f"Distance between (1, 2) and (4, 6): {a.distance_in_points(1, 2, 4, 6)}") # Output: 5.0
print(f"Distance between (0, 0) and (3, 4): {a.distance_in_points(0, 0, 3, 4)}") # Output: 5.0
print(f"Distance between Jaipur (26.9124, 75.7873) and Delhi (28.7041, 77.1025): {a.distance_in_points(26.9124, 75.7873, 28.7041, 77.1025)}") # Output: 2.23606797749979