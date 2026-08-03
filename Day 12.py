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

print(random_user_id())