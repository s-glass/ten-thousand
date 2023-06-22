## Prompt 1
  - In python, do the following:
Today is all about tackling the highest risk and/or highest priority features - scoring and dice rolling.
Define a GameLogic class in ten_thousand/game_logic.py file.
Handle calculating score for dice roll
Add calculate_score static method to GameLogic class.
The input to calculate_score is a tuple of integers that represent a dice roll.
The output from calculate_score is an integer representing the roll’s score according to rules of game.

## Code Output 1
- class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        if not dice_roll:
            return 0

        score = 0
        dice_values = [0]*7  # 1-indexed

        for die in dice_roll:
            dice_values[die] += 1

        # scoring triples
        for i in range(1, 7):
            while dice_values[i] >= 3:
                if i == 1:
                    score += 1000
                else:
                    score += i * 100
                dice_values[i] -= 3

        # scoring singles
        score += dice_values[1]*100
        score += dice_values[5]*50

        return score




## Prompt 1
### Prompt 1a
Handle rolling dice
Add roll_dice static method to GameLogic class.
The input to roll_dice is an integer between 1 and 6.
The output of roll_dice is a tuple with random values between 1 and 6.
The length of tuple must match the argument given to roll_dice method.

### Prompt 2a
- expand this method into a simpler way     @staticmethod
    def roll_dice(n):
        if not 1 <= n <= 6:
            raise ValueError("The number of dice to roll must be between 1 and 6.")
        return tuple(random.randint(1, 6) for _ in range(n))

## Code Output

### Output 1a
import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        # ... rest of code ...

    @staticmethod
    def roll_dice(n):
        if not 1 <= n <= 6:
            raise ValueError("The number of dice to roll must be between 1 and 6.")
        return tuple(random.randint(1, 6) for _ in range(n))

### Output 2a
    @staticmethod
    def roll_dice(n):
        # Check if the input is within the valid range
        if not 1 <= n <= 6:
            raise ValueError("The number of dice to roll must be between 1 and 6.")
        
        # Create an empty list to store the roll results
        roll_results = []

        # Repeat for n times
        for _ in range(n):
            # Generate a random integer between 1 and 6
            roll = random.randint(1, 6)

            # Append the result to the list
            roll_results.append(roll)

        # Convert the list to a tuple and return
        return tuple(roll_results)


### Prompt itself:

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
                    score += 1000 - (counts[0] * 100)  # subtract the score     already added for individual 1's
                else:
                    score += 100 * i - (counts[i - 1] * 50 if i == 5 else 0)  #     subtract the score already added for individual 5's
    
                counts[i - 1] -= 3
    
        return score

this gives me and error:  def test_four_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2))
    expected = 400
    assert actual == expected
E    assert 200 == 400
tests/version_1/test_calculate_score.py:88: AssertionError


###  still getting errors:

test_input = (2, 2, 3, 3, 6, 6), expected = 1500
  @pytest.mark.parametrize(
    "test_input,expected",
    [
      (tuple(), 0),
      ((1,), 100),
      ((1, 1), 200),
      ((1, 1, 1), 1000),
      ((1, 1, 1, 1), 2000),
      ((1, 1, 1, 1, 1), 3000),
      ((1, 1, 1, 1, 1, 1), 4000),
      ((2,), 0),
      ((2, 2), 0),
      ((2, 2, 2), 200),
      ((2, 2, 2, 2), 400),
      ((2, 2, 2, 2, 2), 600),
      ((2, 2, 2, 2, 2, 2), 800),
      ((3,), 0),
      ((3, 3), 0),
      ((3, 3, 3), 300),
      ((3, 3, 3, 3), 600),
      ((3, 3, 3, 3, 3), 900),
      ((3, 3, 3, 3, 3, 3), 1200),
      ((4,), 0),
      ((4, 4), 0),
      ((4, 4, 4), 400),
      ((4, 4, 4, 4), 800),
      ((4, 4, 4, 4, 4), 1200),
      ((4, 4, 4, 4, 4, 4), 1600),
      ((5,), 50),
      ((5, 5), 100),
      ((5, 5, 5), 500),
      ((5, 5, 5, 5), 1000),
      ((5, 5, 5, 5, 5), 1500),
      ((5, 5, 5, 5, 5, 5), 2000),
      ((6,), 0),
      ((6, 6), 0),
      ((6, 6, 6), 600),
      ((6, 6, 6, 6), 1200),
      ((6, 6, 6, 6, 6), 1800),
      ((6, 6, 6, 6, 6, 6), 2400),
      ((1, 2, 3, 4, 5, 6), 1500),
      ((2, 2, 3, 3, 4, 6), 0),
      ((2, 2, 3, 3, 6, 6), 1500),
      ((1, 1, 1, 2, 2, 2), 1200),
    ],
  )
  # @pytest.mark.skip("Pending")
  def test_all(test_input, expected):
    actual = GameLogic.calculate_score(test_input)
