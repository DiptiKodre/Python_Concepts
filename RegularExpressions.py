import re

# Regex	Meaning
# \d	Digit
# \w	Word character
# \s	Whitespace
# .	Any character
# [A-Z]	Uppercase letter
# [a-z]	Lowercase letter
# [0-9]	Digit
# +	One or more
# *	Zero or more
# ?	Zero or one
# {3}	Exactly 3
# {3,5}	3 to 5
# ^	Start
# $	End
# ()	Capture group
# `	`
# \b	Word boundary


#re.search --> finds first match
text = "My phone number is 1234567890."
result = re.search(r"\d+", text)   #\d-->digits , r--> raw string , + --> one or more occurrences
print(result.group())  # Output: 1234567890

#re.match() --> checks for a match only at the beginning of the string
#.group() --> returns the matched string
text2 = "Python is easy to learn."
result2  = re.match(r"Python",text2)
if result2:
    print("Match found:", result2.group())  # Output: Match found: Python

#re.findall() -- finds all matching values
text3 = "I have 10 apples and 20 oranges"
numbers = re.findall(r"\d+",text3)
print(numbers)

text4 = "Python is difficult"
result4 = re.sub(r"difficult","easy",text4)
print(result4)

#Find words starting with P
# \b → word boundary
# P → starts with P
# \w* → zero or more word characters

text5 = "Python is Powerful and Popular languagre"
words = re.findall(r"\bP\w*",text5)
print(words)

# Check whether a string ends with something
# $ means end of string.
text6 = "Here it's raining heavily"
if re.search(r"heavily$",text6):
    print("Ends with heavily")

#find words with exact 5 letters
#{5} --> exact 5
text7 ="hello python there is super surprise apple"
result7 = re.findall(r"\b\w{5}\b",text7)
print(result7)

#  Find words between 3 and 5 letters
text8 ="hello python there is super try cat bat deer surprise apple"
result8 = re.findall(r"\b\w{3,5}\b",text8)
print(result8)


#  Find an email address 
# john.smith123 @ gmail . com
# └─────────────┘ └────┘ └──┘
#  [\w.-]+       [\w.-]+ \w+

text9 = "my email address is diptikodre71@gmail.com"
gmail = re.findall(r"[\w.-]+@[\w.-]+\.\w+",text9)
print(gmail)

# Find multiple email addresses
text10 = """
john@gmail.com
alice@yahoo.com
admin@example.org
"""
gmails = re.findall(r"[\w.-]+@[\w.-]+\.\w",text10)
print(gmails)

#  Validate a 10-digit phone number
phone_number = "8624031919"
if re.fullmatch(r"\d{10}",phone_number):
    print("valid number")
else:
    print("Invalid phone number")


# Indian phone number
# For a basic Indian mobile number starting with 6, 7, 8, or 9:
phone="9011678934"
pattern = r"[6-9]\d{9}"
if re.fullmatch(pattern,phone):
    print("Valid indian phone number")
else:
    print("Invalid Indian phone number")