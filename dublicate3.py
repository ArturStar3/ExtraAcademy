a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
c=int(input('Введите третье число: '))
i=0
if a==b or b==c or a==c:
    i=2
if a==b==c:
    i=3
print(i)