import smtplib  # Import statement for actual sending function
from Crypto.Cipher import DES  # Import statement for DES Encryption

def prompt(prompt):
    """Returns the input of the prompt."""
    return input(prompt).strip()
# The inputs for all the necessary email parts
fromAddr = prompt("From: ")
toAddrs = prompt("To: ").split()
ccAddr = prompt("CC: ").split()
subject = prompt("Subject: ")
message = prompt("Enter message: ")
login = prompt("Login Username: ")
password = prompt("Password: ")


def sendemail(from_addr, to_addrs, cc_addr, subject, msg, log_in, pass_word, smtpserver='smtp.gmail.com:465'):
    """Sends the email with all the correct configurations"""
    # Creates the headers for sending out the email
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addrs)
    header += 'Cc: %s\n' % ','.join(cc_addr)
    header += 'Subject: %s\n\n' % subject
    msg = header + msg

    # Creates the server specifications
    server_ssl = smtplib.SMTP_SSL(smtpserver)
    server_ssl.ehlo()
    server_ssl.login(log_in,pass_word)
    problems = server_ssl.sendmail(from_addr, to_addrs, msg)
    server_ssl.quit()
    # Returns any recorded problems with the system
    return problems

def des_encrypt(message):
    """Encrypts the email message with DES"""
    # Variable for the edited version of the message (removes spaces)
    message_edit = ""
    # The initial index for the message segment
    m = 0
    # Loops through the message and deletes teh spaces
    for i in range(0, len(message)):
        # Checks if the character in the message is a space
        if message[i].isspace():
            # Creates a new segment of the edited message
            # Increments the starting index of the message segment
            message_edit = message_edit + message[m:i]
            m = i+1
        # Sets the message_edit equal to the message if the
        # if the original message has no spaces
        elif i == len(message)-1 and message_edit == "":
            message_edit = message

    # Adds filler characters if the message is not
    # a multiple of 8
    while len(message) % 8 != 0:
        message = message + "&"

    # Prints the edited message
    print("Formatted message: "+message_edit)
    # Creates a new DES object with the given key
    obj = DES.new("alphabet")
    # Assigns created cipher to the variable
    cypher = obj.encrypt(message)
    # Returns the new cipher
    return cypher
# Assigns the created cipher to the variable
cypher = des_encrypt(message)
# This prints the newly created cipher
print("Ciphertext: "+cypher)
# Converts the cypher to a string for transportation
cypher = str(cypher)
# Sends out the email with the cipher
sendemail(fromAddr, toAddrs, ccAddr, subject, cypher, login, password)