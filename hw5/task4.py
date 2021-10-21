for i in range(10, 100):
    mul = i * i
    if ((mul - i) % 100 == 0 and mul <= 999):
        print(i, "is the number which satisfies the conditions")
