# import art
#
# print(art.logo)

def encrypt():
    original_text = input("Enter code: ").lower()
    shift = int(input('Enter the shift: '))
    encrypted_text = ''

    for item in original_text:
      asci = ord(item)
      if item < 'A':
          char = chr(asci)
          encrypted_text += char
      else:
        asci = asci + shift
        if asci > ord('z') :
            asci = ord('a') + (asci - ord('z') - 1)

        char = chr(asci)
        encrypted_text += char
    print(encrypted_text)



def decrypt():
    original_text = input("Enter code: ").lower()
    shift = int(input('Enter the shift: '))
    decrypted_text = ''

    for item in original_text:
      asci = ord(item)
      if item < 'A':
          char = chr(asci)
          decrypted_text += char
      else:
        asci = asci - shift
        if asci < ord('a'):
            asci = ord('z') - ((ord('a')-asci) -1)

        char = chr(asci)
        decrypted_text += char
    print(decrypted_text)

current = True

while(current):
    Task = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if Task == 'encode':
            encrypt()
    elif Task == 'decode':
            decrypt()
    print("Type 'yes' if you want to go again. Otherwise type 'no'.")
    cur = input().lower()
    if cur == 'yes':
        current = True
    else:
        current = False
        print("Thank you for using Encrypt/Decrypt.")