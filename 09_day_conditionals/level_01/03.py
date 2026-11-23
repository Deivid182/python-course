# Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is smaller than b")
else:
    print("a is equal to b")
