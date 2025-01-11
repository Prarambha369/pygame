# "A Day in the Life: A Terminal Adventure Game"
day = 1
time_of_day = "morning"
education = True


def display_start_menu():
    print("""
 __  __      ____            _                 _ 
|  \/  |_ __| __ )  __ _ ___| |__  _   _  __ _| |
| |\/| | '__|  _ \ / _` / __| '_ \| | | |/ _` | |
| |  | | |  | |_) | (_| \__ \ | | | |_| | (_| | |
|_|  |_|_|  |____/ \__,_|___/_| |_|\__, |\__,_|_|
                                   |___/         
""")
    print("Welcome to 'A Day in the Life: A Terminal Adventure Game'")
    choice = input("Do you want to start the game? (y/n): ")
    if choice.lower() == "y":
        start_game()
    else:
        print("Thank you for checking out 'A Day in the Life'. Have a great day!")


def start_game():
    global day, time_of_day
    print(f"Day {day}: Good {time_of_day}!")
    print("Welcome to 'A Day in the Life' adventure!")
    morning_routine()


def morning_routine():
    print("You wake up in the morning. What do you want to do first?")
    print("1. Have breakfast")
    print("2. Go for a jog")
    print("3. Skip school")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        have_breakfast()
    elif choice == "2":
        go_for_jog()
    elif choice == "3":
        skip_school()
    else:
        print("Invalid choice. Please try again.")
        morning_routine()


def have_breakfast():
    global time_of_day
    print("You have a healthy breakfast and feel energized.")
    time_of_day = "afternoon"
    next_choice()


def go_for_jog():
    global time_of_day
    print("You go for a refreshing jog and feel great.")
    time_of_day = "afternoon"
    next_choice()


def skip_school():
    global education
    print("You decided to skip school. This might have consequences later.")
    education = False
    next_choice()


def next_choice():
    global time_of_day
    print(f"It's now {time_of_day}. What do you want to do next?")
    print("1. Study")
    print("2. Play a game")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        study()
    elif choice == "2":
        play_game()
    else:
        print("Invalid choice. Please try again.")
        next_choice()


def study():
    global time_of_day
    print("You study for a few hours and learn something new.")
    time_of_day = "evening"
    next_evening_choice()


def play_game():
    global time_of_day
    print("You play a fun game and enjoy your time.")
    time_of_day = "evening"
    next_evening_choice()


def next_evening_choice():
    global time_of_day
    print(f"It's now {time_of_day}. What do you want to do next?")
    print("1. Have dinner")
    print("2. Relax and read a book")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        have_dinner()
    elif choice == "2":
        read_book()
    else:
        print("Invalid choice. Please try again.")
        next_evening_choice()


def have_dinner():
    global time_of_day
    print("You have a delicious dinner and feel satisfied.")
    time_of_day = "night"
    end_day()


def read_book():
    global time_of_day
    print("You relax and read a book, winding down for the day.")
    time_of_day = "night"
    end_day()


def end_day():
    global day, time_of_day, education
    print(f"Day {day} is over. Good night!")
    day += 1
    time_of_day = "morning"
    if not education:
        print("You didn't attend school and died uneducated. Game over.")
        return
    continue_game()


def continue_game():
    choice = input("Do you want to continue to the next day? (y/n): ")
    if choice.lower() == "y":
        start_game()
    else:
        print("Thank you for playing 'A Day in the Life'. Have a great day!")


if __name__ == "__main__":
    display_start_menu()
