def encrypt():
    plaintext = input("\nPlaintext: ")

    ciphertext = ""
    for char in plaintext:
        code = ord(char)
        offset = None

        # evaluate offset
        if 97 <= code <= 122:
            offset = 97
        elif 65 <= code <= 90:    
            offset = 65
        
        if offset:
            newCode = 25 - code + 2 * offset
            ciphertext += chr(newCode)
        else:
            ciphertext += char

    print(f"Ciphertext: {ciphertext}")      

def decrypt():
    ciphertext = input("\nCiphertext: ")

    plaintext = ""
    for char in ciphertext:
        code = ord(char)
        offset = None

        # evaluate offset
        if 97 <= code <= 122:
            offset = 97
        elif 65 <= code <= 90:    
            offset = 65
        
        if offset:
            newCode = 25 - code + 2 * offset
            plaintext += chr(newCode)
        else:
            plaintext += char

    print(f"Plaintext: {plaintext}")   

def main():
    ask = True
    while ask:
        ask = False
        inp = input("\n1. Encryption\n2. Decryption\n3. Choice\nEnter: ")

        if inp == "1":
            encrypt()
        elif inp == "2":
            decrypt()
        elif inp == "3":
            quit()
        else:
            ask = True

if __name__ == "__main__":
    main()
