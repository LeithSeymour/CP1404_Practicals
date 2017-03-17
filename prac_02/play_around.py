def main():
    valid_input = False
    while not valid_input:
        try:
            character = input("Enter character: ")
            character_int_check = character.isdigit()
            if character_int_check:
                character = int(character)
                while character < 33 or character > 127:
                    character = int(input("new number"))
                    # if character < 33 or character > 127:
                    #     character = int(input("Please enter new number between 33 & 127: "))
            else:
                valid_input = True
        except ValueError:
            print("Invalid input. Enter a new number")

            # for i in range(33, 127):
            #     print("{}{:>6}".format(i, chr(i)))


main()
