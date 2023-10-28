# String data type

# literal assignment
first = "Isekai"
last = "Dev"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statemant = "I like rock music from the " + decade + "s."
print(statemant)

# Multiple lines
multiline = '''
Hey, how are you?                                        

I was just checking in.
                                All good?

'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located' 
print(sentence)

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                                     "
multiline = "                     " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(17, ".") + "$2".rjust(4))
print("Cheesecake".ljust(18, ".") + "$4".rjust(4))

print("")

# string index values
# index start at 0
# 0 first letter
# 1 second letter
# -1 end (don't know how many letters)

print(first[1])
print(first[-1])
print(first[1:-1]) #gives you a range without the end
print(first[1:]) #gives you a range with the end

# Some methods return boolean data
print(first.startswith("I"))
print(first.endswith("Z"))

# Boolean data type (means TRUE or FALSE DATA)
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type (have . in them)
gpa = 3.28
y = float(1.14) 
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))

import math # when saved goes to the top

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
#zip_value = int("New York")
#ValueError: invalid literal for int() with base 10: 'New York'
