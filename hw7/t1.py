def bubblesort(mylist):
    num = len(mylist) - 1
    for i in range(num):
        shouldContinue = False
        for j in range(num):
            if mylist[j]>mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
                shouldContinue = True
        print(i, mylist)
        if not shouldContinue:
            break

a=[1,2,3,4]
bubblesort(a)
print(a)