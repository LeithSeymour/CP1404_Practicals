from prac_07.Guitars import Guitar

Gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
Line6 = Guitar("Line 6 JTV-59", 2010, 1512.9)

print(Gibson)

print(Gibson.get_age())
print(Gibson.is_vintage())

print(Line6.get_age())
print(Line6.is_vintage())

