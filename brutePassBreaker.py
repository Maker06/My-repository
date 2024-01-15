"""Brute-Force PDF Password Breaker"""
import PyPDF2, re

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
#logging.disable(logging.CRITICAL)

# Open dictionary
dictionary = open('dictionary_1.txt').readlines()

# Search and remove \n from the list at the end of the word
regex = re.compile(r'(.*)\n')
i = 0
words = []
for i in range(len(dictionary)):
    if regex.search(dictionary[i]) is not None:
        words.append(regex.search(dictionary[i]).group(1))

# Open encrypted PDF file
pdffileName = 'C:\\Users\\mak_e\\OneDrive\\Documents\\learning\\AutomateBoringStuff\\encrypted.pdf'
pdfFile = open(pdffileName, 'rb')
pdfReader = PyPDF2.PdfReader(pdfFile)

# Looping through dictionary to find the password

j = 0
for j in range(len(words)):
    password = words[j]
    logging.debug('password: ' + str(password))
    passwordUp = password.upper()
    #logging.debug('passwordUP: ' + str(passwordUp))
    passwordLow = password.lower()
    #logging.debug('passwordLow: ' + str(passwordLow))

    if pdfReader.decrypt(passwordUp) == 1:
        #print('Not this one')
        print('Hacked password is: ', passwordUp)
        break
    elif pdfReader.decrypt(passwordLow) == 1:
        #print('Or this one')
        print('Hacked password is: ', passwordLow)
        break
    else:
        continue




