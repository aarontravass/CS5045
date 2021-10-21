import math

while (1):
    num = int(input("Enter a number: "))
    if (math.pow(math.floor(math.sqrt(num)), 2) == num):
        print("Number is a perfect square")
        break
    print("Number is not a perfect square")
