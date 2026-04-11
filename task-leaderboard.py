# Game: Creating Leaderboard
import random
win = 0
lose = 0
point1 = 1
point2 = 1
random_num = random.randint(20,50)
print(random_num)
while True:
    user_num = int(input("Enter your guess number: "))
    if user_num == random_num:
        win = win + 1
        print("Again, we have new number..try to guess it.")
        random_num = random.randint(20,50)
        print(random_num)
        point1 = 5 * win
        print(win, point1)
    else:
        lose = lose + 1
        print("Try again.")
        point2 = 5 * lose
        print(lose, point2)
   
    if point1 == 50 or point2 == 50:
        print(f'GAME HAS ENDED.')
        if(point1 > point2):
            print(f'The winner is you with {win} points.')
        elif (point1 == point2):
            print(f'The match is draw with {lose} points.')
        else:
            print(f'The winner is computer with {lose} points.')
        break