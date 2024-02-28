#3-8
location = ['japan','canada','iceland','new zealand']
print(f'This is the original list \n {location}')

print(f'\nThis is the sorted list \n {sorted(location)}')

print(f'\nThis is the original list \n {location}')

print(f'\nThis is the reverse sorted list \n {sorted(location, reverse=True)}')

print(f'\nThis list is still intact! \n {location}')

location.reverse()
print(f'\nThis is the list in reverse aka not sorted \n {location}')
location.reverse()
print(f'\nOk it is sorted again \n {location}')

location.sort()
print(f'\nThe list is now permanently sorted \n{location}')
location.sort(reverse=True)
print(f'\nNow it is permanently reversed!!! \n{location}')
#3-10