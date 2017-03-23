def main():
    user_name = get_name()
    for_every = input("Enter integer to print every x number: ")
    check = for_every.isdigit()
    while not check:
        for_every = input("Enter integer to print every x number: ")
        check = for_every.isdigit()
    else:
        for_every = int(for_every)
        print_name(user_name, for_every)


def print_name(user_name, for_every):
    print(user_name[::for_every])


def get_name():
    user_name = input("Enter name: ")
    return user_name


main()
