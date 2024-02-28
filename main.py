text = 'Hello World'
shift = 3


def caesar():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in text.lower():
        
        # Ensure not text character are taken care of by just appending them
        if not char.isalpha():
            encrypted_text += char
        else:
            # Find the index of char in the string alphabet
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print(encrypted_text)

caesar()