import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z', 'A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
let = int(input("How many letters would you like in your password?\n"))
sym = int(input(f"How many symbols would you like?\n"))
num = int(input(f"How many numbers would you like?\n"))

print("Easy Password")
  #Eazy Level - Order not randomised:
passcode = ""
for char in range(1, let+1):
  passcode += random.choice(letters)
for char in range(1, sym+1):
  passcode += random.choice(symbols)
for int in range(1, num+1):
  passcode += random.choice(numbers)
print(f"Your password is {passcode} ")
print("\n")
print("Hard Password")
  #Hard Level - Order of characters randomised:
passcode_list = []
for char in range(1, let+1):
  passcode_list += random.choice(letters)
for int in range(1, num+1):
  passcode_list += random.choice(numbers)
for char in range(1, sym+1):
  passcode_list += random.choice(symbols)
random.shuffle(passcode_list)

password = ""
for char in passcode_list:
  password += char
print(f"Your password list is {password}")
