tasks={
    1: 'Создать пользователя',
    2: 'Показать список пользователей',
    3: 'Удалить пользователя из списка',
    4: 'Авторизация',
    5: 'Выход'
}
userlist=[]
def start_message():
    mess='Выберите действие: '

    for key, value in tasks.items():
        mess=mess+f'\n{key}. {value}'

    print(mess)
    task=input('Введите требуемое действие: ')
    while not task.isdigit():
        task=input('Неверные данные. Введите число: ')
    while not int(task) in tasks.keys():
        task=input('Введите число в диапазоне от 1 до 6: ')
    return int(task)

def is_uniq_mail(email):
    for user in userlist:
        if user['email']==email:
            return False
    return True

def create_user():
    name=input('Введите имя пользователя: ')
    while not name.isalpha():
        name=input('Введите корректное имя пользователя: ')
    surname=input('Введите фамилию пользователя: ')
    while not surname.isalpha():
        surname=input('Введите корректную фамилию пользователя: ')
    age=input('Введите возраст пользователя: ')
    while not age.isdigit():
        age=input('Введите корректное значение возраста: ')
    address=input('Введите адресс проживания: ')
    email=input('Введите email адрес: ')
    while not is_uniq_mail(email):
        email=input('Такой адрес уже существует. Введите другую почту: ')
    password=input('Введите пароль: ')
    while len(password)<6:
        password=input('Введите пароль. Минимальная длина пароля - 6 символов: ')
    user={
        'name':name,
        'surname':surname,
        'age':age,
        'address':address,
        'email':email,
        'password':password
    }
    userlist.append(user)
    print()

def show_user_list():
    if len(userlist)==0:
        print('Пользователи еще не созданы')
        return
    for user in userlist:
        print(f"Имя {user['name']}, Фамилия {user['surname']}, Возраст {user['age']}, Адрес {user['address']}, Почта {user['email']}")
    print()

def delete_user():
    if len(userlist)==0:
        print('Нет пользователей для удаления')
        return
    
    for user in userlist:
        print(f"{userlist.index(user)}: {user['name']} {user['surname']} {user['email']}")
    user=input('Введите индекс пользователя которого хотите удалить: ')
    while not user.isdigit():
        user=input('Ч И С Л О В О Е значение: ')
    while int(user)>len(userlist):
        user=input('Такого пользователя не сществует. Попробуйте еще разок: ')
    userlist.pop(int(user))

def get_user(email):
    for user in userlist:
        if user['email']==email:
            return user
    return False

def autarization():
    email=input('Введите email: ')
    user=get_user(email)
    if user:
        password=input('Введите пароль: ')
        while not password==user['password']:
            password=input('Неверный пароль. повторите ввод: ')
        print(f"Добро пожаловать {user['name']}")
    else:
        print('Данные пользователь не зарегистрирован')


while (sm:=start_message())!=5:
    print(sm)
    print(f'\nВы выбрали \'{tasks[int(sm)]}\'\n')
    if sm==1:
        create_user()
    if sm==2:
        show_user_list()
    if sm==3:
        delete_user()
    if sm==4:
        autarization()
print('До свидания')
