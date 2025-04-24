#Functions definations: These lines defines 4 seperate functions, each one responsible for a specific arithmetic operations 
def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

# Main function: This is the main function that will be executed when the script is run. It will prompt the user for input and perform the selected operation.
def calculator():
    print("Select operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        choice = input("Enter choice 1/2/3/4:")
         