from Crypto.Cipher import DES
text = eval(input())

def decrypt_message(cipher_text):
    obj = DES.new("alphabet")
    print(cipher_text)
    plaintext = obj.decrypt(cipher_text)
    print(plaintext)

decrypt_message(text)
