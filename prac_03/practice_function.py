# def get_number(lower, upper):
#     number = input("Enter character: ")
#     while number.isdigit():
#         if lower < int(number) < upper:
#             break
#         else:
#             number = input("Enter character: ")
#     return(number)
#             # character_int_check = character.isdigit()
#
#
# number_received = get_number(10, 50)

def get_number(lower, upper):
    user_number = input("Enter number: ")
    number_check = user_number.isdigit()
    while not number_check:
        user_number = input("Enter number: ")
        number_check = user_number.isdigit()
    else:
        while not lower <= int(user_number) <= upper:
            user_number = input("Enter number: ")
            number_check = user_number.isdigit()
            while not number_check:
                user_number = input("Enter number")
        else:
            return user_number


        # character_int_check = character.isdigit()


number = get_number(10, 50)
print(number)
