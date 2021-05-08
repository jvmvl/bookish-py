"""
Python Program:
 Using a dictionary to store the char frequency in string
"""
input_string = "LOREMIPSUMDOLORSITAMETCONSECTETURADIPISCINGELIT"
frequencies = {}

for char in input_string:
    if char in frequencies:
        frequencies[char] += 1
    else:
        frequencies[char] = 1

# Show Output
print("Per char frequency in '{}' is :\n {}".format(input_string, str(frequencies)))