>    assert actual == expected
E    assert 0 == 1500
tests/version_1/test_calculate_score.py:162: AssertionError




## Prompt 3

Given this code:
class GameLogic:


    @staticmethod
    def roll_dice(num_dice):
        # return tuple(random.randint(1, 6) for _ in range(num_dice))
        dice_values = []
        for _ in range(num_dice):
            value = random.randint(1, 6)
            dice_values.append(value)
        return tuple(dice_values)



    
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

And these tests:
import pytest
from ten_thousand.game_logic import GameLogic
#
pytestmark = [pytest.mark.version_1]


# @pytest.mark.skip("Pending")
def test_single_five():
    actual = GameLogic.calculate_score((5,))
    expected = 50
    assert actual == expected


# @pytest.mark.skip("Pending")
def test_single_one():
    actual = GameLogic.calculate_score((1,))
    expected = 100
    assert actual == expected


# @pytest.mark.skip("Pending")
def test_two_fives():
    actual = GameLogic.calculate_score((5, 5))
    expected = 100
    assert actual == expected


# @pytest.mark.skip("Pending")
def test_two_ones():
    actual = GameLogic.calculate_score((1, 1))
    expected = 200
    assert actual == expected


# @pytest.mark.skip("Pending")
def test_one_and_five():
    actual = GameLogic.calculate_score((1, 5))
    expected = 150
    assert actual == expected


# @pytest.mark.skip("Pending")
def test_zilch():
    actual = GameLogic.calculate_score((2,))
    expected = 0
    assert actual == expected


# @pytest.mark.skip("Pending")
def test_three_fives():
    actual = GameLogic.calculate_score((5, 5, 5, 2, 2, 3))
    expected = 500
    assert actual == expected


# @pytest.mark.skip("Pending")
def test_three_ones():
    actual = GameLogic.calculate_score((1, 1, 1, 2, 3, 4))
    expected = 1000
    assert actual == expected


# @pytest.mark.skip("Pending")
def test_three_ones_and_a_five():
    actual = GameLogic.calculate_score((1, 1, 1, 5))
    expected = 1050
    assert actual == expected


# @pytest.mark.skip("Pending")
def test_straight():
    actual = GameLogic.calculate_score((1, 6, 3, 2, 5, 4))
    expected = 1500
    assert actual == expected


# @pytest.mark.skip("Pending")
def test_three_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2))
    expected = 200
    assert actual == expected


# @pytest.mark.skip("Pending")
def test_four_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2))
    expected = 400
    assert actual == expected


# @pytest.mark.skip("Pending")
def test_five_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2, 2))
    expected = 600
    assert actual == expected


# @pytest.mark.skip("Pending")
def test_six_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2, 2, 2))
    expected = 800
    assert actual == expected


# @pytest.mark.skip("Pending")
def test_six_ones():
    actual = GameLogic.calculate_score((1, 1, 1, 1, 1, 1))
    expected = 4000
    assert actual == expected


