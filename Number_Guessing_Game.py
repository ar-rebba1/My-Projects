import random

print("Give me two different numbers and guess the number that I have chosen. It will be between them.")
while True:
  first_num = input("Enter a number: ").strip()
  if first_num.isdigit():
    first_num = int(first_num)
    break
  else:
    continue
while True:
  second_num = input("Enter another number: ").strip()
  if second_num.isdigit():
    second_num = int(second_num)
    break
  else:
    continue
#print(type(first_num))
#print(type(second_num))
lower_bound = 0
upper_bound = 0

if first_num == second_num:
  while True:
    first_num = input("Enter a number: ").strip()
    second_num = input("Enter another number: ").strip()
    if first_num.isdigit() and second_num.isdigit() and first_num == second_num:
      first_num = int(first_num)
      break
    else:
      continue
else:
  lower_bound = min(first_num,second_num)
  upper_bound = max(first_num,second_num)
center = (lower_bound + upper_bound)//2
random_number = random.randrange(lower_bound,upper_bound)
random_number = int(random_number)
print("A number has been chosen.")
current_distance = upper_bound - lower_bound
while True:
  guess = input("Enter your guess: ").strip()
  guess = int(guess)
  if guess == random_number:
    print("Your guess was correct. Well done.")
    break
  elif guess < lower_bound or guess > upper_bound:
    print("Number out of bounds")
    continue
  else:
    if abs(guess - random_number) < current_distance:
      print("Warmer")
    elif abs(guess - random_number) > current_distance:
      print("Colder")
    current_distance = abs(guess - random_number)
    continue
    
print("Thank you for playing")



  

