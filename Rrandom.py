import random
secret_number = random.randint(0,100)
print(secret_number)

print("\nRandom Number Game\n")
print("\nenter 'exit' to quit\n")

guessed = 0

while True:
   pick_num = input("\nguess a number from zero to hundred\n")
   if pick_num == "exit":
      break
   
   
   
   try:
      a = int(pick_num)
      guessed += 1
   except ValueError:
      print("please enter a valid number")
      continue
   
 
   if a > 100:
      print("more than what I can contain")
      continue

   elif a < 0:
      print("less than what I can contain")
      continue

   difference = abs(a-secret_number)

   if difference == 0:
      print(f"you guessed it, the answer is {secret_number}")
      print(f"you guessed it in the {guessed}th tries")
      break
  
   elif difference <= 5:
      print("move on a bit👌closer")

   elif difference >= 50:
      print("we need an advanced GPS to find you😂")


   elif difference >=20:
      print("where are you🧐")

   elif difference >=10:
      print("one more step and you will be 10 steps ahead of the game🤔")

   elif difference >=6:
      print("jumped on it a bit👌")
  

   else:
      print("on a new planet👽")
   
   
      

  



  