
# Online Python - IDE, Editor, Compiler, Interpreter
bid_Dictionary = {}
Game = True
max = 0 
bidder = ""
while Game == True:
    name = input("What is your name? ")
    bid = int(input("What is our bid? £"))
    bid_Dictionary[name] = bid
    
    others = input("Are there any other bidders? Type 'yes' or 'no'")
    if others == "no":
        Game = False
        for key in bid_Dictionary:
            #print(key)
            #print(bid_Dictionary[key])
            if max < bid_Dictionary[key]:
                bidder = key
                max = bid_Dictionary[key]
    print("\n"*20)

print(f"The Winner is {bidder} with a bid of £{max}")