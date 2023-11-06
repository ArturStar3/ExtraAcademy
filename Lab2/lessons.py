# lessons=int(input("Введите количество уроков "))
# duration=bool(lessons)*(45*lessons+5*(lessons//2)+15*(lessons//2+lessons%2-1))
# print(9+(duration//60),duration % 60)
nums=[2,4,6,8]
for i in range(len(nums)):
    print(i)
    for j in range(i+1,len(nums)):
        print('__'+str(j))
