import simple_colors
import re
from simple_colors import *


class Bank_user:  # Parent Class
    def __init__(self, first_name, last_name, gender, age):
        """

        :param first_name: User's first name in string
        :param last_name: User's last name in string
        :param age: User's age in int
        :param gender: User's gender in string

        """
        try:
            self.first_name = first_name
            self.last_name = last_name
            self.gender = gender.lower()
            self.age = age
            pattern_1 = re.compile(r'\d+')
            while bool(re.search(pattern_1, self.first_name)) is True:
                first_name = input('Type first name in letters only: ')
                self.first_name = first_name
            while bool(re.search(pattern_1, self.last_name)) is True:
                last_name = input('Type last name in letters only: ')
                self.last_name = last_name
            while self.gender != 'female' and self.gender != 'male':
                gender = input('Type either male or female: ')
                self.gender = gender
            while type(self.age) != int:
                age = int(input('Type age as a whole number: '))
                self.age = age
            self.full_name = self.first_name + ' ' + self.last_name
        except TypeError:
            print('Please check your first and last input/argument.')
        except AttributeError:
            print('Please check gender input/argument.')
        print(black('User Info', ['bold']))

    def details(self):
        try:
            print('')
            print(black('Full Name: ', ['bold']), self.full_name)
            print(black('Age: ', ['bold']), self.age)
            print(black('Gender: ', ['bold']), self.gender)
        except AttributeError:
            print('Please check inputs generally')


class Account_info(Bank_user):  # Inheritance Class
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.balance = 0

    def deposit(self, amt_deposited):
        try:
            self.details()
            self.amt_deposited = amt_deposited
            self.balance += self.amt_deposited
            print(black('Amount deposited: ', ['bold']), self.amt_deposited)
            print(black('Updated Account Balance: ', ['bold']), self.balance)

        except TypeError:
            try:
                print('Please enter a valid for your deposited amount')
                amt_deposited = eval(input('Please enter numbers greater than zero: '))
                if amt_deposited > 0:
                    pass
                else:
                    while amt_deposited <= 0:
                        print('Please enter a valid deposited amount')
                        amt_deposited = eval(input('Please enter numbers greater than zero: '))
                        self.amt_deposited = amt_deposited
                        self.balance += self.amt_deposited
            except NameError:
                print('You inserted letters again, retry again!!!')

    def withdraw(self, amt_taken):
        try:
            self.details()
            self.amt_taken = amt_taken
            while self.amt_taken > self.balance:
                print('Insufficient funds.')
                amt_taken = eval(input('Please enter amount less than balance: '))
                self.amt_taken = amt_taken
            while self.amt_taken <= 0:
                print('Input a valid amount greater than zero.')
                amt_taken = eval(input('Please enter amount less than balance: '))
                self.amt_taken = amt_taken
            self.balance -= self.amt_taken
            print(black('Amount Withdrawn: ', ['bold']), self.amt_taken)
            print(black('Updated Account Balance: ', ['bold']), self.balance)
        except TypeError:
            print('Please enter a valid Withdrawn amount')

    def view_balance(self):
        self.details()
        print(black('Account Balance: ', ['bold']), self.balance)
