alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a',
            'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amount):
            cipher_text = ""
            for letter in plain_text:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                if new_position > 51:
                    new_position = new_position - 51
                new_letter = alphabet[new_position]
                cipher_text += new_letter    
            print(f"The encoded text is {cipher_text}")
def decrypt(plain_text, shift_amount):
            cipher_text = ""
            for letter in plain_text:
                position = alphabet.index(letter)
                new_position = position - shift_amount
                if new_position > 51:
                    new_position = new_position - 51
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            print(f"The edecoded text is {cipher_text}")


user_choice = "Yes"
while user_choice != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    
    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(plain_text = text, shift_amount = shift)

    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(plain_text = text, shift_amount = shift)
    else:
        print("You Enter wrong command")
    user_choice = input("Do you want to try again? Type 'yes' or 'no' ").lower()