import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a valid number. ")

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = get_number("What is the first number?: ")

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        if operation_symbol not in operations:
            print("Invalid opperation. Please choice of the available operators. ")
            continue

        num2 = get_number("What is the second number?: ")
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1:.2f} {operation_symbol} {num2:.2f} = {answer:.2f}")

        while True:
            choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation. ").lower()
            
            if choice == "y":
                num1 = answer
                break
            elif choice == "n":
                should_accumulate = False
                print("\n" * 20)
                calculator()
                return
            else:
                print("Invalid option.")
    
calculator()
