auctioners = {}
def add_to_dictionary(name,bid):
    auctioners[name] = bid

while True:
    name = input("whats your name?:\n")
    bid = int(input("whats your bid?:\n"))
    add_to_dictionary(name,bid)
    others = input("Are there other auctioners? 'yes' or 'no':\n ")

    if others == 'no':
        break

highest_bid = 0
highest_bidder = ""
for name,bid in auctioners.items():
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = name

print(f"The highest bid is {highest_bid}, and its by {highest_bidder}")