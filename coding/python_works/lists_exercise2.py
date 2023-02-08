#3-4
guest = ['haruko','rel','ryuuko','rebecca','lucy','mamimi']

print(f"This is the list of guests for today's dinner: \n{str(guest).title()}\n")
for name in guest:
	print(f'Greetings {str(name).title()}, you are hereby invited to my dinner!')

#3-5
print(f'\nUh oh! Looks like {guest.pop(0).title()} can not join us today\n')
guest.insert(0,'naota')
for name in guest:
	print(f'Greetings {str(name).title()}, you are hereby invited to my dinner!')

#3-6
print('\nA bigger table has been found, new set of invitation message has been sent!\n')
guest.insert(0,'kaesha')
guest.insert(4,'rei')
guest.append('asuka')

for name in guest:
	print(f'Greetings {str(name).title()}, you are hereby invited to my dinner!')

#3-7
print(f'\nSorry everyone, only two guest can occupy\n')

for x in range(0, 7):
	print(f'{str(guest.pop(0)).title()}, you are not invited due to limited venue space')
	
print(f'\n{str(guest[0]).title()} and {str(guest[1]).title()}, you are still invited for tonight\n')
del guest[0]
del guest[0]
print(guest)

