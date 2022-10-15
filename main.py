import random
from rolling import choose_a_dice, times_to_throw


def roll():
    dice = choose_a_dice()
    throws = times_to_throw(dice)

    rolls = []
    for throw in range(1, throws + 1):
        roll = (random.randrange(1, dice + 1))
        rolls.append(roll)

    result = 0
    for roll in rolls:
        result += roll

    return f'Your dices show: {rolls}. Overall result is: {result}.'


if __name__ == '__main__':
    print(roll())
    roll_again = True
    while roll_again:
        again = input('Do yo want to roll again? (Yes/No): ')
        if again.upper() == 'Y' or again.upper() == 'YES':
            print(roll())
        else:
            print('Thank you!')
            roll_again = False



