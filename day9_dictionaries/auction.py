bids = []
auction_open = True
while auction_open:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bids.append({"name":name, "bid":bid})
    more_bids = input("Are there more bids?: ")
    if more_bids == 'n':
        auction_open = False
        winner = ''
        highest = 0
        for bid in bids:
            if bid["bid"] > highest:
                highest = bid["bid"]
                winner = bid["name"]
        print(f"The winner is {winner}, with a bid of {highest}")

 

