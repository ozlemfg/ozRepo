# NUMBER GAME WITH FUNCTIONS

# ask number between 1 and 10
# for any digit entry, continue
# if the next number  within the range is smaller, end the game

def get_valid_number():
    while True:
        try:
            number = int(input("enter a number between 1 and 10: "))
            if number in range(1, 11):
                return number
            else:
                print("number is out of range, try again")
        except ValueError:
            print("only digit")


def play_game():
    previous = get_valid_number()

    while True:
        current = get_valid_number()

        if current < previous:
            print(f"Game over! {current} is smaller than {previous}")
            break

        previous = current

play_game()
