#""'Python code for converting camelCase to snake_case"""
#camelCase: In this convention, the first letter of each word except the first word is capitalized and the words are run together. For example, firstName and preferredFirstName.
#snake_case: In this convention, all letters are lowercase and words are separated by underscores (_). For example, first_name and preferred_first_name.

def camel(text):
    #Function to convert a string from camelCase to snake_case.
    s = ""
    for let in text:
        if (let.isupper()):
            s += ("_"+let.lower())
            continue
        s += let
    return s

text = input("camelCase: ")
print ("snake_case:", camel(text))
#This code assumes that the user input is a valid camelCase string.
