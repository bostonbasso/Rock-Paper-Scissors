# Write your code here
import random

print('Enter your name: ', end='')
player_name = input()
print('Hello, ' + player_name)

options = input()

if len(options) == 0:
    options = ['rock', 'paper', 'scissors']
else:
    options = options.split(',')

print("Okay, let's start")

player_score = 0

rating_file = open('rating.txt')

for line in rating_file:
    player, score = line.split()

    if player_name == player:
        player_score = int(score)
        break

rating_file.close()

while True:
    choice = input()

    if choice == '!exit':
        print('Bye!')
        break
    elif choice == '!rating':
        print('Your rating: ' + str(player_score))
    elif choice in options:
        option = random.choice(options)
        option_index = options.index(option)
        new_options = options[option_index + 1:]
        new_options.extend(options[:option_index])

        if choice == option:
            print('There is a draw (' + choice + ')')
            player_score += 50
        elif choice in new_options[:len(new_options) // 2]:
            print('Well done. Computer chose {0} and failed'.format(option))
            player_score += 100
        else:
            print('Sorry, but computer chose ' + option)
    else:
        print('Invalid input')
