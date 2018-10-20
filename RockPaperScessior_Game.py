'''Rules: You and the computer both choose rock, paper or scissors. The winner is decided by these rules:
Rock blunts scissors
Paper covers rock
Scissors cut paper
'''

from random import randint

player = input("rock (r), paper (p), scissor (s)?")
print(player, "vs",end=' ')

chosen = randint(1, 3)

if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer = 's'

print(computer)

if player == computer:
    print("It's a Draw")

elif (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
    print("You won!")
else:
    print("You lost!")
