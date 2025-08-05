import random
class Player:
    def __init__(self,name):
        self.name = name
        self.hearts = 3
number = random.randint(3,10)
input("Hi players today we wanna play hoop game for number: "+ str(number))
input_name_1 = input("Please enter the name for player one: ")
input_name_2 = input("Please enter the name for player two: ")
player_1 = Player(input_name_1)
player_2 = Player(input_name_2)
condition = False
get_first_condition = True
passing_number = 1
while get_first_condition == True:
  get_player_1 = input(player_1.name + " please type the first number")
  if int(get_player_1) == 1:
    condition = True
    next_player = player_2
    passing_number = 2
    break
  else:
    print("Ooooops! I told you that u have to start from 1")
    get_player_2 = input(player_2.name + " please type the first number")
    if int(get_player_2) == 1:
       condition = True
       next_player = player_1
       passing_number = 2
       break
def next_turn(player):
   if player == player_1
     return player_2
   if player == player_2
     return player_1
   
while condition == True:
  get_player = input("Perfect! "+next_player.name+" please enter the next number")
  if (passing_number % number == 0) :
     if (get_player) != 'Hooop':
        passing_number += 1
#This is a new version
# A FILE CONDITION 

  


