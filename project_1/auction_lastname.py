import numpy as np

class User:
    """A person maybe clicking on an ad"""

    def __init__(self):
        # a private __probability attribute to represent the probability of clicking on an ad.
        self.__probability = np.random.rand()

    def __repr__(self):
        return 'The user has a probability of ' + str(self.__probability)

    def __str__(self):
        return 'The user has a probability of ' + str(self.__probability)

    def show_ad(self):
        """a show_ad method with the definition def show_ad(self) that represents showing an ad to this User . This method should return True to represent the user clicking on and ad and False otherwise."""
        return np.random.choice([True, False], p=[self.__probability, 1 - self.__probability])

class Auction:
    """Run the auction between Users and Bidders"""

    def __init__(self, users, bidders):
        self.__users_list = users
        self.__bidders_list = bidders
        self.balances = []

    def __repr__(self):
        return 'hello'

    def __str__(self):
        return str([self.__users_list, self.__bidders_list])

    def execute_round(self):
        pass
        #an execute_round method with the header def execute_round(self) . This method should execute all steps within a single round of the game.