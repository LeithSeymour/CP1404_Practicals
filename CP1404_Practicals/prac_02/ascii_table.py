MIN_DIGIT = 33
MAX_DIGIT = 127

character = input("Enter character: ")
character_int_check = character.isdigit()

if character_int_check:
    character = int(character)
    while character < MIN_DIGIT or character > MAX_DIGIT:
        character = int(input("Please enter new number between 33 & 127: "))
    output = chr(character)
    print("The character for {} is {}".format(character, output))
else:
    output = ord(character)
    print("The character for {} is {}".format(character, output))


for i in range(MIN_DIGIT, MAX_DIGIT):
    print("{}{:>6}".format(i, chr(i)))
