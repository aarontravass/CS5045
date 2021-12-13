import random

# l=[1,2,4,6,8,11,2,8,4]
l = random.sample(range(0, 101), 100)
count = 0
for i in range(len(l) - 2):
    if (l[i] % 2 == 0 and l[i + 1] % 2 == 0 and l[i + 2] % 2 == 0):
        if (len(set(l[i:i + 3])) == 3):
            count += 1

print(count)
