start_mess='Доступные математическую операцию\n1. a + b\n2. a - b\n3. a * b\n4. a/b\n5. a!\n6. Выйти\n'
print(start_mess)
n=input('Выберите операцию: ')

def input_two():
    a=int(input('Введите число a: '))
    b=int(input('Введите число b: '))
    return a,b
def sum():
    print('Вы выбрали операцию сложения a + b')
    a,b=input_two()
    return a+b
def subtrackt():
    print('Вы выбрали операцию вычитания a - b')
    a,b=input_two()
    return a-b
def multipl():
    print('Вы выбрали операцию умножения a * b')
    a,b=input_two()
    return a*b
def devide():
    print('Вы выбрали операцию деления a / b')
    a,b=input_two()
    return a/b
def fact(n):
    
    n=int(n)
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n*fact(n-1)
    

while not int(n)==6:
    
    if n.isdigit():
        n=int(n)
        res=''
        if n==1:
          res=sum()
        elif n==2:
           res=subtrackt()
        elif n==3:
           res=multipl()
        elif n==4:
           res=devide()
        elif n==5:
           print('Вы выбрали операцию расчета факториала')
           a=input('Введите число для расчета факториала: ')
           res=fact(a)
        elif n>6:
            n=input('Вы ввели некорректное значение. Введите число: ')
        print(f'Результат: {res}\n')
        print(start_mess)
        n=input('Выберите операцию: ')
    else:
        n=input('Вы ввели не числовое значение. Повторите ввод: ')
else:
    print('Работа калькулятора завершена')


