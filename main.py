import random

def game():
  def guess(random):
    guess_input = int(input("Please guess a possitive integer between 0 and " + str(max) + ": ")) 
    if guess_input > random:
      print("Your guess is high")
      guess(random)
    elif guess_input < random:
      print("Your guess is low")
      guess(random)
    else:
      print("You are correct! " + str(random) + " is the random number")
      restart = input("Would you like to play again?(Please enter Yes or No): ")
      if restart == "Yes":
        game()
  
  max = int(input("Pick a possitive integer: "))
  guess(random.randint(0, max))

game()