# from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
bidders = {}

has_bidder = True

while has_bidder:
  bidder_name = input("What is your name?: ") 
  bid_amount = int(input("What is your bid?: $"))
  has_next_bidder = input("Are there any other bidders? 'yes' or 'no'. ").lower()

  if has_next_bidder == "no":
    has_bidder = False
  else:
    bidders[bidder_name] = bid_amount
    # clear()


def find_highest_bidder(bidders):
  highest_bid_amount = 0
  highest_bidder = ""
  
  for bidder in bidders:
    current_bidder_bid_amount = bidders[bidder]
    
    if current_bidder_bid_amount > highest_bid_amount:
      highest_bid_amount = current_bidder_bid_amount
      highest_bidder = bidder

  return {"name": highest_bidder, "bid_amount": highest_bid_amount}
    

winner = find_highest_bidder(bidders)
name = winner["name"]
amount = winner["bid_amount"]

print(f"The winner is {name} with a bid of ${amount}.")
