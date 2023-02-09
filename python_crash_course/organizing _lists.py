#sorting order using .sort() permanently <---Alphanetically
gundam = ['exia','rx78','wing', 'strike']
print(gundam)
gundam.sort()
print(gundam)
gundam.sort(reverse=True)
print(gundam)

#sorting order temporarily using sorted() <---Alphabetically
print('This is the original lists of Gundams:')
print(gundam)
print('\nThis is a sorted list:')
print(sorted(gundam))
print('\nThis is the original list again')
print(gundam)
#reverse is just the reverse of list
gundam.reverse()
print(gundam)
#find length of a list
print(len(gundam))