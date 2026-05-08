try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a / b)
    
except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")