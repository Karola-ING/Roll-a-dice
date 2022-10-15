def is_a_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def choose_a_dice():
    rolling = True
    while rolling:
        dice = input('How many sided dice do you want to roll?: ')
        if is_a_number(dice) == False:
            print('Your input must be a number.')
            is_a_number(dice)
        else:
            if 3 <= int(dice) < 21:
                return int(dice)
            else:
                print('Dice can only have from 3 to 20 sides. Please try again.')


def times_to_throw(dice):
    rolling = True
    while rolling:
        throws = input(f'How much {dice} sided dices you need?: ')
        if is_a_number(throws) == False:
            print('Your input must be a number.')
            is_a_number(throws)
        else:
            return int(throws)