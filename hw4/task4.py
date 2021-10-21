def list_sum(L, i):
    if (i < len(L)):
        return L[i] + list_sum(L, i + 1)
    return 0

L = [i for i in range(0, 40)]

even_list = [i + list_sum(L, i) for i in L]
print(even_list)
