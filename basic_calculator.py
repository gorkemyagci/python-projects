# Basic Calculator
# define the functions needed: add, subtract, multiply, divide

def add(a,b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))
    
def sub(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))
    
def mul(a,b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))
    
def div(a,b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

while True:
    print('A. Additon')
    print('B. Subtraction')
    print('C. Multiplication')
    print('D. Division')
    print('E. Exit')

    choice = input('Enter your choice: ')
    if choice == 'A' or choice == 'a':    
        print('Addition')
        a = float(input('Enter the first number: '))
        b = float(input('Enter the second number: '))
        add(a,b)
    elif choice == 'B' or choice == 'b':    
        print('Subtraction')
        a = float(input('Enter the first number: '))
        b = float(input('Enter the second number: '))
        sub(a,b)
    elif choice == 'C' or choice == 'c':
        print('Multiplication')
        a = float(input('Enter the first number: '))
        b = float(input('Enter the second number: '))
        mul(a,b)
    elif choice == 'D' or choice == 'd':
        print('Division')
        a = float(input('Enter the first number: '))
        b = float(input('Enter the second number: '))
        div(a,b)
    elif choice == 'E' or choice == 'e':
        quit()
    else:
        print('Invalid choice')
    