from Crypto.Cipher import DES
e_or_d = 'r'
while e_or_d != 'q':
    print("Please type in any letter to continue. Press 'q' if")
    e_or_d = input()
    try_again = True
    message = input()

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
    decrypt_message = cypher
    print(cypher)
    print("Would you like to decrypt (press 'd')?")
    if input() == 'd':
        obj1 = DES.new("alphabet")
        print(decrypt_message)
        plaintext = obj1.decrypt(decrypt_message)
        print(plaintext)
        print("Would you like to run this program again?")
        e_or_d = input()



