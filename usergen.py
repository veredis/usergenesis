# Username Generator

import random
import math
from pairs_output import pairs

amount = int(input("Number of Usernames? "))
length = int(input("Length of Usernames? "))

print("\n")

# divides length by 2 since each pair already has 2 letters
k_val = length / 2

# if the length was an odd number, this rounds up the decimal from a float to an int
if isinstance(k_val, float):
    k_val = int(math.ceil(k_val))

def user_gen(amt):
    for i in range(amt):
        name = "".join(random.choices(pairs, k=k_val))
        # cuts off the last letter if length is odd and too long
        if len(name) > length:
            name = name[:length]
        print(name)
        with open('usernames.txt', 'a') as t:
            t.write(name + '\n')

user_gen(amount)

print("\n\nDone. Appended to usernames.txt")
