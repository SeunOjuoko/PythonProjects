alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt or type 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))


#Create a function 'encrypt()' takes the original_text and shift the amount
def encrypt(original_text, shift_amount):
    #Shift each letter of the original text forwards in the alphabet by the shift amount and print the encrypted text
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount #Shifts position by shifted amount
        shifted_position %= len(alphabet) #Wraps the alphabet array around the position at Z (position 25)
        cipher_text += alphabet[shifted_position]

    print(cipher_text)

#Create a function 'decrypt()' takes the original_text and shifts the text back to the amount
def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(cipher_text)
    
#Call encrypt() function and pass in the user inputs
if direction == 'encode':
    encrypt(original_text=text, shift_amount=shift)
else:
    decrypt(original_text=text, shift_amount=shift)