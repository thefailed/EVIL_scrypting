# -*- coding: utf-8 -*-
import sys
import time
from random import randrange

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
   
class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'
    
def talking():
    irand = randrange(10, 500)
    num1 = '{}'.format(irand)
    num2 = '{}'.format(irand)
    num3 = '{}'.format(irand)
    num4 = '{}'.format(irand)
    num5 = '{}'.format(irand)
    write = 'abcdefghijklmnopqrstuvwxyz0123456789'
    numlist = [num1, num2, num3, num4, num5] 
    newMessage = ''

    message = raw_input('\033[1mPlease Enter Message For Encryption: ')
    blah = """Encryption ..."""
    for l in blah:
      sys.stdout.write(l)
      sys.stdout.flush()
      time.sleep(0.000001)
    for text in message:
      if text in write:   
        position = write.find(text)
        newposition = (position + int(num1) + int(num2) - int(num3) + int(num4) - int(num5)) % 36
        newtext = write[newposition]
        newMessage += newtext
      else:
        newMessage += text
        
    print ("\033[91mYour New Message Is \033[0m===> " + newMessage)

    write = 'abcdefghijklmnopqrstuvwxyz0123456789'
    numlist = [num1, num2, num3, num4, num5] 
    newMessage = ''

    message = raw_input('\033[1mPlease Enter Message For Decryption: ')

    for text in message:
      if text in write:   
        position = write.find(text)
        newposition = (position - int(num1) - int(num2) + int(num3) - int(num4) + int(num5)) % 36
        newtext = write[newposition]
        newMessage += newtext
      else:
        newMessage += text
        
    print("\033[91mYour New Message Is \033[0m===> " + newMessage)  
    talking()
    
if __name__ == "__main__":
        talking()
