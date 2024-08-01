"""
No error checking with v1, just simple shifting
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    new_word = ""
    for letter in text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            new_letter_index = letter_index + shift
            new_letter = alphabet[new_letter_index]
            new_word += new_letter
        else:
            print("...")
    print(new_word)
    
encrypt(text=text, shift=shift)
