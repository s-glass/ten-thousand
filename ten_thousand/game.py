import random
from flo import diff
from random import randint
from ten_thousand.game_logic import GameLogic

class GameLogic:
    @staticmethod
    def roll_dice(num_dice):
        dice_values = []
        for _ in range(num_dice):
            value = random.randint(1, 6)
            dice_values.append(value)
        return tuple(dice_values)

    @staticmethod
    def calculate_score(dice):
        score = 0

        counts = [dice.count(i) for i in range(1, 7)]

        if all(count == 1 for count in counts):
            score += 1500
        elif counts.count(2) == 3:
            score += 1500
        else:
            for i, count in enumerate(counts, start=1):
                if count >= 3:
                    if i == 1:
                        score += 1000 * (count - 2)
                    else:
                        score += i * 100 * (count - 2)
                    counts[i-1] -= 3
            score += counts[0] * 100
            score += counts[4] * 50

        return score

class Banker:
    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def bank(self):
        amount_deposited = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return amount_deposited

    def shelf(self, amt):
        self.shelved += amt

    def clear_shelf(self):
        self.shelved = 0


def play(roller=GameLogic.roll_dice, num_rounds=6):
    global dice_roller
    dice_roller = roller

    print("Welcome to Ten Thousand")
    answer = input("(y)es to play or (n)o to decline\n> ")

    if answer.lower() == 'y':
        play_dice(num_rounds)
    else:
        print("OK. Maybe another time")

def start_new_round(round_num, dice_to_roll):
    print(f"Starting round {round_num}")
  



dice_to_keep = []

def play_dice(num_rounds):
    global dice_to_keep
    round_num = 1
    total_points = 0
    banker = Banker()
    dice_to_roll = 6  # Start with 6 dice

    while round_num <= num_rounds:
        dice_to_keep.clear()
        start_new_round(round_num, dice_to_roll)  # Moved the call here

        roll = dice_roller(dice_to_roll)
        stringified_value = [str(value) for value in roll]
        formatted_roll = " ".join(stringified_value)
        print(f"*** {formatted_roll} ***")

        print("Enter dice to keep, or (q)uit:")
        choice = input("> ")

        if choice == "q":
            print(f"Thanks for playing. You earned {total_points} points")
            break

        for die in choice:
            if die.isdigit() and int(die) in roll:
                dice_to_keep.append(int(die))

        dice_to_roll -= len(dice_to_keep)
        remaining_dice = [die for die in roll if die not in dice_to_keep]

        round_points = GameLogic.calculate_score(dice_to_keep)

        if not dice_to_keep:
            print("Invalid dice selection. You scored 0 points for this round.")
        else:
            total_points += round_points
            banker.shelf(round_points)
            print(f"You have {banker.shelved} unbanked points and {dice_to_roll} dice remaining")

            print("(r)oll again, (b)ank your points or (q)uit:")
            action = input("> ")

            if action == "r":
                dice_to_roll = 6 - len(dice_to_keep)  # Update the number of dice to roll
                print(f"Rolling {dice_to_roll} dice...")
                round_num += 1  # Increment round_num
                continue
            elif action == "b":
                deposited = banker.bank()
                print(f"You banked {deposited} points in round {round_num}")
                round_num += 1
                print(f"Total score is {total_points} points")
                start_new_round(round_num)
            elif action == "q":
                print(f"Thanks for playing. You earned {total_points} points")
                break
            else:
                print("Invalid input. Please enter a valid action.")


if __name__ == "__main__":
    play()
