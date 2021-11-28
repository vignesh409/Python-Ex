print("Welcome to the Tip Calculator!!")
bill=float(input("What is the bill amount? $ "))
tip=int(input("How much you want to give? 10 or 12 or 15? "))
bill_tip = tip/100*bill+bill
total=bill_tip
people = int(input("how many peoples want to share? "))
result=float(bill_tip/people)
print("Bill amount is: "+str(bill))
print("bill Amount include Tip is : "+str(total))
print("Each person owes: "+str(result))
