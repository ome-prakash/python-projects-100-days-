from art import logo

print(logo)

def find_highest_bid(bid_dictionary):
    winner=""
    highest_bid = 0
    for bidder in bid_dictionary:
        if bid_dictionary[bidder] > highest_bid:
            highest_bid = bid_dictionary[bidder]
            winner = bidder
    print(f"The winner is {winner}! with a bid of {highest_bid}")

bids={}
continue_bidding = True
while continue_bidding:
    name = input("What is your name? \n")
    bid = int(input("What is your bid? \n"))
    bids[name] = bid
    bidders = (input("Are there any other bidders? Type 'yes or 'no'. \n")).lower()
    if bidders == "no":
        continue_bidding = False
        find_highest_bid(bids)
    elif bidders == "yes":
        print("\n"*50)











