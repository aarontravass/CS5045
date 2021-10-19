def func(s):
    if (len(s) != 5):
        print("String length should be 5")
        return
    a = [i for i in s]
    a.sort()
    new_str = ''.join(a)
    print(new_str)


func(input("Enter a string = "))
