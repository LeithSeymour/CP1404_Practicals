numbers = []
for i in range(0, 5):
    user_number = input("Enter a number: ")
    user_number = int(user_number)
    numbers.append(user_number)

print("First number is: {}".format(numbers[0]))
print("Last number is: {}".format(numbers[-1]))
print("The smalled number is: {}".format(min(numbers)))
print("The largest number is: {}".format(max(numbers)))
print("The average number is: {}".format(sum(numbers)/len(numbers)))
