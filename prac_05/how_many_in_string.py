# string = input("Enter a string of words")
string = "Hello my name is leith the biggest leith you will ever see name"


# words_of_string = string.split()
# d = {k:v for k,v in enumerate(words_of_string)}
# print(d)

def word_count(string):
    entered_string = string.lower().split()
    my_dict = {}
    for item in entered_string:
        my_dict[item] = entered_string.count(item)
    print(my_dict)


word_count(string)
