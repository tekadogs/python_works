username = input('Input Username:')
usernames = []
usernames.append(username)

print('Hello ' +username)
input('Would you like to see database? (y/n)')
if input == 'y':
    print(usernames)
else:
    print('Goodbye!')
