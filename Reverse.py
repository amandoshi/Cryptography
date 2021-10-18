def encrypt():
    plaintext = input("\nPlaintext: ")
    ciphertext = plaintext[::-1]

    print(f"Ciphertext: {ciphertext}")

def decrypt():
    ciphertext = input("\nCiphertext: ")
    plaintext = ciphertext[::-1]

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
