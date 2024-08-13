"""Calculator Project"""
def add(n1, n2):
    return n1 + n2
# Add other functions
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def modulo(n1, n2):
    return n1 % n2
"""
We can declare a variable and assign a function
addition = add
"""
# Add the functions into a dict
math_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo
}

def calculator():
    should_continue = True
    first_number = float(input("Enter the first number: \n"))

    while should_continue:
        for operation in math_operations:
            print(operation)
        operator = input("Choose the operation: \n")
        second_number = float(input("Enter the second number: \n"))
        result = math_operations[operator](first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {result}")
        # Ask user if to continue
        game_on = input(f"Another calculation with the {result}? Type y or n: \n").lower()
        if game_on == "y":
            first_number = result
        else:
            should_continue = False
            print("\n" * 20)
            calculator()
            
calculator()
