def basic_calculator():
    def addition(x, y):
        return x + y 
    def subtraction(x, y):
        return x - y
    def multiplication(x, y):
        return x * y
    def division(x, y):
        if y != 0:
            return x / y
        
    arthimetic = int(input(f'What operation are we doing: \n1.Addition 2.Subtraction 3.Multiplication 4.Division\n'))
    
    num1 = float(input('\nEnter first number:    '))
    num2 = float(input('\nEnter second number:   '))

    if arthimetic == 1:
        print(f'{num1} + {num2} = {addition(num1, num2)}') 
    elif arthimetic == 2:
        print(f'{num1} - {num2} = {subtraction(num1, num2)}') 
    elif arthimetic == 3:
        print(f'{num1} x {num2} = {multiplication(num1, num2)}') 
    elif arthimetic == 4:
        print(f'{num1} / {num2} = {division(num1, num2)}') 
    else:
        print(f'Enter a valid option')

basic_calculator()        
