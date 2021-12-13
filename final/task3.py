import random

turn_arr = []


def main():
    num = random.randint(0, 100)
    turns = 0
    while 1:
        turns += 1
        user = int(input("Enter a guess: "))
        if user > num:
            print("Your guess was bigger. Try again")
        elif user < num:
            print("Your guess was smaller. Try again")
        else:
            print("Correct answer")
            print("Turns:", turns)
            turn_arr.append(turns)
            break


for __ in range(10):
    main();
print(turn_arr)
print(sum(turn_arr) / 10.0)