# @pytest.mark.skip("Pending")
@pytest.mark.parametrize(
    "test_input,expected",
    [
        (tuple(), 0),
        ((1,), 100),
        ((1, 1), 200),
        ((1, 1, 1), 1000),
        ((1, 1, 1, 1), 2000),
        ((1, 1, 1, 1, 1), 3000),
        ((1, 1, 1, 1, 1, 1), 4000),
        ((2,), 0),
        ((2, 2), 0),
        ((2, 2, 2), 200),
        ((2, 2, 2, 2), 400),
        ((2, 2, 2, 2, 2), 600),
        ((2, 2, 2, 2, 2, 2), 800),
        ((3,), 0),
        ((3, 3), 0),
        ((3, 3, 3), 300),
        ((3, 3, 3, 3), 600),
        ((3, 3, 3, 3, 3), 900),
        ((3, 3, 3, 3, 3, 3), 1200),
        ((4,), 0),
        ((4, 4), 0),
        ((4, 4, 4), 400),
        ((4, 4, 4, 4), 800),
        ((4, 4, 4, 4, 4), 1200),
        ((4, 4, 4, 4, 4, 4), 1600),
        ((5,), 50),
        ((5, 5), 100),
        ((5, 5, 5), 500),
        ((5, 5, 5, 5), 1000),
        ((5, 5, 5, 5, 5), 1500),
        ((5, 5, 5, 5, 5, 5), 2000),
        ((6,), 0),
        ((6, 6), 0),
        ((6, 6, 6), 600),
        ((6, 6, 6, 6), 1200),
        ((6, 6, 6, 6, 6), 1800),
        ((6, 6, 6, 6, 6, 6), 2400),
        ((1, 2, 3, 4, 5, 6), 1500),
        ((2, 2, 3, 3, 4, 6), 0),
        ((2, 2, 3, 3, 6, 6), 1500),
        ((1, 1, 1, 2, 2, 2), 1200),
    ],
)
# @pytest.mark.skip("Pending")
def test_all(test_input, expected):
    actual = GameLogic.calculate_score(test_input)
    assert actual == expected

What are more tests I can run


## Code Output 3

`def test_no_scoring_dice():
    actual = GameLogic.calculate_score((2, 3, 4, 6))
    expected = 0
    assert actual == expected

def test_three_pairs():
    actual = GameLogic.calculate_score((1, 1, 2, 2, 3, 3))
    expected = 1500
    assert actual == expected

def test_mixed_scoring_dice():
    actual = GameLogic.calculate_score((1, 1, 1, 2, 2, 6))
    expected = 1100
    assert actual == expected

def test_all_same_number():
    actual = GameLogic.calculate_score((4, 4, 4, 4, 4, 4))
    expected = 1600
    assert actual == expected

def test_large_straight():
    actual = GameLogic.calculate_score((2, 3, 4, 5, 6, 1))
    expected = 1500
    assert actual == expected

def test_no_scoring_dice_with_three_pairs():
    actual = GameLogic.calculate_score((2, 2, 3, 3, 4, 4))
    expected = 1500
    assert actual == expected`


## Prompt 4

when building a python cli game of farkle, how do I bank the current score 

## Code Output 4

Create a variable to hold the current score, initialized to zero at the beginning of the game. For example:
python
Copy code
current_score = 0
During the game, the player accumulates points based on their dice rolls. When they decide to bank their current score, you need to add the current score to their total score and reset the current score to zero. You can use a function to handle this logic. Here's an example:
python
Copy code
def bank_score(total_score, current_score):
    total_score += current_score
    current_score = 0
    return total_score, current_score
Whenever the player chooses to bank their score, you can call the bank_score function and update the variables accordingly. For example:
python
Copy code
total_score, current_score = bank_score(total_score, current_score)
Here, total_score represents the player's cumulative score throughout the game.

You might also want to add some validation to ensure the player can only bank their score when they have accumulated points. For instance, you can include a check before calling the bank_score function:
python
Copy code
if current_score > 0:
    total_score, current_score = bank_score(total_score, current_score)
else:
    print("You can only bank your score when you have points to bank.")
By following these steps, you can implement the banking of the current score in your Python CLI game of Farkle. Remember to adapt the code to fit within the structure and rules of your specific game implementation.