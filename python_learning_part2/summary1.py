msg = "Hello Python World!"
print(msg)

msg ="Hello Python Crash Course World!"
print(msg)
#case functions
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
#f strings, new line, white space
first_name = "maron"
last_name = "dagang"
full_name = f"{first_name} {last_name}"
print(full_name.title())
message = f"Hello, {full_name.title()} !!!"
print(f'\n{message}')

print("\n\tPython")
#strip white space
fav_language = " french"
print(fav_language)
print(fav_language.lstrip())
print(fav_language)

fav_language = fav_language.lstrip()
print(fav_language)

my_friend = "carl nikko villena"
print(f'Hello {my_friend.title()}, ikaw ang pinakamatabang tao sa buong mundo') 
print(f'Hello {my_friend.lower()}, ikaw ang pinakamatabang tao sa buong mundo') 
print(f'Hello {my_friend.upper()}, ikaw ang pinakamatabang tao sa buong mundo')

quote = 'trust the process'
sentence = f'{my_friend.title()} once said, {quote.capitalize()}.'
print(sentence)

friendko = "Punjabi"
friendko = f'\n\t{friendko}'
print(friendko)
print(friendko.lstrip())
print(friendko.rstrip())
print(friendko.strip())

