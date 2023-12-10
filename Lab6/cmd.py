import os
import time

class PythonShell:
    def __init__(self):
        self.path = os.getcwd()

    def timer(func):
        def wrap(*args):
            timestart = time.perf_counter()
            f = func(*args)
            print(f'Время выполнения функции "{f}": {(time.perf_counter() - timestart) * 1000}мс')
        return wrap
    
    @timer
    def ls(self, *args):
        print(os.listdir(self.path))
        return ('Список файлов и папок')
    
    @timer
    def cd(self, targetDirectory: str, *args):
        if os.path.exists(targetDirectory):
            os.chdir(targetDirectory)
            self.path=os.getcwd()
            print(self.path)
            return 'Переход в директорию'
        else:
            raise OSError('Данная директория не существует')

    @timer
    def mkdir(self, targetPath):
            os.mkdir(targetPath)
            print(f"Папка {targetPath} создана")
            return 'Создание папки'
    
    @timer
    def touch(self, targetFilePath):
        file=open(targetFilePath, 'x')
        print(f'Файл {targetFilePath} создан')
        file.close()
        return 'Создание файла'
    
    @timer
    def remove(self, targetFilePath):
        os.remove(targetFilePath)
        print(f'Файл {targetFilePath} удален')
        return 'Удаление файла'

    @timer
    def rmdir(self, targetPath):
        if os.listdir(targetPath):
            req = input('Папка не пуста, хотите ли вы все равно удалить папку и все вложенные элементы? (y/n): ').upper()
            if req == 'Y':
                for el in os.walk(targetPath, topdown=False):
                    print(el)
                    if el[2]:
                        print(el[2])
                        for file in el[2]:
                            os.remove(el[0] + '\\' + file)
                    if el[1]:
                        print(el[1])
                        for dir in el[1]:
                            os.rmdir(el[0] + '\\' + dir)
                    if el[0]==targetPath:
                        os.rmdir(targetPath)
        else:
            os.rmdir(targetPath)
        return 'Удаление папки'
    
    @timer
    def fileopen(self,targetFile):
        with open(targetFile,'r') as f:
            print(f.read())
        return 'Чтение файла'



cmd=PythonShell()
commands={'ls':cmd.ls, 'cd':cmd.cd, 'mkdir':cmd.mkdir, 'touch':cmd.touch, 'remove':cmd.remove, 'rmdir':cmd.rmdir, 'fileopen':cmd.fileopen, 'exit':None}
print(f'Приветствую Вас в симуляторе командной строки PythonShell.\nСписок доступных команд: {(", ").join(commands.keys())}')
command=input().split(' ')
while not command[0].upper() == 'EXIT':
    argument=(' ').join(command[1:])
    try:
        if command[0] in commands.keys():
            commands[command[0]](argument)
        else:
            raise OSError('Данная команда не поддерживается')
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    command=input().split(' ')
print('Вы завершили работу с симулятором коммандной строки')

