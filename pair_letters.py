# letter pairs

# This is the script used to create the letter pairs which are used for generating names.
# Once the pairs list is generated this is no longer needed, but I wanted to keep it for documentation.

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

vowels = ["a", "e", "i", "o", "u", "y"]

for l in alphabet:
    for v in vowels:
        with open('pairs_output.py', 'a') as t:
            t.write(str('"' + l + v + '"' + ',' + ' '))
