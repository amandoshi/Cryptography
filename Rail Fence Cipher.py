def encode_rail_fence_cipher(string, n):
    partials = [[] for _ in range(n)]
    
    count = 0
    ascending = False
    for char in string:
        partials[count].append(char)
        
        if count in [0, n-1]:
            ascending = not ascending
        
        if ascending:
            count += 1
        else:
            count -= 1
    
    return ''.join([''.join(partial) for partial in partials])
    
def decode_rail_fence_cipher(string, n):
    wavelength = n * 2 - 2
    numWaves = len(string) // wavelength
    remainder = len(string) % wavelength
    
    partials = []
    index = 0
    for i in range(1, n+1):
        if i == 1:
            num = numWaves
            if remainder:
                num += 1
        elif i == n:
            num = numWaves
            if remainder >= n:
                num += 1
        else:
            num = numWaves * 2
            if remainder >= i:
                num += 1
            if remainder >= wavelength - i + 2:
                num += 1
        partials.append(list(string[index : index + num]))
        index += num
        
    plaintext = ""
    count = 0
    ascending = False
    
    for i in range(len(string)):
        plaintext += partials[count].pop(0)
        
        if count in [0, n-1]:
            ascending = not ascending
        
        if ascending:
            count += 1
        else:
            count -= 1
    
    return plaintext

def main():
    ask = True
    while ask:
        ask = False
        inp = input("\n1. Encryption\n2. Decryption\n3. Choice\nEnter: ")

        if inp == "1":
            # get plaintext
            plaintext = input("\nPlaintext: ")
            
            # get number of rails
            enterRails = True
            while enterRails:
                enterRails = False
                rails = input("Rails: ")

                # check valid key
                try:
                    rails = int(rails)
                    if rails <= 0:
                        print("Invalid Number of Rails\n")
                        enterRails = True
                except:
                    print("Invalid Number of Rails\n")
                    enterRails = True
            
            ciphertext = encode_rail_fence_cipher(plaintext, rails)
            print(f"Ciphertext: {ciphertext}")
        elif inp == "2":
            # get ciphertext
            ciphertext = input("\nCiphertext: ")
            
            # get number of rails
            enterRails = True
            while enterRails:
                enterRails = False
                rails = input("Rails: ")

                # check valid key
                try:
                    rails = int(rails)
                    if rails <= 0:
                        print("Invalid Number of Rails\n")
                        enterRails = True
                except:
                    print("Invalid Number of Rails\n")
                    enterRails = True
            
            plaintext = decode_rail_fence_cipher(ciphertext, rails)
            print(f"Plaintext: {plaintext}")
        elif inp == "3":
            quit()
        else:
            ask = True

if __name__ == "__main__":
    main()