def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return n1 / n2
def multiply(n1, n2):
    return n1 * n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print("welcome to pycalculator!\n")
    num1 = float(input("first number\n"))
    for keys in operations:
        print(keys)
    should_continue = True

    while should_continue:
        symbol = input("pick operation:\n")
        num2 = float(input("next number\n"))
        calculation = operations[symbol]      #gets value associated to symbol and assigns to calculation
        answer = calculation(num1, num2)      #calling the functions by the values 
        print(f"{num1} {symbol} {num2} = {answer}")

        if input(f"type 'y' to continue calculations with {answer} or 'n' to start a new calculation:\n") == 'y':
            num1 = answer
        else: 
            should_continue = False
            calculator()

calculator()