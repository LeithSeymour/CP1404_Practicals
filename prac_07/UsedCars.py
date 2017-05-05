from prac_07.Car import Car


def main():
    bus = Car("bus", 180)
    bus.drive(30)
    limo = Car("limo", 100)
    limo.add_fuel(20)
    print("fuel =", bus.fuel)
    limo.drive(115)
    print("odo =", bus.odometer)
    print(bus)

    # print("fuel =", bus.fuel)
    # print("odo =", bus.odometer)
    # print(bus)


main()
