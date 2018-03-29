__author__ = 'Trent'

import random

stay_winnings = 0
switch_winnings = 0
for x in range(1000):
    car = random.randint(1,3)
    i = random.randint(1,3)
    choice = random.randint(1,3)
    while choice == car or choice == i:
        choice = random.randint(1,3)
    if i == car:
        stay_winnings += 1
    else:
        switch_winnings += 1

print("Stay Winnings: " + str(stay_winnings))
print("Switch Winnings: " + str(switch_winnings))