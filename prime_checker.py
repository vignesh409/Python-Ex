#Write your code below this line ๐
def prime_checker(number):
  is_prime=True
  for i in range(2,number):
    if number%1==0:
      is_prime=False
  if is_prime:
      print("it is Prime Number")
  else:
      print("it is Not a prime")



#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
