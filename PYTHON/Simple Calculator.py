def add(num1, num2):
    return num1+ num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1* num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero"
print ("choice 1: addition \nchoice 2:subtraction\nchoice 3: multiplication\nchoice 4:division")
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    choice = int(input("enter choice:"))
    if choice == 1:
           operator="+"
           result= add(num1,num2)
    elif choice == 2:
           operator="-"
           result= subtract(num1,num2)
    elif choice == 3:
           operator="*"
           result=multiply(num1,num2)
    elif choice == 4:
           operator="/"
           result=divide(num1,num2)
    else:
           print ("Invalid Input from the User")
    print("Performing Calculation....","(",operator,")",":")
    print(num1,operator,num2,"=",result)
    if input("Do you want to continue the program(yes/no):")=="no":
           break

       
