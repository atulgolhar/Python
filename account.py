#!/usr/bin/env python3
#account.py
#Implement a Transaction class that takes an amount, a date, a currency (default USD),
#a USD conversion rate (default is 1), an a description (default None). All of the data
#attributes must be private. Provide the following read-only properties:
#amount, date, currency, usd_conversion_rate, description, usd


import pickle


"""
>>> t = Transaction(100, "2008-12-09")
>>> t.amount, t.currency, t.usd_conversion_rate, t.usd
(100, 'USD', 1, 100)
>>> t = Transaction(250, "2009-03-12", "EUR", 1.53)
>>> t.amount, t.currency, t.usd_conversion_rate, t.usd
(250, 'EUR', 1.53, 382.5)
"""


class Transaction:

    def __init__(self, amount, date, currency="USD", usd_conversion_rate=1, description=None):
        self.__amount = amount
        self.__date = date
        self.__description = description
        self.__currency = currency
        self.__usd_conversion_rate = usd_conversion_rate


    @property
    def amount(self):
        return self.__amount


    @property 
    def date(self):
        return self.__date 


    @property 
    def description(self):
        return self.__description


    @property
    def currency(self):
        return self.__currency


    @property 
    def usd_conversion_rate(self):
        return self.__usd_conversion_rate


    @property 
    def usd(self):
        return self.__amount * self.__usd_conversion_rate


class Account:
    def __init__(self, number, name):
        self.__number = number 
        self.__name = name 
        self.__transactions = []


    @property 
    def number(self):
        "The read-only account number"
        return self.__number


    @property 
    def name(self):
        return self.__name 


    @name.setter 
    def name(self, name):
        assert len(name) > 3, "account name must be at least 4 characters"
        self.__name = name


    def __len__(self):
        "Returns the number of transactions"
        return len(self.__transactions)


    def apply(self, transaction):
        "Applies (adds) the given transaction to the account"
        self.__transactions.append(transaction)


    @property 
    def balance(self):
        "Returns the balance in USD"
        total = 0.0
        for transaction in self.__transactions:
            total += transaction.usd 
        return total


    @property 
    def all_usd(self):
        "Returns True if all transactions are in USD"
        for transaction in self.__transactions:
            if transaction.currency != "USD":
                return False
        return True 


    def save(self):
        "Saves the account's data in file number.acc"
        fh = None
        try:
            data = [self.number, self.name, self.__transactions]
            fh = open(self.number + ".acc", "wb")
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError,pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()


    def load(self):
        fh = None
        try:
            fh = open(self.number + ".acc", "rb")
            data = pickle.load(fh)
            assert self.number == data[0], "account number doesnt match"
            self.__name, self.__transactions = data[1:]
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LaodError(str(err))
        finally:
            if fh is not None:
                fh.close()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
