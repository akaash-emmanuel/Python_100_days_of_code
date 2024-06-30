alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(in_text, in_shift):
    cypher_text = ""
    for letter in in_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + in_shift) % len(alphabet)
            new_letter  = alphabet[new_position]
            cypher_text += new_letter
        else:
            cypher_text += new_letter
    return cypher_text    

def decrypt(in_text, in_shift):
    cypher_text = ""
    for letter in in_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - in_shift) % len(alphabet)
            new_letter  = alphabet[new_position]
            cypher_text += new_letter
        else:
            cypher_text += new_letter
    return cypher_text  

if direction == "encode":
    encoded_text = encrypt(in_text=text, in_shift=shift)
    print(f"Encoded text is {encoded_text}")

elif direction == "decode":
    decoded_text = decrypt(in_text=text, in_shift=shift)
    print(f"Decoded text is {decoded_text}")