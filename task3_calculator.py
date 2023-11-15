def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y


all_operations = {'+':add, '-':sub, '*': mul, '/':div}

while True:
    op = input("Select an operation: + - / * or print exit: ")
    if op == 'exit':
        break
    if op not in ('+', '-', '*', '/'):
        print("Failed: Didn't recognize an operation")
        continue
    number1 = input("input numbers 1: ")
    number2 = input("input numbers 2: ")
    try:
        number1 = float(number1)
        number2 = float(number2)
    except ValueError:
        print('Failed: Invalid input')
        continue
    if op == '/' and number2==0:
        print("Failed: Divizion by zero")
        continue

    print(f"Result: {all_operations[op](number1, number2)}")
