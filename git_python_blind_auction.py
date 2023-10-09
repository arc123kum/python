#blind auction
def winner(bidder_dict):
    heighest_bidd = 0
    heighest_bidder =""
    for key in bidder_dict:
        if heighest_bidd < bidder_dict[key]:
            heighest_bidd = bidder_dict[key]
            heighest_bidder = key
    print(f"{heighest_bidder} is the winner with {heighest_bidd}")

print("Welcome to the secret auction program.")

bidder_dict = {}
another_person = "yes"


while another_person == "yes":
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))

    bidder_dict[name]= bid_amount
    another_person = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    #clear()


print(bidder_dict)
winner(bidder_dict)
