def isalphanum(data: str):
    for s in data:
        if not (s.isalnum() or s.isnumeric()):
            return False
    return True


def check_length(password):
    if (len(password) < 8):
        return 1
    elif (len(password) >= 12):
        return 3
    else:
        return 2


def check_case(password: str):
    if (password.islower() or password.isupper()):
        return 1
    else:
        return 2


def check_content(password: str):
    if password.isalpha():
        return 1
    elif isalphanum(password):
        return 2
    else:
        return 3


def main():
    print("Welcome to the Password Evaluator!")
    while 1:
        password = input('Enter a password or "q" to quit: ')
        if (password == 'q' or password == 'Q'):
            print("Thanks for using the Password Evaluator!")
            break
        score = check_case(password) + check_content(password) + check_length(password)
        print("Score:", score)
        if (score <= 5):
            print("That password is Weak")
        elif (score >= 8):
            print("That password is Strong")
        else:
            print("That password is Acceptable")


if __name__ == "__main__":
    main()
