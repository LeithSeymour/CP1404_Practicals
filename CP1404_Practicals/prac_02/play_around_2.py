character = input("Enter character: ")
character_int_check = character.isdigit()

LOWER = 33
UPPER = 127

if character_int_check:
    character = int(character)
    while character < 33 or character > 127:
        character = int(input("Please enter new number between 33 & 127: "))
    output = chr(character)
    print("The character for {} is {}".format(character, output))
else:
    output = ord(character)
    print("The character for {} is {}".format(character, output))

# for i in range(33, 127):
#     print("{}{:>6}".format(i, chr(i)))
