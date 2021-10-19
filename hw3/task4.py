def main():
    s = input("Enter a string = ")
    if (len(s) != 5):
        print("String length should be 5")
        return
    a = [i for i in s]
    a.sort()
    print(a)
    new_str = ''.join(a)
    print(new_str)


main()
