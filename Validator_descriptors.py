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


class Date:
    def __init__(self, date: str):
        self.date = date
        self.pattern = r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}$'
        self.regex = re.compile(self.pattern)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.date in instance.__dict__:
            return instance.__dict__[self.date]
        else:
            raise KeyError(f"Date was not added.")

    def __set__(self, instance, value):
        if not self.regex.match(value):
            print("Wrong date format!")
        else:
            instance.__dict__[self.date] = value
