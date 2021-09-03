# Username Generator

import random
import math

def pair_letters():
    # This is how I originally made the pairs list below. This function is now unused.
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    vowels = ["a", "e", "i", "o", "u", "y"]

    for l in alphabet:
        for v in vowels:
            with open('pairs_output.py', 'a') as t:
                t.write(str('"' + l + v + '"' + ',' + ' '))

pairs = ["aa", "ae", "ai", "ao", "au", "ay", "ba", "be", "bi", "bo", "bu", "by", "ca", "ce", "ci", "co", "cu", "cy", "da", "de", "di", "do", "du", "dy", "ea", "ee", "ei", "eo", "eu", "ey", "fa", "fe", "fi", "fo", "fu", "fy", "ga", "ge", "gi", "go", "gu", "gy", "ha", "he", "hi", "ho", "hu", "hy", "ia", "ie", "ii", "io", "iu", "iy", "ja", "je", "ji", "jo", "ju", "jy", "ka", "ke", "ki", "ko", "ku", "ky", "la", "le", "li", "lo", "lu", "ly", "ma", "me", "mi", "mo", "mu", "my", "na", "ne", "ni", "no", "nu", "ny", "oa", "oe", "oi", "oo", "ou", "oy", "pa", "pe", "pi", "po", "pu", "py", "qa", "qe", "qi", "qo", "qu", "qy", "ra", "re", "ri", "ro", "ru", "ry", "sa", "se", "si", "so", "su", "sy", "ta", "te", "ti", "to", "tu", "ty", "ua", "ue", "ui", "uo", "uu", "uy", "va", "ve", "vi", "vo", "vu", "vy", "wa", "we", "wi", "wo", "wu", "wy", "xa", "xe", "xi", "xo", "xu", "xy", "ya", "ye", "yi", "yo", "yu", "yy", "za", "ze", "zi", "zo", "zu", "zy"]

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
