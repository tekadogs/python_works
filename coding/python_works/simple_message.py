'''2/5/2023 Guidelines in Variables'''
'''
Variable names can contain only letters, numbers, and underscores.

They can start with a letter or an underscore, but not with a
number. For instance, you can call a variable message_1 but not
1_message.

Spaces are not allowed in variable names, but underscores can be
used to separate words in variable names. For example,
greeting_message works, but greeting message will cause errors.

Avoid using Python keywords and function names as variable
names; that is, do not use words that Python has reserved for a
particular programmatic purpose, such as the word print.

Variable names should be short but descriptive. For example, name
is better than n, student_name is better than s_n, and name_length is
better than length_of_persons_name.

Be careful when using the lowercase letter l and the uppercase
letter O because they could be confused with the numbers 1 and 0
'''

'''Exercise on Variables'''

message = "Subrscribe to Tekadags!!!"
print(message)

message = "PLEASE"
print(message)

print('This is a string, but what happens if "I add double quotation?"')

name = "maron dagang"
print(name.title())
print(name.upper())
print(name.lower())

firstname = "carl"
lastname = "villena"
fullname = f"{firstname} {lastname}"
print(fullname)

'''f means f-string or formats'''

