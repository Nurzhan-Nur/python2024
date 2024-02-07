import logging


def cal(t, x, y):
    match t:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            if y != 0:
                return x / y
            else:
                return "You can't divide by zero"


def calculathor():
    print("Welcome to the calculator!")
    print("What would you like to do?")
    print(
        "1. For addition, type '+' " + '\n'
                                       "2. For subtraction, type '-' " + '\n'
                                                                         "3. For multiplication, type '*' " + '\n'
                                                                                                              "4. For division, type '/' "
    )
    loo = "yes"
    while loo == "yes":
        iput = (input("type here: "))
        l = ['+', '-', '*', '/']
        if iput not in l:
            logging.warning("Invalid input entered")
        else:
            x = int(input("Enter a number: "))
            y = int(input("Enter a second  number: "))
            print("The result is: " + str(cal(iput, x, y)))
            loo = input(
                "Do you want to continue? Type 'yes' if  you  want to continue or anything else if you dont: ").lower()


calculathor()
