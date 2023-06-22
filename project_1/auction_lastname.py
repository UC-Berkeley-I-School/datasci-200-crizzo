import numpy as np

class User:

    def __init__(self):
        self.__probability = np.random.rand()

    def __repr__(self):
        return 'The user has a probability of ' + str(self.__probability)

    def __str__(self):
        return 'The user has a probability of ' + str(self.__probability)

    def show_ad(self):
        return np.random.choice([True, False], p=[self.__probability, 1 - self.__probability])

class Auction:

    def __init__(self, users, bidders):
        self.__users_list = users
        self.__bidders_list = bidders

    def __repr__(self):
        return 'hello'

    def __str__(self):
        return str([self.__users_list, self.__bidders_list])

    def execute_round(self):
        pass