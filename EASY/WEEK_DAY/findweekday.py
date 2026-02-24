class Answer:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def get_weekday(self) -> str:
        # Zeller's Congruence algorithm to calculate the day of the week
        if self.month < 3:
            self.month += 12
            self.year -= 1
        
        K = self.year % 100
        J = self.year // 100
        
        f = self.day + (13 * (self.month + 1)) // 5 + K + (K // 4) + (J // 4) - (2 * J)
        weekday = f % 7
        
        days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days_of_week[weekday]
    
# Example usage:
if __name__ == "__main__":
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))
    
    answer = Answer(day, month, year)
    print(f"The day of the week is: {answer.get_weekday()}")