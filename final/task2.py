import random

letters = ['A', 'C', 'T', 'G']
data = ""
for j in range(5):
    length = 21 + (3 * random.randint(0, 3))
    seq = ""
    for i in range(length):
        seq += letters[random.randint(0, len(letters) - 1)]
    data += ">dna" + str(j + 1) + "\n"
    data += seq + "\n"
data = data.strip()
file = open('output.fas', 'w')
file.write(data)
file.close()
