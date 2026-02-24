def divisible(number):
    if number % 4 == 0:
        return "YES"
    else:
        return "NO"
    

number = int(input("Enter a number: "))
result = divisible(number)
print(result)