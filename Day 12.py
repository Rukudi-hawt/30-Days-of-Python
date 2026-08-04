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

#user_id_gen_by_user()

def rgb_color_gen():
     red = random.randint(0,255)
     green = random.randint(0,255)
     blue = random.randint(0,255)

     rgb = 'rgb('+ str(red) + ',' + str(green) + ','+ str(blue) + ')'
     return rgb

#print(rgb_color_gen())

def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return f"rgb({red}, {green}, {blue})"

#print(rgb_color_gen())

def list_of_hexa_colors(length):
     hexa_list = []
     hex_code = '#'
     character = 0

     for lst in range(1, length + 1, 1): #correlates with given amount of codes
          hex_code = '#'

          for code in range(1, 7, 1): #creates code; 7-code length
               character = random.randint(0, 1)

               if character == 0:
                    hex_code += str(random.randint(0, 9))

               if character == 1:
                    hex_code += random.choice(string.ascii_lowercase)

          hexa_list.append(hex_code)

     return hexa_list

#print(list_of_hexa_colors(19))

def list_of_rgb_colors(length):
     rgb_list = []
     rgb = ''

     for lst in range(0, length):
          rgb = ''

          red = random.randint(0, 255)
          green = random.randint(0, 255)
          blue = random.randint(0, 255)

          rgb = f"rgb({red}, {green}, {blue})"
          rgb_list.append(rgb)
     return rgb_list

#print(list_of_rgb_colors(9))

def generate_colors(type, length):
     hexa_list = []
     hex_code = '#'
     character = 0

     rgb_list = []
     rgb = ''

     colour_list = []

     if type.lower() == 'hexa':
          for lst in range(1, length + 1, 1): #correlates with given amount of codes
                    hex_code = '#'
          
                    for code in range(1, 7, 1): #creates code; 7-code length
                         character = random.randint(0, 1)
          
                         if character == 0:
                              hex_code += str(random.randint(0, 9))
          
                         if character == 1:
                              hex_code += random.choice(string.ascii_lowercase)
          
                    hexa_list.append(hex_code)
          return hexa_list


     if type.lower() == 'rgb':

          for lst in range(0, length):
                    rgb = ''
          
                    red = random.randint(0, 255)
                    green = random.randint(0, 255)
                    blue = random.randint(0, 255)
          
                    rgb = f"rgb({red}, {green}, {blue})"
                    rgb_list.append(rgb)
          return rgb_list

     # if len(rgb_list) > 0:
     #      colour_list.append(rgb_list)
     #      return rgb_list
     # else:
     #      colour_list.append(hexa_list)
     #      return hexa_list

     #return colour_list

print(generate_colors('rgb', 3))
     