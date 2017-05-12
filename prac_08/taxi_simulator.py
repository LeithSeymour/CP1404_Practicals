from prac_08.taxi import Taxi
from prac_08.taxi import SilverServiceTaxi

MENU = "Q) uit \nC) Hoose taxi \nD) rive"


def main():
    taxis = [ Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
              SilverServiceTaxi("Hummer", 200, 4) ]

    taxis = [ (i, j) for i, j in enumerate(taxis) ]

    def print_taxis(list_of_taxis):
        for taxi in taxis:
            print("{} - {}".format(taxi[ 0 ], taxi[ 1 ]))

    print("Lets Drive!")
    print(MENU)
    choice = ""
    total_bill = 0
    current_car = [ ]
    while choice != "Q":
        choice = input("Enter Menu Choice: ").upper()
        if choice == "C":
            print_taxis(taxis)
            taxi_selection = int(input("Enter Taxi number to ride: "))
            current_car = taxis[ taxi_selection ][ 1 ]
            print("Bill to date is ${}".format(total_bill))
        elif choice == "D":
            current_car.start_fare()
            drive_distance = int(input("How far do you want to drive: "))
            current_car.drive(drive_distance)
            total_bill += current_car.get_fare()
            print("Your {} trip cost you ${}".format(current_car.name, current_car.get_fare()))
            print("Bill to date is ${}".format(total_bill))
    print("Total trip cost: ${}".format(total_bill))
    print("Taxis are now")
    print_taxis(taxis)


if __name__ == '__main__':
    main()
