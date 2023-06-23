import random, builtins
from flo import diff 
      

# Roger's code from Lab 6
class GameLogic:


    @staticmethod
    def roll_dice(num_dice):
        # return tuple(random.randint(1, 6) for _ in range(num_dice))
        dice_values = []
        for _ in range(num_dice):
            value = random.randint(1, 6)
            dice_values.append(value)
        return tuple(dice_values)



# Chat GPT final product - see README.md
    @staticmethod
    def calculate_score(dice):
        score = 0

        # Count the occurrences of each number
        counts = [dice.count(i) for i in range(1, 7)]

        # Check for straight
        if all(count == 1 for count in counts):
            return 1500

        # Calculate the score for individual 1s and 5s
        score += counts[0] * 100
        score += counts[4] * 50

        # Check for three or more of the same number
        for i in range(1, 7):
            if counts[i - 1] >= 3:
                if i == 1:
                    score += 1000 * (counts[i - 1] - 2) - counts[0] * 100
                else:
                    score += i * 100 * (counts[i - 1] - 2) - counts[4] * 50

                counts[i - 1] = 0

        # Check for three pairs
        if counts.count(2) == 3:
            score += 1500

        return score


class Banker:
    """Banker is reponsible for tracking points "on the shelf" and "in the bank"
    version_1
    """
    def __init__(self):
        self.balance = 0  # 200
        self.shelved = 0  # 0

    def bank(self):
        amount_deposited = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return amount_deposited

    def shelf(self, amt):
        self.shelved += amt

    def clear_shelf(self):
        self.shelved = 0