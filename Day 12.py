# import math
# dir(math) 
# help(math)

import random 
import string

def random_user_id():
     user_id = ''
     user_id += str(random.randint(0, 9))
     user_id += random.choice(string.ascii_lowercase)
     user_id += random.choice(string.ascii_lowercase)
     user_id += str(random.randint(0, 9))
     user_id += str(random.randint(0, 9))
     user_id += random.choice(string.ascii_lowercase)

     return user_id

#print(random_user_id())

def user_id_gen_by_user():
     length = int(input('Number of charaacters:', ))
     tally = int(input('Number of codes:', ))
     #codes = []
     character = 0
     code = ''

     for number_of_codes in range(1, tally + 1, 1):
          code = ''

          for number_of_characters in range(1, length + 1, 1):
               character = random.randint(0,1)

               if character == 0:
                    code += str(random.randint(0,9))

               if character == 1:
                    code += random.choice(string.ascii_letters)

          #codes.append(code)
          print(code)
     #return codes

user_id_gen_by_user()

