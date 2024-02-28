text = 'Hello World'
shift = 3
encrypted_text =''

def caesar():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in text.lower():
        # Ensure not text character are taken care of by just appending them
        if char.isalpha():
            encrypted_text += char
        else:
            # Find the index of char in the string alphabet
            index = alphabet.index(char)
            new_index = (index + shift) % len(alphabet)
            new_char = alphabet[new_index]
            encrypted_text.append(new_char)
    print(encrypted_text)

