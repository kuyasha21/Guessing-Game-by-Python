
import random

print("\nWelcome to guessing game\n")

live = 4
for i in range(5):
    ran = random.randint(1,5)
    # print(ran)

    user = int(input('Enter a number (1-5): '))

    if ran == user:
        print('Matched..!!\n')
        print('You have won the game.')
        break
    else:
        print('\nOh!! Wrong number.')

    if live == 0:
        print('\nYou do not have any chance left\nBetter luck for next time...\n')
    else:
        print(f"You have {live} chances left...\n")
    live -= 1

