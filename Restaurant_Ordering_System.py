from Banking_System import Customer
from abc import ABC, abstractmethod


class Dish:
    def __init__(self, name: str, price: int):
        self.__name = name
        self.__price = price
        self.__ingredients = []

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def ingredients(self):
        return self.__ingredients

    def __repr__(self):
        return f'{self.__name}'


class Appetizer(Dish):
    def __init__(self, name: str, price: int):
        super().__init__(name, price)


class Entree(Dish):
    def __init__(self, name: str, price: int):
        super().__init__(name, price)


class Dessert(Dish):
    def __init__(self, name: str, price: int):
        super().__init__(name, price)


class SideDish(Dish):
    def __init__(self, name: str, price: int):
        super().__init__(name, price)


class Beverage(Dish):  # like duck typing?
    def __init__(self, name: str, price: int):
        super().__init__(name, price)


class Menu:
    def __init__(self, cuisine: str):
        self.__revenue = 0
        self.__cuisine = cuisine
        self.__appetizers = []
        self.__entrees = []
        self.__desserts = []
        self.__side_dishes = []
        self.__beverages = []
        self.__menu = {'Appetizers': self.__appetizers,
                       'Entrees': self.__entrees,
                       'Desserts': self.__desserts,
                       'SideDishes': self.__side_dishes,
                       'Beverages': self.__beverages}

    @property
    def revenue(self):
        return self.__revenue

    @revenue.setter
    def revenue(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__revenue = value
        else:
            raise ValueError('Revenue must be of type int or float.')

    @property
    def menu(self):
        return self.__menu

    @property
    def appetizer(self):
        return self.__appetizers

    @property
    def entrees(self):
        return self.__entrees

    @property
    def desserts(self):
        return self.__desserts

    @property
    def side_dishes(self):
        return self.__side_dishes

    @property
    def beverages(self):
        return self.__beverages

    def add_appetizer(self, dish: Appetizer):
        self.__appetizers.append(dish.name)

    def add_entree(self, dish: Entree):
        self.__entrees.append(dish.name)

    def add_dessert(self, dish: Dessert):
        self.__desserts.append(dish.name)

    def add_side_dish(self, dish: SideDish):
        self.__side_dishes.append(dish.name)

    def add_beverage(self, beverage: Beverage):
        self.__beverages.append(beverage.name)

    def __repr__(self):
        return f'{self.__menu}'


class RestaurantCustomer(Customer):
    def __init__(self, name, email, phone_num, budget: int or float):
        super().__init__(name, email, phone_num)
        self.__order_history = []
        self.budget = budget

    @property
    def order_history(self):
        return self.__order_history

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__budget = value
        else:
            raise ValueError('Budget must be of type int or float.')

    def order(self, some_menu: Menu, dish: Dish):
        found = False
        for item in some_menu.menu:
            if dish.name in some_menu.menu[item]:
                found = True
                if self.budget <= dish.price:
                    print(f'I can\'t afford {dish}.')
                else:
                    print(f'I bought {dish}.')
                    self.budget -= dish.price
                    some_menu.revenue += dish.price
                    self.order_history.append(dish)
        if not found:
            print('Sorry we\'re out of that dish.')

    @staticmethod
    def view_menu(menu):
        print(menu)


if __name__ == '__main__':
    print('Creating a menu.')
    print('______________________________________________________________________')
    chinese_menu = Menu('Chinese')

    print('Creating dishes and adding them to the menu.')
    print('______________________________________________________________________')
    spring_roll = Appetizer('Spring Rolls', 3000)
    dim_sum = Appetizer('Dim Sums', 5000)
    cucumber_salad = Appetizer('Cucumber Salad', 1500)

    chinese_menu.add_appetizer(spring_roll)
    chinese_menu.add_appetizer(dim_sum)
    chinese_menu.add_appetizer(cucumber_salad)

    chicken = Entree('Kung Pao Chicken', 4000)
    chaomian = Entree('Chao Mian', 2000)
    pork = Entree('Sweet and Sour Pork', 4000)
    duck = Entree('Peking Duck', 8000)
    hotpot = Entree('Hot Pot', 20000)

    chinese_menu.add_entree(chicken)
    chinese_menu.add_entree(chaomian)
    chinese_menu.add_entree(pork)
    chinese_menu.add_entree(duck)
    chinese_menu.add_entree(hotpot)

    sesame_ball = Dessert('Sesame balls', 1500)
    cheesecake = Dessert('Cheesecake', 2000)

    chinese_menu.add_dessert(sesame_ball)
    chinese_menu.add_dessert(cheesecake)

    jasmine_tea = Beverage('Jasine Tea', 1000)
    beer = Beverage('Tsingdao beer', 800)

    chinese_menu.add_beverage(jasmine_tea)
    chinese_menu.add_beverage(beer)

    dumplings = SideDish('Pork Dumplings', 6000)
    rice = SideDish('Steamed Rice', 1000)

    chinese_menu.add_side_dish(dumplings)
    chinese_menu.add_side_dish(rice)

    print(chinese_menu)

    print('______________________________________________________________________')
    print('Creating a customer.')
    print('______________________________________________________________________')
    customer = RestaurantCustomer('Penny', 'penny.hoffstader@hotmail.com', '+37455867586', 10000)

    print('______________________________________________________________________')
    print('The customer views the menu. ')
    print('______________________________________________________________________')
    customer.view_menu(chinese_menu)
    print('______________________________________________________________________')
    print('The customer orders food. ')
    print('Budget: ', customer.budget)
    print('______________________________________________________________________')
    customer.order(chinese_menu, beer)
    customer.order(chinese_menu, dumplings)
    customer.order(chinese_menu, pork)
    customer.order(chinese_menu, rice)
    customer.order(chinese_menu, cheesecake)
    print('______________________________________________________________________')
    print('Budget: ', customer.budget)
    print('Customer order history: ', customer.order_history)
    print('Restaurant revenue: ', chinese_menu.revenue)



