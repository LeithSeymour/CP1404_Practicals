def main():
    number = get_number(10, 50)

    if number.isdigit():
        number = int(number)
        output = chr(number)
        print("The character for {} is {}".format(number, output))

        # for i in range(MIN_DIGIT, MAX_DIGIT):
        #     print("{}{:>6}".format(i, chr(i)))


def get_number(lower, upper):
    user_number = input("Enter number: ")
    number_check = user_number.isdigit()
    while not number_check:
        user_number = input("Enter number: ")
        number_check = user_number.isdigit()
    while not lower <= int(user_number) <= upper:
        user_number = input("Enter number between {} & {}: ".format(lower, upper))
        number_check = user_number.isdigit()
        while not number_check:
            user_number = input("Enter number")
    return user_number

# TODO: check exceptions notes, week 2, near end

main()
