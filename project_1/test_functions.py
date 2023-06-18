import sys
import auction_lastname
import bidder_lastname

match sys.argv[1]:
    case 'Auction':
        u = auction_lastname.User()

        match sys.argv[2]:
            case 'Repr':
                print(u)
            case 'Show_Ad':
                print(u)
                temp = [u.show_ad() for i in range(100)]
                print(f'There were {temp.count(True)} Trues and {temp.count(False)} Falses.')
                print(f'The win percentage was {temp.count(True)/len(temp)}')
    case 'Bidder':
        b = bidder_lastname.Bidder(num_users=1,num_rounds=10)

        match sys.argv[2]:
            case 'Repr':
                print(b)