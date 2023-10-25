a=int((input('Введите a: ')))
b=int((input('Введите b: ')))
c=int((input('Введите c: ')))

diskr=b**2-4*a*c
if diskr>0:
    rez1=(-b-diskr**0.5)/(2*a)
    rez2=(-b+diskr**0.5)/(2*a)
    print(rez1,rez2)
elif diskr==0:
    rez=-b/(2*a)
    print(rez)
