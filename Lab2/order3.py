a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
c=int(input('Введите третье число: '))

(a,b)=(a,b) if a<b else (b,a)
(b,c)=(b,c) if b<c else (c,b)
(a,b)=(a,b) if a<b else (b,a)
print(a,b,c)