import sys
from auction_lastname import Auction, User
from bidder_lastname import Bidder

match sys.argv[1]:
    case 'Auction.User':
        u = User()

        match sys.argv[2]:
            case 'Repr':
                print(u)
            case 'Show_Ad':
                print(u)
                temp = [u.show_ad() for i in range(100)]
                print(f'There were {temp.count(True)} Trues and {temp.count(False)} Falses.')
                print(f'The win percentage was {temp.count(True)/len(temp)}')
    case 'Bidder':
        b = Bidder(num_users=1,num_rounds=10)

        match sys.argv[2]:
            case 'Repr':
                print(b)
    case 'Auction.Auction':
        a = Auction(users='hi', bidders='bonjour')

        match sys.argv[2]:
            case 'Repr':
                print(a)
    case 'Official.Code':
        # Initialize bidders
        b0, b1, b2 = Bidder(1,10), Bidder(1,10), Bidder(1,10)

        # Print out the official bidders
        all_bidders = [b0, b1, b2]
        # set this to false if you don't want to print it out
        # instead of commenting out a bunch of lines
        PRINT_BIDDERS = True
        for ind, single in enumerate(all_bidders):
            if PRINT_BIDDERS:
                print(f'This is bidder number {ind}')
                print(single)

        # Initialize Auction
        auction = Auction([User()],[b0, b1, b2])
        # Execute a round
        auction.execute_round()
        bal = auction.balances
    