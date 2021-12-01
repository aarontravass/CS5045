while 1:
    choice=int(input("Enter a choice(1/2/3/4) "))
    if(choice<1 and choice>4):
        print("Invalid choice")
    else:
        a=float(input("Enter the first number "))
        b=float(input("Enter the second number "))
        result=0
        if choice==1:
            result=a+b
        elif choice==2:
            result=a-b
        elif choice==3:
            result=a*b
        elif choice==4:
            result=a/b
        print("Result is",result)
    f=input("Do you wish to continue? Enter yes or no ").lower()
    if (f!='yes' and f!='no'):
        print("Invalid choice")
    if(f=='no'):
        break