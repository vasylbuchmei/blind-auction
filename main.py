from replit import clear
from art import logo
print(logo, "\nWelcome to the secret auction program")

bidding_finished=False
bids={}

def find_higher_bidder(bidding_record):
  highest_bid=0
  winner=""
  # bidding_record = {"name":"price"} (bids)
  for bidder in bidding_record:
    bid_amount=bidding_record[bidder]
    if bid_amount>highest_bid:
      highest_bid=bid_amount
      winner=bidder
  print(f"The winner is {winner} with a bid of {highest_bid}$")

while not bidding_finished:
  name=input("What is your name?: ")
  price=int(input("What is your bid?: $"))
  bids[name]=price
  should_continue=input("Are there any other bidders? Type 'yes' or 'no.'\n")
  if should_continue=="no":
    bidding_finished=True
    find_higher_bidder(bids)
  elif should_continue=="yes":
    clear()
    
