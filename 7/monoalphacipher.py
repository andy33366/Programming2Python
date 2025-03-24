

def main():

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = input("Enter the text to encrypt:  ")
    key = int(input("Enter the key: "))
    ciphertext = []
    
    for letter in plaintext:
        cipherletterindex = alphabet.index(letter) + key
        ciphertext.append(alphabet[cipherletterindex])
    
    print(f"{"".join(ciphertext)} is the ciphertext")

    #decipher
    plaintext = []
    for letter in ciphertext:
        plaintextletterindex = alphabet.index(letter) - key
        plaintext.append(alphabet[plaintextletterindex])

    print(f"{"".join(plaintext)} is the plaintext")


main()
