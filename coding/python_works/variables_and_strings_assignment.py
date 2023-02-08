first_name = "   ayami   "
last_name = "   aguila   "
full_name = f"{last_name} {first_name}"

greeting_msg = f"Hello {full_name.title()}, are you still sick?"
quotemsg = "Even we who were not chosen yesterday are still holding onto tommorow"

print(greeting_msg)

print(full_name.title())
print(full_name.lower())
print(full_name.upper())

print(f'{full_name.title()} once said, "{quotemsg.title()}"')

whitespace = f'{first_name}\n\t{last_name}'
whitespace = whitespace.strip()
#whitespace = whitespace.lstrip()
print(whitespace)

import this
