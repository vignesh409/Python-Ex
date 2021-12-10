import random
user_choice=int(input("What is Your choice?Type  for Rock,Type 1 for Paper,Type 2 for scisscors"))
print(f"Your choice is {user_choice}")
computer_choice = random.randint(0,2)
print(f"Computer Choice is {computer_choice}")

if user_choice>3:
  print("Your Number is Wrong,Computer Wins")
elif user_choice==0 and computer_choice==2:
  print("You Win")
elif user_choice>computer_choice:
  print("You win")
elif computer_choice>user_choice:
  print("Computer win")
elif computer_choice==user_choice:
  print("It`s Draw Match")
else:
  print("Program Overlapping")
