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

num1 = int(input("first number\n"))
num2 = int(input("second number\n"))

for keys in operations:
    print(keys)

symbol = input("pick an operation from above:\n")

calculation = operations[symbol]      #gets value associated to symbol and assigns to calculation
answer = calculation(num1, num2)      #calling the functions by the values 
print(f"{num1} {symbol} {num2} = {answer}")

contin = input("would you like to continue your calculations with the above answer? 'y' or 'n':\n")

if contin == 'y':
    num1 = answer
    num2 = int(input("second number that you would want to calculate with the above answer\n"))

    for keys in operations:
        print(keys) 
    symbol = input("pick an operation from above:\n")
    calculation = operations[symbol]      #gets value associated to symbol and assigns to calculation
    answer = calculation(num1, num2)      #calling the functions by the values 
    print(f"{num1} {symbol} {num2} = {answer}")

else:
    print("Thank you for using this calc")
