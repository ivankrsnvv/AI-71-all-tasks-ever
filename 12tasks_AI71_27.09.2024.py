#  число кратно 3-ем
try:
    nu1 = int(input())
    if nu1 % 3 == 0:
        print('true')
    else:
        print('False')
except:
     print('u invalid')

#  калькулятор
try:
    print('this is calculator')
    nu1 = int(input('enter first number'))
    nu2 = int(input('enter second number'))
    action = input('enter action (+,-,*,/,//,%,**)')
    if action == '+':
        print(nu1 + nu2)
    elif action == '-':
        print(nu1 - nu2)
    elif action == '*':
        print(nu1 * nu2)
    elif action == '/':
        print(nu1 / nu2)
    elif action == '//':
        print(nu1 // nu2)
    elif action == '%':
        print(nu1 % nu2)
    elif action == '**':
        print(nu1 ** nu2)
    elif action == '/' and nu2 == 0:
        print('error')
except:
    print('error')

#  задача1
try:
    nu1 = int(input('enter number'))
    if nu1 < 0:
        print('число отрицательно')
    else:
        print('число положительнео')
except:
    print('error')

# задача 2
try:
    nu1 = int(input('enter number'))
    if nu1 % 2 == 0:
        print('even')
    else:
        print('odd')
except:
    print('error')

# задача 3
try:
    nu1 = int(input('enter number'))
    if nu1 >= 10 and nu1 <= 20:
        print('true')
    else:
        print('false')
except:
    print('error')

# задача4
try:
    nu1 = int(input('enter first num'))
    nu2 = int(input('enter second num'))
    if nu1 >= 10 and nu2 >= 10:
        print('true')
    else:
        print('false')
except:
    print('error')

#задача 5
try:
    nu1 = int(input('enter number'))
    if nu1 >= 1:
        print('positive number')
    if nu1 == 0:
        print('number = zero')
    if nu1 <= -1:
        print('negative number')
except:
    print('error')

# задача 6
try:
    nu1 = int(input())
    nu2 = int(input())
    nu3 = int(input())
    if nu1 > 0 or nu2 > 0 or nu3 > 0:
        print('есть положительное число')
    else:
        print('false')
except:
    print('ERROR')

# задача 7
try:
    nu1 = int(input())
    if nu1 <= 10:
        print('меньше 10')
    elif nu1 >= 10 and nu1 <= 20:
        print('между 10 и 20')
    elif nu1 >= 20:
        print('больше 20')
except:
    print('error')

#  задача 8
password = 'q1w2e3'
passw = input('Введите пароль высланый вам на почту')
if passw == password:
    print('пароль принят')
else:
    print('пароль неверный')

# задача 9
try:
    year = int(input())
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('YES')
    else:
        print('NO')
except:
    print('error')

# задача 10 (я чут чут импровизировал и сделал не 3 а 4 числа случайно аххахахаха)
try:
    in1 = int(input())
    in2 = int(input())
    in3 = int(input())
    in4 = int(input())

    if in1 < in2:
        if in1 < in3:
            if in1 < in4:
                print(in1)
            else:
                print(in4)
        else:
            if in3 > in4:
                print(in4)
            else:
                print(in3)
    else:
        if in2 < in3:
            if in2 < in4:
                print(in2)
            else:
                print(in4)
        else:
            if in3 > in4:
                print(in4)
            else:
                print(in3)
except:
    print('error')