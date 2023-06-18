
class Bidder:

    def __init__(self, num_users, num_rounds):
        self.__num_users = num_users
        self.__num_rounds = num_rounds 
        self.__current_round = 0
        self.__balances = {}

    def __repr__(self):
        return 'This bidder has ' + str(self.__num_users) + ' users and ' + str(self.__num_rounds) + ' rounds.'

    def __str__(self):
        return 'This bidder has ' + str(self.__num_users) + ' users and ' + str(self.__num_rounds) + ' rounds.'

    def bid(self, user_id):
        pass

    def notify(self, auction_winner, price, clicked):
        pass