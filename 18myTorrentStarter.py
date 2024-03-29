# Controlling Your Computer Through Email
# program that checks an email account every 15 minutes for any instructions you email it and executes those
# instructions automatically

# Check email every 15 mins for torrents to start loading
import smtplib, imapclient, pyzmail, logging, traceback, time, subprocess
logging.basicConfig(filename='torrentStarterLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Configure the program by setting some variables.
MY_EMAIL = 'mike.maksymiuk@gmail.com' # bot should only respond to me
BOT_EMAIL = 'testpythonskills@gmail.com'
BOT_EMAIL_PASSWORD = 'vYWtS8KgR5kyEcE'
IMAP_SERVER = 'imap.gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
TORRENT_PROGRAM = 'C:\\Users\\Mykhailo Maksymiuk\\AppData\\Roaming\\uTorrent\\utorrent.exe'

assert BOT_EMAIL != MY_EMAIL, "Give the bot it's own email address."


def getInstructionEmails():
    # Log in to the email imapCli.
    logging.debug('Connecting to IMAP server at %s...' % (IMAP_SERVER))
    imapCli = imapclient.IMAPClient(IMAP_SERVER, ssl=True)
    imapCli.login(BOT_EMAIL, BOT_EMAIL_PASSWORD)
    imapCli.select_folder('INBOX')
    logging.debug('Connected.')

    # Fetch all instruction emails.
    instructions = []
    UIDs = imapCli.search(['FROM', MY_EMAIL])
    rawMessages = imapCli.fetch(UIDs, ['BODY[]'])
    for UID in rawMessages.keys():
        # Parse the raw email message.
        message = pyzmail.PyzMessage.factory(rawMessages[UID][b'BODY[]'])
        if message.html_part != None:
            body = message.html_part.get_payload().decode(message.html_part.charset)
        if message.text_part != None:
            # If there's both an html and text part, use the text part.
            body = message.text_part.get_payload().decode(message.text_part.charset)

        # Extract instruction from email body.
        instructions.append(body)

    # Delete the instruction emails, if there are any.
    if len(UIDs) > 0:
        imapCli.delete_messages(UIDs)
        imapCli.expunge()

    imapCli.logout()

    return instructions


def parseInstructionEmail(instruction):
    # Send an email response about the task.
    responseBody = 'Subject: Instruction completed.\nInstruction received and completed.\nResponse:\n'

    # Parse the email body to figure out the instruction.
    lines = instruction.split('\n')
    for line in lines:
        if line.startswith('magnet:?'):
            subprocess.Popen(TORRENT_PROGRAM + ' ' + line) # launch the bittorrent program
            responseBody += 'Downloading the torrent.\n'

    # Email the response body to confirm the bot carried out this instruction.
    logging.debug('Connecting to SMTP server at %s to send confirmation email...' % (SMTP_SERVER))
    #smtpCli = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)     # uncomment one or the other as needed.
    smtpCli = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) # uncomment one or the other as needed.
    smtpCli.ehlo()
    #smtpCli.starttls() # comment this out if using SMTP_SSL
    smtpCli.login(BOT_EMAIL, BOT_EMAIL_PASSWORD)
    logging.debug('Connected.')
    smtpCli.sendmail(BOT_EMAIL, MY_EMAIL, responseBody)
    logging.debug('Confirmation email sent.')
    smtpCli.quit()

logging.debug('Getting instructions from email...')
instructions = getInstructionEmails()
print(instructions)
for instruction in instructions:
    logging.debug('Doing instruction: ' + instruction)
    parseInstructionEmail(instruction)



# Start an infinite loop that checks email and carries out instructions.
'''print('Email bot started. Press Ctrl-C to quit.')
logging.debug('Email bot started.')
while True:
    try:
        logging.debug('Getting instructions from email...')
        instructions = getInstructionEmails()
        for instruction in instructions:
            logging.debug('Doing instruction: ' + instruction)
            parseInstructionEmail(instruction)
    except Exception as err:
        logging.error(traceback.format_exc())

    # Wait 15 minutes before checking again
    logging.debug('Done processing instructions. Pausing for 15 minutes.')
    time.sleep(60 * 15)'''


