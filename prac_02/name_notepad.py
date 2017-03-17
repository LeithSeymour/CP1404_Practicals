name = input("Enter Your name: ")
name_file = open('data.txt', mode='w')
name_file.write(name)
name_file.close()
#
read_name_file = open('data.txt', mode='r')
read_name = read_name_file.read().strip()
print("Your name is {}".format(read_name))
read_name_file.close()

numbers = open('numbers.txt', mode='r')
number1 = int(numbers.readline())
number2 = int(numbers.readline())
sum_of_nums = number1 + number2
print("Read lines were: {} & {} equating to a sum of {}".format(number1, number2, sum_of_nums))
numbers.close()
