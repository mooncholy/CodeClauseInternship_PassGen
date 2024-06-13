"""
# User specifications
1. password length
2. number inclusion (range/specific numbers)
3. letters inclusion (range/specific letters)
4. symbol inclusion (all/specific symbols)
5. lowercase inclusion
6. uppercase inclusion
"""

## Importing libraries
import string
import random
import re
from difflib import SequenceMatcher

## Class for user defined password specs
class password_specs:
  def __init__(self, length, num_count, char_count, sym_count, letter_case = None):
    self.length = length
    self.num_count = num_count
    self.char_count = char_count
    self.sym_count = sym_count
    self.letter_case = letter_case

## Password generation function
### Wrong input handling
def misinput_handling(self):
  if self.length < self.num_count + self.char_count + self.sym_count:
    print("Total element count can't exceed password length")
    return 0
  elif self.length > self.num_count + self.char_count + self.sym_count:
    if (input("Total element count is less than required length.\nDo you want to repeat characters? ").strip().lower() == "yes"):
      return 1
    else:
      print("Make sure the total number of each element adds up to whole password length")
      return 0
  else:
    return 1

### Generation function
# basic data used for generation
alpha_lower = list(string.ascii_letters.lower())
alpha_upper = list(string.ascii_letters.upper())
numbers = list(string.digits)
symbols = list("!@#$%^&*()")

expected_params = ['length', 'num_count', 'sym_count', 'char_count', 'letter_case']

def gen_pass(self):
  password = []
  if misinput_handling(self):
    ratioUpper = SequenceMatcher(None,self.letter_case,"uppercase").ratio()
    ratioLower = SequenceMatcher(None,self.letter_case,"lowercase").ratio()
    if ratioLower > 0.6:
      password = [random.choice(numbers) for _ in range(self.num_count)] + [random.choice(alpha_lower) for _ in range(self.char_count)] + [random.choice(symbols) for _ in range(self.sym_count)]
    elif ratioUpper > 0.6:
      password = [random.choice(numbers) for _ in range(self.num_count)] + [random.choice(alpha_upper) for _ in range(self.char_count)] + [random.choice(symbols) for _ in range(self.sym_count)]
    else:
      password = [random.choice(numbers) for _ in range(self.num_count)] + [random.choice(alpha_lower + alpha_upper) for _ in range(self.char_count)] + [random.choice(symbols) for _ in range(self.sym_count)]
    if len(password) < self.length:
      for i in range(self.length - len(password)):
        password.append(random.choice(password[:self.num_count+self.char_count+self.sym_count]))
    random.shuffle(password)
    print(f"Your generated password is: {''.join(password)}")

## User input
contd = "yes"
while(contd == "yes" or contd == "y"):
  usr_specs = input("Enter your desired specs in the following order:\npassword length, digits count, letters count, symbols count\n")
  usr_specs = re.sub(r"\s+", " ", re.sub(r",\s*", " ", usr_specs)).strip().split(" ")
  try:
    usr_specs = list(map(int, usr_specs))
    try:
      if usr_specs[2] > 0:
        usr_specs.append(input("Do you want to include lowercase, uppercase, or both?\n").strip().lower())
    except IndexError:
      print("Too few arguments. Make sure to enter all required fields.")
    try:
      password = password_specs(*usr_specs)
      #print(f"vars(password) = {vars(password)}")
      gen_pass(password)
    except TypeError:
      print(f"Incorrect number of arguments. Expected number of inputs = {len(expected_params)} but {len(usr_specs)} were given.")
  except ValueError:
    print("Invalid input. Make sure all inputs are digits")
  contd = input("\nDo you want to generate a new password?\n").lower().strip()