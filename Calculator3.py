"""
        SIMPLE CALCULATOR
        Perform simple function like Addition, Substraction, Multiplication, Division

"""

def add(num1, num2):
    
    sum = num1+num2
    print(sum)

def mul(num1, num2):
    mul = num1*num2
    print(mul)
    
def sub(num1, num2):
    sub = num1-num2
    print(sub)
    
def div(num1, num2):
    
    div = num1/num2
    print(div) 
        
while(True):
    print("Press 1 for addition")
    print("Press 2 for substraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")
    print("type exit to close the application")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        num1 = int(input("Enter the first number: "))       
        num2 = int(input("Enter the second number: "))
        
        add(num1, num2)
    elif choice == '2':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        sub(num1, num2)    
    
    elif choice == '3':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        mul(num1,num2)
        
    elif choice == '4':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        div(num1, num2)        
        
    elif choice == "exit":
        print("Thank you for using our application")
        break    
    else:
        print("You entered the Invalid choice, Please try again with valid choice.")
        
        