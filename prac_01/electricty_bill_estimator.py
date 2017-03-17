# Electricity Bill estimator

# Tariff Constants
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

# Calculator
menu = "A - Tariff 11\nB - Tariff 31\nC - No Tariff (input required)\nQ - Quit"
print(menu)
choice = input("Select an option: ").upper()
while choice != "Q":
    if choice == "A":
        billing_days = int(input("How many days in billing period: "))
        kWh_daily_use = float(input("Daily kWh usage: "))
        total_bill = float(kWh_daily_use * billing_days * TARIFF_11)
        print("Total cost is $" + str(total_bill))
    elif choice == "B":
        billing_days = int(input("How many days in billing period: "))
        kWh_daily_use = float(input("Daily kWh usage: "))
        total_bill = float(kWh_daily_use * billing_days * TARIFF_31)
        print("Total cost is $" + str(total_bill))
    elif choice == "C":
        billing_days = int(input("How many days in billing period: "))
        kWh_daily_use = float(input("Daily kWh usage: "))
        cents_per_kWh = int(input("Cents per kWh: $0.")) / 100
        total_bill = float(kWh_daily_use * billing_days * cents_per_kWh)
        print("Total cost is $" + str(total_bill))
    else:
        print("Invalid option")
        choice = input("Select an option: ").upper()
    print(menu)
    choice = input("Select an option: ").upper()
print("Thank you")
