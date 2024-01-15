# Auto unsubscriber
# program that scans through your email account, finds all the unsubscribe links in all your emails,
# and automatically opens them in a browser.
import imapclient, pyzmail, re, bs4, webbrowser

# Login to email account and download all emails with IMAP
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
#imapObj.login('testpythonskills@gmail.com', str(input('Enter the password: ')))
imapObj.login('testpythonskills@gmail.com', 'vYWtS8KgR5kyEcE')
imapObj.select_folder('INBOX', readonly=True)
#UIDs = imapObj.search(['ALL'])
UIDs = imapObj.search(['ALL'])
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
wordCheck = ['unsubscribe', 'Unsubscribe']
unsubscibeList = []
regex = re.compile(r'.nsubscribe')
for UID in UIDs:
    message = pyzmail.PyzMessage.factory(rawMessages[UID][b'BODY[]'])

    # Use Beautiful Soup (covered in Chapter 12) to check for any instance where the word unsubscribe occurs within an HTML link tag.
    if message.html_part != None:
        html = message.html_part.get_payload().decode('utf-8')
        soupObj = bs4.BeautifulSoup(html, 'html.parser')
        elems = soupObj.select('a')
        for i in range(len(elems)):
           try:
               search_result = regex.search(str(elems[i])).group()
               unsubscibeList.append(elems[i].get('href'))
           except:
               search_result = None
               continue
imapObj.logout()
print(unsubscibeList)

# Automatically open all of the links in a browser with webbrowser.open() from the list with unsubscribe URLs
for i in range(len(unsubscibeList)):
    webbrowser.open(unsubscibeList[i])



