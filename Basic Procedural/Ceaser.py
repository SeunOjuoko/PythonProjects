alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt or type 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))


#Create a function 'ceaser()' that 'encrypt()' and 'decrypt()' function takes the original_text and shift the amount
def ceaser(original_text, shift_amount, encode_or_decode):
    #Shift each letter of the original text forwards in the alphabet by the shift amount and print the encrypted text
    cipher_text = ""
    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) + shift_amount #Shifts position by shifted amount
        shifted_position %= len(alphabet) #Wraps the alphabet array around the position at Z (position 25)
        cipher_text += alphabet[shifted_position]

    print(cipher_text)

#Call encrypt() function and pass in the user inputs
ceaser(text, shift, direction)