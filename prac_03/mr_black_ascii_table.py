def main():
    # MAX_DIGIT = 33
    # MIN_DIGIT = 127
    # character = []

    def get_number(lower, upper):
        user_number = input("Enter number: ")
        number_check = user_number.isdigit()
        while not number_check:
            user_number = input("Enter number: ")
            number_check = user_number.isdigit()
        else:
            while not lower <= int(user_number) <= upper:
                user_number = input("Enter number between {} & {}: ".format(lower, upper))
                number_check = user_number.isdigit()
                while not number_check:
                    user_number = input("Enter number")
            else:
                return user_number

    number = get_number(10, 50)
    check = number.isdigit()

    if check:
        number = int(number)
        # while character < MIN_DIGIT or character > MAX_DIGIT:
        #     character = int(input("Please enter new number between {} & {}: ".format(MIN_DIGIT, MAX_DIGIT)))
        output = chr(number)
        print("The character for {} is {}".format(number, output))
    # else:
    #     output = ord(character)
    #     print("The character for {} is {}".format(character, output))

    # for i in range(MIN_DIGIT, MAX_DIGIT):
    #     print("{}{:>6}".format(i, chr(i)))


main()
