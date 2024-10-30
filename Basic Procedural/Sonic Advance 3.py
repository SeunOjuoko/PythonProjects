import random

friends = ["Sonic","Tails","Knuckles","Amy","Cream"]

#Option 1
RNG = random.randint(0, 4)
print(friends[RNG])

#Option 2
print(random.choice(friends))