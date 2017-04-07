COLOUR_AND_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                   "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                   "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74",
                   "azure1": "#f0ffff"}

colour_table = COLOUR_AND_CODE.items()
colour_table = sorted(colour_table)
for i, j in colour_table:
    print("{}".format(i))
selection = input("\nType the colours name for it's hexadecimal: ")

while selection != "":
    if selection in COLOUR_AND_CODE:
        print(selection, "is", COLOUR_AND_CODE[selection])
        break
    else:
        print("Invalid name")
    selection = input("Type the colours name for it's hexadecimal: ")