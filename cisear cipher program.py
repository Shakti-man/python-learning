from cisear_art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def ceaser(plain_text,shift_amount,direction):
    cipher_text = ""
    if shift_amount>26:
        shift_amount=shift_amount%26
    else:
        shift_amount=shift_amount
    if direction=="encode":
        for letter in plain_text:
            if letter not in alphabet:
                cipher_text+=letter
            else:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                cipher_text += alphabet[new_position]
        print(f"The encoded text is {cipher_text}")
    elif direction=="decode":
        for letter in plain_text:
            if letter not in alphabet:
                cipher_text+=letter
            else:
                position = alphabet.index(letter)
                new_position = position - shift_amount
                cipher_text += alphabet[new_position]
        print(f"The decoded text is {cipher_text}")
should_end =True
while should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction== "encode" or direction== "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
    else:
        print ("Yo Hommie! I gave you 2 options either encrypt or decrypt and you can't even chose 1. \nShame on YOU!!!! ")
        break
    ceaser(text,shift,direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = False
        print("Goodbye")

