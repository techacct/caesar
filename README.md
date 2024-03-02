# Caesar Cipher
This is a simple Python script that implements the Caesar cipher, a type of substitution cipher, where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

# Usage
Set the text variable to the message you want to encrypt.
Set the shift variable to the number of positions you want to shift each letter by.

# Example
`text = 'Hello World'
shift = 3`

caesar()
This will output: `Khoor Zruog`

# Explanation
- The text variable holds the message to be encrypted.
- The shift variable determines the number of positions each letter is shifted in the alphabet.
- The caesar() function iterates through each character in the text, shifting alphabetic characters by the specified shift value.
- Non-alphabetic characters remain unchanged.
- The encrypted text is printed to the console.
Note: This implementation only handles lowercase letters and maintains the case of the original text.
