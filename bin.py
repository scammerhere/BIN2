import time,os,sys


def text_to_binary(text):
    binary_string = ""
    for char in text:
        # Convert each character to its ASCII value
        ascii_value = ord(char)
        # Convert the ASCII value to binary representation
        binary_value = bin(ascii_value)[2:]  # [2:] removes the "0b" prefix
        # Pad the binary value with leading zeros to make it 8 bits long
        padded_binary = binary_value.zfill(8)
        # Append the padded binary value to the final binary string
        binary_string += padded_binary
    return binary_string


def binary_to_text(binary):
    text = ""
    # Split the binary string into 8-bit chunks
    binary_chunks = [binary[i:i+8] for i in range(0, len(binary), 8)]
    for chunk in binary_chunks:
        # Convert the binary chunk to decimal
        decimal_value = int(chunk, 2)
        # Convert the decimal value to its corresponding character
        character = chr(decimal_value)
        # Append the character to the final decrypted text
        text += character
    return text

def rob():
    input_binary = input("Enter the binary to decrypt: ")
    decrypted_text = binary_to_text(input_binary)
    print("Decrypted text: ", decrypted_text)

def roob():
    input_text = input("Enter the text to encrypt: ")
    encrypted_binary = text_to_binary(input_text)
    print("Encrypted binary: ", encrypted_binary)



logo="""
██████╗ ██╗███╗   ██╗
██╔══██╗██║████╗  ██║
██████╔╝██║██╔██╗ ██║
██╔══██╗██║██║╚██╗██║
██████╔╝██║██║ ╚████║
╚═════╝ ╚═╝╚═╝  ╚═══╝
                     
"""
os.system("clear")
print(logo)
print("⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌⇌")
print("[01] TEXT TO BINARY")
print("[02] BINARY TO TEXT")
print("[00] EXIT")
ban = input("CHOOSE::")
if ban in ["1","01"]:
    roob()
    time.sleep(0.5)
    exit()
if ban in ["2","02"]:
    rob()
    time.sleep(0.05)
    exit()
if ban in ["0","00"]:
    exit()
else:
    print("CHOOSE RIGHT OPTIONS")
    exit()

