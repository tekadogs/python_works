#3-4
guest = []
guest.append('ivan')
guest.append('nash')
guest.append('carl')
guest.append('joshua')
guest.append('jamile')
guest.append('benhur')
guest.append('carlos')

print(f'This is the list of guest: \n{str(guest).title()}\n')

for name in guest:
	print(f'Greetings {str(name).title()}, you are hereby invited to my dinner!')

ghost = {'nash', 'ivan', 'carl'}
guest = [e for e in guest if e not in ghost]

print(f'\nThese are the people who cannot make it tonight: \n{str(ghost).title()}\n')

for name in guest:
	print(f'Greetings {str(name).title()}, you are hereby invited to my dinner!')

new_guest = ['lara', 'estopace', 'yujin']
guest = guest + new_guest

print(f'\nOMG! I found a bigger table, meaning more space is available. Ive invited the following people: \n{str(new_guest).title()}')
print(f'\nAll of the Guest: {str(guest).title()}')

