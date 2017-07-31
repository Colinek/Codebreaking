## Encryption/Decryption

choice=True
while choice:
    print("""
    1.Encrypt
    2.Decrypt
    3.Exit/Quit
    """)
    choice=int(input("What would you like to do? "))

    if choice==1:     ## Encrypt a word/phrase
        print("Encryption")
        
        orig = input("Please enter your text (lower case only): ")
        shift = input("How many digits to shift? ")
        encrypt = ""
        for c in orig:
            if c >= 'a' and c <= 'z':
                encrypt += chr(((ord(c) + int(shift)) - ord('a')) % 26 + ord('a')) 
            else:
                encrypt += c
        print(encrypt)        

    elif choice==2:     ## Decrypt a word/phrase
        print("Decryption")
        orig = input("Please enter your text (lower case only): ")
        shift = input("How many digits to shift? ")
        decrypt = ""
        for c in orig:
            if c >= 'a' and c <= 'z':
                decrypt += chr(((ord(c) - int(shift)) - ord('a')) % 26 + ord('a')) 
            else:
                decrypt += c
        print(decrypt)

    elif choice==3:
        print("\n Goodbye") 
        choice = None
    else:
        print("\n Not Valid Choice Try again")
