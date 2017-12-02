import smtplib # Import statement for actual sending function
from Crypto.Cipher import DES
def prompt(prompt):
    return input(prompt).strip()

fromAddr = prompt("From: ")
toAddrs = prompt("To: ").split()
ccAddr = prompt("CC: ").split()
subject = prompt("Subject: ")
message = prompt("Enter message: ")
login = prompt("Login Username: ")
password = prompt("Password: ")

# print("Enter message, end with ^D (Unix) or ^Z (Windows):")


def sendemail(from_addr, to_addrs, cc_addr, subject, msg, log_in, pass_word, smtpserver='smtp.gmail.com:465'):
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addrs)
    header += 'Cc: %s\n' % ','.join(cc_addr)
    header += 'Subject: %s\n\n' % subject
    msg = header + msg

    server_ssl = smtplib.SMTP_SSL(smtpserver)
    server_ssl.ehlo()
    server_ssl.login(log_in,pass_word)
    problems = server_ssl.sendmail(from_addr, to_addrs, msg)
    server_ssl.quit()
    return problems
def des_encrypt(message):
    message_edit = ""
    m = 0
    for i in range(0, len(message)):

        if message[i].isspace():
            message_edit = message_edit + message[m:i]
            m = i+1
        elif i == len(message)-1 and message_edit == "":
            message_edit = message


    while len(message) % 8 != 0:
        message = message + "&"

    print(message_edit)
    obj = DES.new("alphabet")
    cypher = obj.encrypt(message)

    return cypher
cypher = des_encrypt(message)
print(cypher)
cypher = str(cypher)

sendemail(fromAddr, toAddrs, ccAddr, subject, cypher, login, password)