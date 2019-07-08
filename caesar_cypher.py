

def main():
    plain_text = input("Enter a word: ").lower()
    try:
        distance = int(input("Enter the distance value: "))
    except ValueError:
        print("Distance value must be a number!")
        distance = input("Enter the distance value: ")
    code = ""
    for ch in plain_text:
        ord_value = ord(ch)
        cipher_value = ord_value + distance
        if cipher_value > ord("z"):
            cipher_value = ord("a") + distance - \
                           (ord("z") - ord_value + 1)
        code += chr(cipher_value)
    print(code)


main()
