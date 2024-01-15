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
decrypting = 0
while decrypting == 0:
    j = 0
    for j in range(len(words)):
        password = words[j]
        logging.debug('password: ' + str(password))
        passwordUp = password.upper()
        # logging.debug('passwordUP: ' + str(passwordUp))
        passwordLow = password.lower()
        # logging.debug('passwordLow: ' + str(passwordLow))

        decrypt1 = pdfReader.decrypt(passwordUp)
        decrypt2 = pdfReader.decrypt(passwordLow)
        if decrypt1 == 1:
            decrypting = decrypt1
            theWord = passwordUp

        elif decrypt2 == 1:
            decrypting = decrypt2
            theWord = passwordLow

else:
    print('Hacked password is: ', theWord)





