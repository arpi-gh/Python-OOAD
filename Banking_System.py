from abc import ABC, abstractmethod
from Validator_descriptors import Email, PhoneNumber, AccountNumber
import time

accounts = {}
transactions = {}


class Customer:
    email = Email('email')
    phone_num = PhoneNumber('phone_num')

    def __init__(self, name: str, email: str, phone_num: str) -> None:
        self.__name = name
        self.email = email
        self.phone_num = phone_num

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def contact(self):
        return f'phone: {self.phone_num}\nemail: {self.email}'

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return self.name


class Account(ABC):
    global transactions
    acc_num = AccountNumber('acc_num')

    def __init__(self, acc_num: str, balance=0, currency='USD') -> None:
        self.acc_num = acc_num
        self.balance = balance
        self.__currency = currency

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__balance = value

    def transfer(self, receiver, amount: int or float):
        if not isinstance(receiver, Account):
            raise TypeError('Please provide a valid account.')
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise ValueError('Please enter a valid amount.')
        else:
            self.balance -= amount
            receiver.balance += amount
            t = str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec)
            receipt = f'Sender: {self}\nReceiver:{receiver}\nAmount:{amount}\nexecuted:{t}'
            key = 'N' + str(len(transactions)+1)
            transactions[key] = f'{self.acc_num}->{receiver.acc_num}({amount}{self.__currency}) at {t}'
        print('\n___________________________________\n', receipt, '\n___________________________________\n')

    def deposit(self, amount: int or float) -> None:
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise ValueError('Enter a numeric value.')
        else:
            self.balance += amount
            t = str(time.localtime().tm_hour) + ':'+ str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec)
            receipt = f'Deposited amount:{amount}\nAccount:{self.acc_num}\nBalance:{self.balance}\nexecuted:{t}'
            key = 'N' + str(len(transactions)+1)
            transactions[key] = f'-> {self.acc_num}({amount}) at {t}'
            print('\n___________________________________\n', receipt, '\n___________________________________\n')

    def withdraw(self, amount: int or float) -> None:
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise ValueError('Enter a numeric value.')
        else:
            self.__balance -= amount
            t = str(time.localtime().tm_hour) + ':'+ str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec)
            receipt = f'Withdrawn amount:{amount}\nAccount:{self.acc_num}\nBalance:{self.balance}\nexecuted:{t}'
            key = 'N' + str(len(transactions)+1)
            transactions[key] = f'{self.acc_num}({amount})-> at {t}'
            print('\n___________________________________\n', receipt, '\n___________________________________\n')

    @abstractmethod
    def __repr__(self):
        ...


class IndividualAccount(Account, ABC):
    global accounts

    @staticmethod
    def __update_accounts(key, value):
        if key not in accounts:
            accounts[key] = value
        else:
            return f'Account already exists.'

    def __init__(self, acc_num: str, customer: Customer, balance=0):
        super().__init__(acc_num, balance)
        self.customer = customer
        self.__update_accounts(self.customer.name, self.acc_num)

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer_obj):
        if not isinstance(customer_obj, Customer):
            raise TypeError('Please create a customer using the "Customer()" constructor.')
        else:
            self.__customer = customer_obj

    def __repr__(self):
        return f'{self.customer.name}: {self.acc_num}'


class JointAccount(Account):
    global accounts

    @staticmethod
    def __update_accounts(key, value):
        if key not in accounts:
            accounts[key] = value
        else:
            return f'Account already exists.'

    def __init__(self, acc_num: str, customers: list[Customer], balance=0):
        super().__init__(acc_num, balance)
        self.customers = customers
        self.__update_accounts(tuple(obj.name for obj in customers), self.acc_num)

    @property
    def customers(self):
        return self.__customers

    @customers.setter
    def customers(self, customer_list: list[Customer]):
        if not all(isinstance(customer, Customer) for customer in customer_list):
            raise TypeError('Please create customers using the "Customer()" constructor.')
        else:
            self.__customers = customer_list

    def __repr__(self):
        return f'{self.customers}: {self.acc_num}'


class CheckingAccount(IndividualAccount):
    global accounts

    @staticmethod
    def __update_accounts(key, value):
        if key not in accounts:
            accounts[key] = value
        else:
            return f'Account already exists.'

    def __init__(self, acc_num: str, customer: Customer, balance=0):
        super().__init__(acc_num, customer, balance)


class SavingsAccount(IndividualAccount):
    global accounts

    @staticmethod
    def __update_accounts(key, value):
        if key not in accounts:
            accounts[key] = value
        else:
            return f'Account already exists.'

    def __init__(self, acc_num: str, customer: Customer, balance=0):
        super().__init__(acc_num, customer, balance)

    def withdraw(self, amount: int or float):
        return 'Can\'t make a withdrawal from a savings account'


if __name__ == '__main__':

    # Creating the customers

    Bernadette = Customer('Bernadette Rostenkowski', 'bernie.rostenkowski@gmail.com', '+37444838673')
    Sheldon = Customer('Sheldon Cooper', 'sheldon.cooper@gmail.com', '+37444558920')
    Amy = Customer('Amy Farrah Fowler', 'amy_fowler@gmail.com', '+37444567120')
    Leonard = Customer('Leonard Hofstadter', 'leonardandpenny@gmail.com', '+37444678723')

    # Creating the accounts

    chk_acc_B = CheckingAccount('1234567812345678', Bernadette)
    sav_acc_S = SavingsAccount('5678123456781234', Sheldon)
    joint_acc_SA = JointAccount('1726374615243948', [Sheldon, Amy])

    # Displaying the results

    print('_____________________________________________________________________')
    print('Here are the customers')
    print('_____________________________________________________________________')
    print(f'Bernadette: {Bernadette}')
    print(f'Sheldon: {Sheldon}')
    print(f'Amy: {Amy}')
    print(f'Leonard: {Leonard}')
    print('_____________________________________________________________________')
    print('Here are the accounts')
    print('_____________________________________________________________________')
    print(f'Bernadette: {chk_acc_B}')
    print(f'Sheldon: {sav_acc_S}')
    print('Sheldon and Amy: ', joint_acc_SA)
    print('_____________________________________________________________________')
    print('Here is the contact information')
    print('_____________________________________________________________________')
    print(f'{Bernadette.name}\n{Bernadette.contact}')
    print(f'{Sheldon.name}\n{Sheldon.contact}')
    print(f'{Amy.name}\n{Amy.contact}')
    print(f'{Leonard.name}\n{Leonard.contact}')
    print('_____________________________________________________________________')

    # Checking the behavior
    print('_____________________________________________________________________')
    print('Here are some transactions.')
    print('_____________________________________________________________________')
    sav_acc_S.deposit(5000)
    print('Balance:', sav_acc_S.balance)
    sav_acc_S.transfer(chk_acc_B, 2000)
    print('Balance:', chk_acc_B.balance)
    sav_acc_S.withdraw(200)
    print('Balance:', sav_acc_S.balance)
    chk_acc_B.withdraw(500)
    print('Balance:', chk_acc_B.balance)
    print('_____________________________________________________________________')
    print('Info about created accounts and transaction history')
    print('_____________________________________________________________________')
    print(accounts)
    print(transactions)





