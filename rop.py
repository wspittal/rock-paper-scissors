while True:
  
  print "Let's play rock paper scissors!"
  import random
  rps= ["Rock", "Paper", "Scissors"]
  computer = (random.choice(rps))
  
  player = False
  while player == False:
      player = input("Rock, Paper, Scissors, Gun?")
      if player == computer:
          print("I play ") + (player) + ("! We tie!")
      elif player == "Rock":
          if computer == "Paper":
              print("I play Paper! You lose!")
          else:
              print("I play Scissors! You win!")
      elif player == "Paper":
          if computer == "Scissors":
              print("I play Scissors! You lose!")
          else:
              print("I play Rock! You win!")
      elif player == "Scissors":
          if computer == "Rock":
              print("I play Rock! You lose...")
          else:
              print("I play Paper! You win!")
      elif player == "Gun":
         print ("You don't deserve to play rock paper scissors")
         break
      else:
          print("That's not an option, make sure you spelled your input correctly and capatilized it")
  c = input("Press R to restart or another key to end")
  if c == "R" or "r":
    continue    
  print("Bye Then!")
  break
