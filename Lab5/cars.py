class Engine:
    def __init__(self, power: int, producer: str):
        self.power=power
        self.producer=producer
    def __str__(self):
        return f'Мотор: {self.power} л.с., {self.producer}'

class Person:
    def __init__(self, age:int, fullName:str):
        self.__age=age
        self.fullName=fullName
class Driver (Person):
    def __init__(self, fullName: str, age: int,  experience: int):
        super().__init__(fullName=fullName, age=age)
        self.experience=experience
    def __str__(self):
        return f'Водитель: {self.fullName}, Стаж вождения: {self.experience}'

class Car:
    def __init__(self, model: str, weight: int, carClass: str, driver: Driver, engine: Engine):
        self.model=model
        self.weight=weight
        self.carClass=carClass
        self.driver=driver
        self.engine=engine

    def start(self):
        res=f'{self.model} начинает движение'
        print(res)
    def stop(self):
        res=f'{self.model} останавливается'
        print(res)
    def turn_right(self):
        res=f'{self.model} поворачивает направо'
        print(res)
    def turn_left(self):
        res=f'{self.model} поворачивает налево'
        print(res)
    
    def __repr__(self):
        return f'Марка: {self.model}, Класс: {self.carClass}, Вес: {self.weight}, {self.driver}, {self.engine}'

class Lorry(Car):
    def __init__(self,model: str, weight: int, carClass: str, driver:Driver, engine: Engine,carrying:int):
        super().__init__(model, weight, carClass, driver, engine)
        self.carrying=carrying
    def __repr__(self):
        return f'{super().__repr__()}, Грузоподъемность: {self.carrying} кг'
    
class SportCar(Car):
    def __init__(self, model: str, weight: int, carClass: str, driver: Driver, engine: Engine, speed: int):
        super().__init__(model, weight, carClass, driver, engine)
        self.speed=speed
    def __repr__(self):
        return f'{super().__repr__()}, Предельная скорость: {self.speed} км/ч'

driver=Driver('Иванов Иван', 33, 5)
engine=Engine(200, 'Toyota')
car=Car('Toyota Camry', 1500, 'Седан', driver, engine)
driver=Driver('Петр Петров',45,10)
engine=Engine(300, 'Volvo')
lorry=Lorry('Volvo FH', 8000, 'Грузовк', driver, engine, 5000)
driver=Driver('Михаэль Шумахер', 50, 15)
engine=Engine(400, 'Ferrari')
sportCar=SportCar('Ferrari 488', 1500, 'Спорткар', driver, engine, 300)

print(car)
print(lorry)
print(sportCar)

car.start()
lorry.stop()
sportCar.turn_left()