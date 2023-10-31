#Michael Pierre-Canel
def encode(password):
    encoded_password = ''.join(str((int(digit) + 3) % 10) for digit in password)
    return encoded_password
    
#Giuliana Silva
def decode(decoded_password):
    newNumber = ""
    newDigit = ""
    for digit in decoded_password:

        if int(digit) >= 3:
            newDigit = int(digit) - 3

        if int(digit) == 0:
            newDigit = "7"

        if int(digit) == 1:
            newDigit = "8"

        if int(digit) == 2:
            newDigit = "9"

        newNumber += str(newDigit)

    return newNumber

#Michael Pierre-Canel
def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print(f"Your password has been encoded and stored: {encoded_password}")

        elif choice == "2":
            encoded_password = input("Please enter the encoded password: ")
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
