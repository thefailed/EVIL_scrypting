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
        
"""

for l in blah:
   sys.stdout.write(l)
   sys.stdout.flush()
   time.sleep(0.0001000)
   
def talking():
 ### change encreption
    
    first = randrange(10, 500)
    second = randrange(20, 500)
    third = randrange(10, 600)
    four = randrange(10, 500)
    five = randrange(10, 500)
    
    num1 = '{}'.format(first)
    num2 = '{}'.format(second)
    num3 = '{}'.format(third)
    num4 = '{}'.format(four)
    num5 = '{}'.format(five)
###------------------------------------------------------------------------------###

##show codes (use for one encryption)
    
    #print ('\033[93m----------------------')    
    #print ("\033[91mFirst code\033[92m: " + num1)
    #print ('\033[93m----------------------')
    #print ("\033[91msecond code\033[92m: " + num2)
    #print ('\033[93m----------------------')
    #print ('\033[91mthird code\033[92m: ' + num3)
    #print ('\033[93m----------------------')
    #print ('\033[91mfour code\033[92m: ' + num4)
    #print ('\033[93m----------------------')
    #print ('\033[91mfive code\033[92m: ' + num5)
    #print (\033[93m'----------------------\n')
    
###------------------------------------------------------------------------------###


###------------------------------------------------------------------------------###
    
###  for keep you encryption steel one
    
##    num1 = 192
##    num2 = 312
##    num3 = 314  
##    num4 = 113
##    num5 = 216
    
###------------------------------------------------------------------------------###
    numlist = [num1, num2, num3, num4, num5]
    newMessage = ''
    write = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
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
        
   ## change encreption
        
    min_char = 20
    max_char = 60
    allchar = string.ascii_letters + string.digits
    password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    mix = '{}'.format(password)
    change = '{}'.format(mix)
    s = "{}".format(newMessage).replace(' ', mix)
    time.sleep(0.1)
    print ("\033[91mYour New Message Is \033[0m===> " + s)
    
###---------------------------------------------------------------------------------###

   ### stay one encryption

##    encr = 'fjjhkfdl1fgh1fg5d1fgf1f5fd1dfg'
##    mix = '{}'.format(encr)
##    s = "{}".format(newMessage).replace(' ', mix)
##    print ("\033[91mYour New Message Is \033[0m===> " + s)

###----------------------------------------------------------------------------------###     
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

    
