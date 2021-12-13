def reverse(l):
    return [l[i] for i in range(len(l) - 1, -1, -1)]


a = [1, 4, 2, 6, 7]
print(reverse(a))
