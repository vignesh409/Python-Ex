high = input("Enter you Height in M: ")
Wigh = input("Enter your Weight in KG: ")
bmi = int(Wigh)/float(high)**2
print(int(bmi))
if bmi>30:
  print("over weight")
if bmi<30:
  print("Below weight")
if bmi>20 and bmi>25:
  print("Normal")
  
