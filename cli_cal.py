def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y == 0:
        return "cannot divide by zero!"
    return x/y

print ("Select operation")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLIACTION")
print("4. DIVISION")

choice=input("enter choice (1/2/3/4)")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:",mul(num1, num2))
elif choice == '4':
    print("Result:", div(num1, num2))
else:
    print("Invalid input")