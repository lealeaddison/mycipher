import sys

# takes message and returns the encoded message based on the shift value
def caesar_cipher(message, shift):
    shifted_message = ""
    for letter in message.upper():
        if letter.isalpha():
            shifted_letter = chr((ord(letter) - 65 + shift) % 26 + 65)
            shifted_message += shifted_letter
    return shifted_message

if len(sys.argv) < 2:
    print("Usage: python caesar_cipher.py message [shift]")
    sys.exit()

message = sys.argv[1]
shift = 2

if len(sys.argv) >= 3:
    shift = int(sys.argv[2])

encoded_message = caesar_cipher(message, shift) # calling function

# Print the encoded message in blocks of five letters, ten blocks per line
for i in range(0, len(encoded_message), 5):
    print(encoded_message[i:i+5], end=" ")
    if (i+5) % 50 == 0:
        print()
