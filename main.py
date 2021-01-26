#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
print(logo)

def easy_hard():
  eorh = input("Do you want easy or hard mode? (easy/hard)").lower()
  if eorh == "easy":
    tries = 10
  elif eorh == "hard":
    tries = 5
  print(f"You have {tries} attempts")
  return tries

def play_game():
  number_picked = random.randint(1,101)
  print(number_picked)
  tries1 = easy_hard()

  while tries1 > 0:
    print(f"tries1 {tries1}")
    print(type(tries1))
    choose_num = int(input("please choose a number in between 1 to 100:  "))
    if number_picked == choose_num:
      print(f"Yasss qween you win")
      tries1 = 0
    else:
      print("Choose another number")
      tries1 = tries1 - 1

      print(tries1)
      if(tries1 == 0):
        print("you lost lol")




play_game()
