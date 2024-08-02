"""
Added the decode caesar cipher part
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    new_word = ""
    for letter in text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            new_letter_index = letter_index + shift
            if new_letter_index > 25:
                overlap = new_letter_index % 26
                new_letter = alphabet[overlap]
            else:
                new_letter = alphabet[new_letter_index]
            new_word += new_letter
        else:
            print("...")
    print(new_word)
    
def decrypt(encrypted_text, shift_amount):
  decrypted_text = ""
  for letter in encrypted_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    decrypted_text += alphabet[new_position]
  print(f"The decoded text is {decrypted_text}")
 
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(encrypted_text=text, shift_amount=shift) 
else:
    print("Wrong choice, please enter encode or decode")
  
