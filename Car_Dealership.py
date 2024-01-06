from abc import ABC, abstractmethod
from Banking_System import Customer
import inspect
inventory = {}
revenue = 0


class Car(ABC):
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def drive(self):
        ...

    @abstractmethod
    def refuel(self):
        ...


class GasolineEngine(Car, ABC):
    def __init__(self, tank_capacity=0):
        self.tank_capacity = tank_capacity

    def drive(self):
        print('Consume fuel to drive.')

    def refuel(self):
        print('Refill the fuel tank with gasoline.')


class ElectricEngine(Car, ABC):
    def __init__(self, battery_capacity=0):
        self.battery_capacity = battery_capacity

    def drive(self):
        print('Consume battery energy to drive.')

    def refuel(self):
        print('Charge the battery with electricity.')


class CarModel(Car):
    global inventory

    def __init__(self, make: str, model: str, engine: ElectricEngine or GasolineEngine, price: int, color: str):
        super().__init__()
        self.price = price
        self.__color = color
        self.__make = make
        self.__model = model
        self.__engine = engine
        self.add_to_inventory(self)

    @staticmethod
    def add_to_inventory(car):
        _key = car.model.lower()
        if _key in inventory:
            inventory[_key] += 1
        else:
            inventory[_key] = 1

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise ValueError
        else:
            self.__price = value

    @property
    def color(self):
        return self.__color

    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def engine(self):
        return self.__engine

    def drive(self):
        self.__engine.drive()

    def refuel(self):
        self.__engine.refuel()

    def __repr__(self):
        return f'{self.__make}{self.__model}'


class Salesperson:
    global inventory
    global revenue

    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @staticmethod
    def search_inventory(model: str):
        if not isinstance(model, str):
            raise TypeError('Car model must be a string')
        if model.lower() in inventory:
            return f'{inventory[model.lower()]} <{model}> cars in inventory.'

    @staticmethod
    def sell(car: CarModel):
        global revenue
        _key = car.model.lower()
        if _key not in inventory:
            print('Sorry! It\'s sold out. Better luck next time.')
            return None
        inventory[_key] -= 1
        if inventory[_key] == 0:
            del inventory[_key]
        revenue += car.price
        return f'Congratulations! You just purchased a {car}!'

    def __repr__(self):
        return f'Hi! I\'m {self.__name}!'


class CarBuyer(Customer):
    global revenue

    def __init__(self, name: str, email: str, phone_num: str, budget: int or float):
        super().__init__(name, email, phone_num)
        self.__budget = budget
        self.__my_cars = []

    @property
    def my_cars(self):
        return self.__my_cars

    @property
    def budget(self):
        return self.__budget

    def buy(self, car: CarModel, stuff: Salesperson):
        if not stuff.search_inventory(car.model) is None:
            if self.__budget >= car.price:
                self.__budget -= car.price
                stuff.sell(car)
                self.__my_cars.append(car.model)
            else:
                print('It\'s out of my budget!')


if __name__ == '__main__':
    print('*********************************************************************************************')
    print('Adding cars to the inventory. ')
    print('____________________________________________________________________________________________')
    car1 = CarModel('Ferrari', '488GTB', engine=ElectricEngine(50), price=8000, color='RED')
    car2 = CarModel('Ferrari', '488GTB', engine=ElectricEngine(50), price=8000, color='BLUE')
    print('Car1: ', car1,'Car2: ', car2)
    print('Inventory:', inventory, 'Revenue: ', revenue)

    print('*********************************************************************************************')
    print('Taking the cars out for a test drive.')
    print('____________________________________________________________________________________________')
    car1.drive()
    car1.refuel()

    print('*********************************************************************************************')
    print('Adding customers.')
    print('____________________________________________________________________________________________')
    customer1 = CarBuyer('Raj Koothrapali', 'raj.kooth@gmail.com', '+37498679823', 10000)
    customer2 = CarBuyer('Howard Wollowitz', 'howie_astrounaut@hotmail.com', '+37456789723', 8000)

    print('*********************************************************************************************')
    print('And here comes Betty. She\'s our salesperson.')
    print('____________________________________________________________________________________________')
    salesperson_Betty = Salesperson('Betty')
    print(salesperson_Betty)

    print('*********************************************************************************************')
    print('Raj buys a car.')
    print('____________________________________________________________________________________________')
    customer1.buy(car1, salesperson_Betty)
    print('Inventory: ', inventory)
    print('Revenue: ', revenue)
    print('Raj\'s cars: ', customer1.my_cars)

    print('*********************************************************************************************')
    print('Howard buys a car.')
    print('____________________________________________________________________________________________')
    customer2.buy(car2, salesperson_Betty)
    print('Inventory: ', inventory)
    print('Revenue: ', revenue)
    print('Howard\'s cars: ', customer2.my_cars)

