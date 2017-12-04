from Crypto.Cipher import DES  # Imports DES for decryption
import bcrypt  # Imports the module used for hashing passwords
# Sets the username to nothing
username = ''
# Tries the code
try:
    # Opens the username and password files for reading
    fileu = open("dec_username.txt", 'r')
    filep = open("dec_password.txt", 'r')
    # Reads in the username and password hash
    username = fileu.read()
    hashed = eval(filep.read())
    # Closes both files
    fileu.close()
    filep.close()
    # Receives the input of a password and encodes it into a byte string
    password = input("Please enter in existing password: ").encode('utf-8')
    # Sets the loop condition for number of times
    num = 0
    # While the password hash of the entered password does not equal
    # the existing password hash and the number of times tried is not 5
    while bcrypt.hashpw(password, hashed) != hashed and num < 5:
        # Receive password input after failed try
        password = input("Incorrect password. Please try again: ")
        num = num+1
    # If the number of times has reached 5, print the
    # limit statement
    if num == 5:
        print("Sorry, you have surpassed the limit.")
    # Prints the success statement
    else:
        print("You are now logged in.")

# If the file is not found
except FileNotFoundError:
    # Automatically creates a username
    username = "exists"
    # Opens the username and password files for write mode
    fileu = open("dec_username.txt", 'w')
    filep = open("dec_password.txt", 'w')
    # Writes username to file and closes the file
    fileu.write(username)
    fileu.close()
    # Accepts the input of a new password encoded the byte string
    pword = input("Please enter a new password: ").encode('utf-8')
    # Assigns the password hash to the variable with salt
    hashed = bcrypt.hashpw(pword, bcrypt.gensalt())
    # Writes string version to password file
    filep.write(str(hashed))
    # Closes file
    filep.close()
    # Prints the success statement
    print("You are now logged in.")
# Receives the cipher text from user input
text = eval(input("Please enter in the encrypted DES message: "))

def decrypt_message(cipher_text):
    """Decrypts the DES cipher text"""
    # Creates the DES object
    obj = DES.new("alphabet")
    # Prints the cipher text out
    print("Ciphertext: "+cipher_text)
    # Assigns the plain text to the variable
    plaintext = obj.decrypt(cipher_text)
    # Prints out the plain text
    print("Plaintext: "+plaintext)

decrypt_message(text)
