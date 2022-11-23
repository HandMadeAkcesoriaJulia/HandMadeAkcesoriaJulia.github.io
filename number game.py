import random

#mynumber = 0
#count = 0
#while(mynumber != 1000 and mynumber != 1):
#    mynumber = random.randrange(1, 1001)
#    print(mynumber)
#    count += 1

#print(count)

mynumber = random.randrange(1, 1001)
guess = 0
count_player = 0
while (mynumber != guess):
    count_player += 1
    guess_str = input('guess my number: ')
    guess = int(guess_str)
    if (guess > mynumber):
        print('the number is smaller')
    if (guess < mynumber):
        print('the number is bigger')
    if (guess == mynumber):
        print('Congrats, you guessed it! You used ' + str(count_player) + ' attempts')


min_number = 1
max_number = 1000
answer = ''
count_cpu = 0 
while (answer != '='):
    count_cpu += 1
    guess = random.randrange(min_number, max_number + 1)
    answer = input('is your number ' + str(guess) + '? ') 
    if (answer == '>'):
        min_number = guess + 1
    if (answer == '<'):
        max_number = guess - 1
    if (answer == '='):
        print('gefeliciteerd meid!')

print(f'Player: {count_player}, CPU: {count_cpu}')
if (count_player > count_cpu):
    print('лошара')
if (count_player < count_cpu):
    print(' I will be back')
if (count_player == count_cpu):
    print('a draw this time, but i will come back stronger than ever. -\(-_-)/- ')
