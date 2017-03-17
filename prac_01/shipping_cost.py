cost = float()
item_count = int(0)

MENU = "A - Add Quantity of identical items to Bill\nP - Print cost of shipping\nQ (for quit)"
print(MENU)
choice = input("Enter Choice: ").upper()
while choice != "Q":
    if choice == "A":
        number_of_items = int(input("Number of identical items: "))
        while number_of_items < 1:
            print("Enter a positive amount")
            number_of_items = int(input("Number of same item: "))
        cost_of_shipping = float(input("Enter cost of items: $"))
        item_count += number_of_items
        cost += number_of_items * cost_of_shipping
    elif choice == "P":
        if cost >= 100:
            cost = cost * 0.9
        print("Cost of shipping is: $", cost, "for", item_count, "items. ")
    else:
        print("Invalid option")
    print(MENU)
    choice = input("Enter Choice: ").upper()
print("Cheers.")
