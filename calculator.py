def add (x, y):
    return x + y

def subtract (x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    return x/y

def square (x):
    return x**2

def percent (x, y): 
    return x/100*y
 
print ("Would you like to...")
print ("1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Square \nor \n6. Take percent?") 

operation = input("Please select one (1-6): ")

if operation == "1" or operation == "2" or operation == "3" or operation == "4":
    value1 = input ("Please input your first value: ")
    value2 = input ("Please input your second value: ")
    value1 = float(value1)
    value2 = float(value2)

    if operation == "1":
        print(value1, " + ", value2, " = ", add(value1, value2))
    
    elif operation == "2":
        print(value1, " - ", value2, " = ", subtract(value1, value2))

    elif operation == "3":
        print(value1, " * ", value2, " = ", multiply(value1, value2))

    elif operation == "4":
        print(value1, "/", value2, " = ", divide(value1, value2))


elif operation == "5": 
    value1 = input ("Please input the number you would like to square: ")
    value1 = float(value1)
    print(value1, "^ 2 = ", square(value1))

elif operation == "6": 
    print ("Please input the percent you would like to take followed by the number you would like to take the percent of.")
    print("(example: I want 15%" " of 75. First number: 15. Second number: 75)")
    value1 = input ("Please input your first value: ")
    value2 = input ("Please input your second value: ")
    value1 = float(value1)
    value2 = float(value2)
    print (value1, "%" " of ", value2, " = ", percent(value1, value2), "%")

else : 
    print ("invalid")