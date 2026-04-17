# Data Cleaner
# Assignment Objectives:
# Write a script that splits the raw string into exactly four distinct string elements using the comma as a delimiter.
# Iterate through the resulting items to strip out all leading and trailing whitespace.
# Target the email element specifically and convert the entire string to lowercase.
# Target the age element and convert it from a string to an `integer`.
# Target the salary element, remove the `$` character, and convert it to a `float`.

input_string = "  user_name123  , TEST_EMAIL@example.com ,  24 ,  $45000.50  "

def data_clean(input_string):
    remove_spaces = input_string.replace(" ", "")
    temp_list = remove_spaces.split(",")
    for i in range(len(temp_list)):
        if "@" in temp_list[i]:
            temp_list[i] = temp_list[i].lower()
        elif temp_list[i].isdigit():
            temp_list[i] = int(temp_list[i])
        elif "$" in temp_list[i]:
            temp_list[i] = float(temp_list[i].replace("$", ""))
    return temp_list

print(data_clean(input_string))