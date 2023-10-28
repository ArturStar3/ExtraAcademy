lessons=int(input("Введите количество уроков "))
duration=bool(lessons)*(45*lessons+5*(lessons//2)+15*(lessons//2+lessons%2-1))
print(9+(duration//60),duration % 60)