print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_string=name1+name2
lower_case=combine_string.lower()

t=lower_case.count('t')
r=lower_case.count('r')
u=lower_case.count('u')
e=lower_case.count('e')
true=t+r+u+e
l=lower_case.count('l')
o=lower_case.count('o')
v=lower_case.count('v')
e=lower_case.count('e')#t=lower_case.count('t')
love=l+o+v+e

#score=str(true)+str(love)
score=int(str(true)+str(love))
#print(score)
if score<10 or score>90:
  print(f"Your love score is {score}, you go ")
elif score>=40 and score<=50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
