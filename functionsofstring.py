# .endswith("") function to check if string ends with the given string or not
# returns boolean value
a="my alibi is gonna face charges from law"
print(a.endswith("law"))
print(a.endswith("judge"))
print(a.endswith("w"))

#.capitalize() function makes the first char of the string capital and all other to lower cases
b="my man HAS GONE tO fair."
print(b.capitalize())

# .find("") function helps to find if certain string is present in the parent string or not , also
# its position , returns the index no. where string starts if the string is present , and returns -1
# if string is not present in the parent string
print(b.find("man"))
print(a.find("man"))
print(b.find("law"))
print(a.find("law"))

kid_str="a e i o u"
par_str="Vowels are a e i o u ."
print(par_str.find(kid_str))

# .count("") function  returns the number of times a certain string is repeating in the parent string
c="you are right to have the right to be right but you can't be always right"
print(c.count("right"))
print(c.count(" "))
print(c.count("z")) # will give zero as z doest not exists in c
print(c.count("")) # counting empty string ("") of a string in python gives (length of string + 1) as
# it counts the boundary line between blocks of array for ex. |H|e|L|L|o| has 6 boundary lines separating the block

# .replace("old","new") function is used to replace some string or its part with a new string
# it is important to store the updated string in a variable because anything if stored then only is saved in RAM
# otherwise it is lost after the line , direct printing also just displays the result but to storing is essential
# for future use
str_us=" Hello citizen of united states of america "
str_ind=str_us.replace("united states of america","India")
print(str_ind)
str_ind=str_ind.replace("India","united states of India") # str_ind value is updated here as well as in RAM
print(str_ind)

# .startswith("") function is used to check if parent string starts with a certain string or not and gives boolean value
print(a.startswith("my"))
print(b.startswith("My"))
print(c.startswith("y"))
print(str_us.startswith("Hello"))
print(str_us.startswith(" Hello"))

# .isalnum() function checks if given string is alphanumeric or not and gives boolean values
# also gives true if all characters are either letter or number too but no special character is permissible
str_test="So today I called her 2 times to say happynewyear2026"
str_a=str_test[-16:] # "happynewyear2026"
str_b=str_test[-17:] # " happynewyear2026"
str_c=str_test[-16:-4] # "happynewyear"
str_d=str_test[-4:] # "2026"
print(str_a.isalnum()) # gives true as str is mix of letters and numbers
print(str_b.isalnum()) # gives false cause " " space before h is a special symbol
print(str_c.isalnum()) # true as all are letters
print(str_d.isalnum()) # true as all are numbers

# .islower() checks if all letters in string are in lower case and gives boolean values
print(a.islower())
print(b.islower())



