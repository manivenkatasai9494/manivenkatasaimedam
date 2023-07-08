"""
purpose = to encode and decode the values
example give input = hello
              shitf = 5
              it adds alphabets to 5and prints the answer
              op = mjqqt


"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def decryption(given_word, shift_no):
    answer = ""
    for letter in given_word:
        alphabet_index = alphabet.index(letter)
        new_index = alphabet_index - shift_no
        answer = answer + alphabet[new_index]
    print(f"decode answer = {answer}")


def encription(given_word, shift_no):
    answer = ""
    for letter in given_word:
        alphabet_index = alphabet.index(letter)
        new_index = alphabet_index + shift_no
        answer += alphabet[new_index]
    print(f"answer is {answer}")


if direction == "encode":
    encription(given_word=text, shift_no=shift)
elif direction == "decode":
    decryption(given_word=text, shift_no=shift)

