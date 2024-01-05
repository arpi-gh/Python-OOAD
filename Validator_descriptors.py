import re

class Email:
    def __init__(self, name: str):
        self.name = name
        self.pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self.regex = re.compile(self.pattern)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        else:
            raise KeyError(f"The email address for {self.name} was not added.")

    def __set__(self, instance, value):
        if not self.regex.match(value):
            print("Invalid email format detected!")
        else:
            instance.__dict__[self.name] = value
            print('Email address successfully added.')


class PhoneNumber:
    def __init__(self, name: str):
        self.name = name
        self.pattern = r'^\+374[0-9]{8}$'
        self.regex = re.compile(self.pattern)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        else:
            raise KeyError(f"The phone number for {self.name} was not added.")

    def __set__(self, instance, value):
        if not self.regex.match(value):
            print("Invalid phone number detected!")
        else:
            instance.__dict__[self.name] = value
            print('Phone number successfully added.')

class AccountNumber:
    def __init__(self, name: str):
        self.name = name
        self.pattern = r'^\d{16}$'
        self.regex = re.compile(self.pattern)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        else:
            raise KeyError(f"The account number for {self.name} was not added.")

    def __set__(self, instance, value):
        if not self.regex.match(value):
            print("Invalid account number detected!")
        else:
            instance.__dict__[self.name] = value
            print('Account number successfully added.')


class Customer:
    num = PhoneNumber('num')

    def __init__(self, num):
        self.num = num


if __name__ == '__main__':
    customer1 = Customer('444838673')
    print(customer1.num)
