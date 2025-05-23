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

        if choice in ["1","2","3","4"]:
            try:
                num1 = float(input("Enter first number:"))
                num2 = float(input("Enter second number:"))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
                
            if choice == "1":
                print(num1,"+",num2,"=",add(num1,num2) )
            elif choice == "2":
                print(num1,"-", num2, "=", subtract(num1,num2))
            elif choice == "3":
                print(num1,"*", num2, "=", multiply(num1,num2))
            elif choice == "4":
                print(num1, "/", num2, '=', divide(num1,num2))

            next_calculation = input("Do you want to perform another calculation? (yes/no):")
            if next_calculation.lower() != "yes":
                break
        else:
            print("Invalid input. Please enter valid choice between 1 and 4")
if __name__ == "__main__":
    calculator()


'''
The program displays a menu of operations.
The user selects an operation (1, 2, 3, or 4).
The program prompts the user to input two numbers.
The selected operation is performed, and the result is displayed.
The user is asked if they want to perform another calculation. If "yes," the program restarts; otherwise, it exits.
'''