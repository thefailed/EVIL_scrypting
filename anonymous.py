# -*- coding: utf-8 -*-
import sys
import time
from random import randrange
import string
from random import *

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'
    
blah = """
──────────────── ────██
────────────────────█─░█
────────────────────█───█
────────────────────█───█
────────────────────█───█
────────────────────█───█
────────────────────█───█▓
────────────────────█───▓█
────────────────────█───░█
────────────────────█───░█
────────────────────█░░░─█
─────────────▓███──██▓▓███
─────────────██──▓██▓────██
─────────────█▓────█▓─────▓█
─────────────█▓─────█──────░█
████████─────█▓─────█────────█
██████████▓███░──────█──█▓────█
██░░░░░░██───────────█░███────█▓
▓████████─────────────█▓██────██
█████████░────────────────────▓█
▓████████░────────────────────░█
▓████████░────────────────────▓█
▓████████░────────────────────█▓
▓████████░────────────────────█
▓████████░───────────────────██
▓█████░██░──────────────────█
▓█████──████████████████████
█████████
"""

for l in blah:
   sys.stdout.write(l)
   sys.stdout.flush()
   time.sleep(0.0000000001)
   
def talking():

    irand = randrange(10, 500)
    num1 = '{}'.format(irand)
    num2 = '{}'.format(irand)
    num3 = '{}'.format(irand)
    num4 = '{}'.format(irand)
    num5 = '{}'.format(irand)
    write = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numlist = [num1, num2, num3, num4, num5] 
    newMessage = ''

    message = raw_input('\033[1mPlease Enter Message For Ecryption : ')
    blah = """\033[92mEncryption \033[91m...\n\n"""
    for l in blah:
      sys.stdout.write(l)
      sys.stdout.flush()
      time.sleep(0.00001)
      
    for text in message:
      if text in write:   
        position = write.find(text)
        newposition = (position + int(num1) + int(num2) - int(num3) + int(num4) - int(num5)) % 62
        newtext = write[newposition]
        newMessage += newtext
        time.sleep(0.01)
      else:
        newMessage += text
        time.sleep(0.01)
        
    min_char = 20
    max_char = 60
    allchar = string.ascii_letters + string.digits
    password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))

    mix = '{}'.format(password)
    s = "{}".format(newMessage).replace(' ', mix)
    print ("\033[91mYour New Message Is \033[0m===> " + s)



    message = raw_input('\033[1mPlease Enter Message For Decryption: ')
     
    change = '{}'.format(message)
    s = "{}".format(change).replace(mix, ' ')


    write = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numlist = [num1, num2, num3, num4, num5] 
    newMessage = ''

    message = '{}'.format(s)

    for text in message:
      if text in write:   
        position = write.find(text)
        newposition = (position - int(num1) - int(num2) + int(num3) - int(num4) + int(num5)) % 62
        newtext = write[newposition]
        newMessage += newtext
      else:
        newMessage += text
    
    print ("\033[91mYour New Message Is \033[0m===> " + newMessage)
    talking()
 
if __name__ == "__main__":
        talking()

    
