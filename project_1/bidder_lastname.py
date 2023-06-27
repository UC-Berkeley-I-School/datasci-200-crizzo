
class Bidder:
    """Creates a bidder to bid on the ad being served to the User."""

    def __init__(self, num_users, num_rounds):
        self.__num_users = num_users
        self.__num_rounds = num_rounds
        self.__current_round = 0
        self.__balances = {}

        #an initializer with the definition def __init__(self, num_users, num_rounds) , in which num_users contains the number of User objects in the game, and num_rounds contains the total number of rounds to be played. The Bidder might want to use this info to help plan its strategy.

    def __repr__(self):
        return 'This bidder has ' + str(self.__num_users) + ' users and ' + str(self.__num_rounds) + ' rounds.'

    def __str__(self):
        return 'This bidder has ' + str(self.__num_users) + ' users and ' + str(self.__num_rounds) + ' rounds.'

    def bid(self, user_id):
        # a bid method with the definition def bid(self, user_id) , which returns a non-negative amount of money, in dollars round to three (3) decimal places
        import numpy as np
        num = np.random.rand()
        return num

    def notify(self, auction_winner, price, clicked):
        pass
        #a notify method with the definition def notify(self, auction_winner, price, clicked) , which is used to send information about what happened in a round back to the Bidder . Here, auction_winner is a boolean to represent whether the given Bidder won the auction ( True ) or not ( False ). price is the amount of the second bid, which the winner pays. If the given Bidder won the auction, clicked will contain a boolean value to represent whether the user clicked on the ad. If the given Bidder did not win the auction, clicked will always contain None .