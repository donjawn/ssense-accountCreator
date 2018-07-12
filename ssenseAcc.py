## ssense account creator by @donjawn(s)

import requests
from random import getrandbits
import time
from datetime import datetime

datetime.now().strftime('%H:%M:%S') # time

url = 'https://www.ssense.com/en-us/account/register'
text_file = open("Accounts.txt", "w")

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
           }

print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
print datetime.now().strftime('%H:%M:%S | ') + 'Ssense Account Creator by @donjawn(s)'
print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
print

accountLimit = int(raw_input('How many account would you like to create? Note: please enter an integer.\n'))

i = 0
def acc_Creator():
	while i <= accountLimit-1:
		num = getrandbits(99) # edit integer value as you please
		global email
		email = 'your_email+{}@gmail.com'.format(num) # CHANGE YOUR_EMAIL to your email prefix for a *GMAIL* account. don't change the +{} after.
		global password
		password = 'yourpass123' #change to the password of your choice for all accounts
		payload = {
		'email': email,
		'password': password,
		'confirmpassword': password,
		'gender': 'no-thanks', # use 'no-thanks' to opt out of emails or 'Men' to sign up for Men news
		'source': 'SSENSE_EN_SIGNUP' # don't change
		}
		resp = requests.post(url, data=payload, headers=headers)
		print datetime.now().strftime('%H:%M:%S | ') + '{}/{} accounts created.'.format(i+1, accountLimit)
		write()


		global i
		i = i + 1
		



def write():
        userLogin = email + ":" + password
        text_file.write(userLogin + "\n")


# main code below

print
userAnswer = raw_input(datetime.now().strftime('%H:%M:%S | ') + 'Are you ready to create ' + str(accountLimit) + ' Ssense accounts? (y/n): ').lower()
if userAnswer == 'y':
    acc_Creator()
    text_file.close()
else:
    print "Come back when you're ready!"


