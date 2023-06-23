from random import randint
from ten_thousand.game_logic import GameLogic

dice_roller = GameLogic.roll_dice
# def default_roller():
#     # GameLogic.roll_dice(roller)
#     return randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)

# def round_starter():
def play(roller = GameLogic.roll_dice, num_rounds = 6):
    global dice_roller

    dice_roller = roller
    print("Welcome to Ten Thousand")
    answer = input("(y)es to play or (n)o to decline\n> ")

    if answer.lower() == 'y':
        play_dice(num_rounds)
    else:
        print("OK. Maybe another time")
    

def play_dice(num_rounds):
    while True:
            round_num = 1
            max_rounds = num_rounds
            total_points = 0
            # roll = GameLogic.roll_dice(roller)
            roll_str = ""
            print(f"Starting round {round_num}")
            print('Rolling 6 dice...')
            roll = dice_roller(6)
            for num in roll:
                roll_str += str(num) + " "
            print(f"*** {roll_str}***")
            print("Enter dice to keep, or (q)uit:")
            choice = input("> ")
            # dice_roll_points = GameLogic.calculate_score(choice)
            if choice == "q":
              print("Thanks for playing. You earned 0 points")
              break

## From Chat GPT
# def play_dice(num_rounds):
#     round_num = 1
#     total_score = 0

#     while round_num <= num_rounds:
#         print(f"Starting round {round_num}")
#         print("Rolling 6 dice...")
#         roll = dice_roller(6)
#         roll_str = " ".join(str(num) for num in roll)
#         print(f"*** {roll_str} ***")

#         print("Enter dice to keep, or (q)uit:")
#         choice = input("> ")

#         if choice == "q":
#             print(f"Thanks for playing. You earned {total_score} points")
#             break

#         # Calculate the score for the chosen dice
#         dice_roll_points = GameLogic.calculate_score(choice)

#         print(f"You have {dice_roll_points} unbanked points and {6 - len(choice)} dice remaining")
#         print("(r)oll again, (b)ank your points or (q)uit:")
#         action = input("> ")

#         if action == "b":
#             total_score += dice_roll_points
#             print(f"You banked {dice_roll_points} points in round {round_num}")
#             print(f"Total score is {total_score} points")
#             round_num += 1
#         elif action == "q":
#             print(f"Thanks for playing. You earned {total_score} points")
#             break

#     if round_num > num_rounds:
#         print(f"You completed {num_rounds} rounds. Final score: {total_score} points")



if __name__ == "__main__":
    play()


# def play(roller = None):
#     print("Welcome to Ten Thousand")
#     print("(y)es to play or (n)o to decline")
#     player_input = input("> ")
#     if player_input == "n":
#          print("OK. Maybe another time")
#     elif player_input == "y":
#             print("Starting round 1")
#             print("Rolling 6 dice...")
#             print("*** 4 4 5 2 3 1 ***")
#             print("Enter dice to keep, or (q)uit:")
#             print("> q")
#             print("Thanks for playing. You earned 0 points")



# from random import randint


# def default_roller():
#     return randint(1, 6, ), randint(1, 6, )


# def play_dice(roller=default_roller):

#     while True:
#         print("Enter r to roll or q to quit")
#         choice = input("> ")

#         if choice == "q":
#             print("OK, bye")
#             break
#         else:
#             roll = roller()
#             roll_str = ""
#             for num in roll:
#                 roll_str += str(num) + " "
#             print(f"*** {roll_str}***")


# if __name__ == "__main__":
#     rolls = [(1, 1), (3, 3), (2, 2)]

#     def mock_roller():
#         return rolls.pop(0) if rolls else default_roller()

#     play_dice(mock_roller)






# Notes on banking score
# current score = 0
# def bank_score(total_score, current_score):
    # total_score += current_score
    # current_score = 0
    # return total_score, current_score

# total_score, current_score = bank_score(total_score, current_score)
# if current_score > 0:
#     total_score, current_score = bank_score(total_score, current_score)
# else:
#     print("You can only bank your score when you have points to bank.")


# import random


# def play_dice(roller):
#     round_num = 1
#     total_score = 0

#     while True:
#         print(f"Starting round {round_num}")
#         print("Rolling 6 dice...")
#         roll = GameLogic.roll_dice(roller)
#         roll_str = " ".join(str(num) for num in roll)
#         print(f"*** {roll_str} ***")

#         dice_remaining = list(roll)
#         unbanked_points = 0

#         while True:
#             print("Enter dice to keep, or (q)uit:")
#             choice = input("> ")

#             if choice == "q":
#                 print(f"Thanks for playing. You earned {total_score} points")
#                 return
#             else:
#                 try:
#                     selected_dice = list(map(int, choice))
#                     if not all(die in dice_remaining for die in selected_dice):
#                         raise ValueError
#                 except ValueError:
#                     print("Invalid input. Please enter valid dice to keep.")
#                     continue

#                 unbanked_points += roller.calculate_score(selected_dice)
#                 dice_remaining = [die for die in dice_remaining if die not in selected_dice]

#                 print(f"You have {unbanked_points} unbanked points and {len(dice_remaining)} dice remaining")
#                 print("(r)oll again, (b)ank your points or (q)uit:")
#                 choice = input("> ")

#                 if choice == "q":
#                     print(f"Thanks for playing. You earned {total_score} points")
#                     return
#                 elif choice == "b":
#                     total_score += unbanked_points
#                     print(f"You banked {unbanked_points} points in round {round_num}")
#                     print(f"Total score is {total_score} points")
#                     round_num += 1
#                     break
#                 elif choice != "r":
#                     print("Invalid input. Please enter 'r', 'b', or 'q'.")
#                     continue


# def play(roller):
#     print("Welcome to Ten Thousand")
#     answer = input("(y)es to play or (n)o to decline\n> ")

#     if answer.lower() == 'y':
#         play_dice(roller)


# game_logic = GameLogic()
# play(game_logic)
