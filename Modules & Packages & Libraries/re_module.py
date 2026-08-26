# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# https://www.w3schools.com/python/python_regex.asp

import re

txt = "alireza hosseini is a programmer"
x = re.search("^a", txt)  # ^a means word that starts with a
if x:
    print("we have word start with a")
else:
    print("we don't have word start with a")
