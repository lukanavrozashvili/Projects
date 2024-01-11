import random

def diceroll():
  #წესები
  print("#მოგესალმებით კამათელის გაგორობანაში!")
  print("#წესები შემდეგია:")
  print("#2 მოთამაშე აგორებს კამათელს - რომლის კამათელიც უფრო მეტი იქნება ის გაიმარჯვებს!")
  print("#თამაში გაჩერდება თუ ორივე მოთამაშე ამას დაეთანხმება!")
  print("#თამაში გაგრძელდება თუ ორივე მოთამაშე ამას დაეთანხმება")
  print("3...2...1..")
  
  #თამაშის სისტემა
  player_input = input("Type Roll! to roll the dice: ")
  if player_input == "Roll!":
    dice = (1, 2, 3, 4, 5, 6)
    number = random.choice(dice)
    py1_num = number
    print(number)
  else:
    print("error")

  player2_input = input("Type Roll! to roll the dice: ")
  if player_input == "Roll!":
    dice = (1, 2, 3, 4, 5, 6)
    number = random.choice(dice)
    py2_num = number
    print(number)
  else:
    print("error")

  if py1_num > py2_num:
    print("Player 1 Won!")
  else:
    print("player 2 Won!")

  play_again1 = input("Want to continue? Type Yes/No : ")
  play_again2 = input("Want to continue? Type Yes/No : ")

  if play_again1 == "No" or play_again2 == "No":
    print("Game Over!")

  elif play_again2 and play_again1 == "Yes":
    print("Starting...")
    diceroll()

diceroll()