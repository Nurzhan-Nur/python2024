# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def cal(t, x, y):
        if t  == '+':
            return x + y
        if t == '-':
            return x - y
        if t == '*':
            return x * y
        if t == '/':
            if y == 0:
                return "You can't divide by zero"
            return x / y

def calculathor():
    print("Welcome to the calculator!")
    print("What would you like to do?")
    print(
          "1. For addition, type '+' " + '\n'
          "2. For subtraction, type '-' " + '\n'
          "3. For multiplication, type '*' " + '\n'
          "4. For division, type '/' "
    )
    loo ="yes"
    while(loo == "yes"):
        iput = (input("type here: "))
        l = ['+', '-', '*', '/']
        if iput not in l:
            print("Invalid input entered")
        else:
            x = int(input("Enter a number: "))
            y = int(input("Enter a second  number: "))
            print("The result is: " + str(cal(iput, x, y)))
        loo = input("Do you want to continue? Type 'yes' if  you  want to continue or anything else if you dont: ").lower()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculathor()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
