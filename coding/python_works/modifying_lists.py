#modifying lists
zodiac_signs = ['rabbit', 'goat', 'dragon']
print(zodiac_signs[0].capitalize())

zodiac_signs[0] = 'pig'
print(zodiac_signs[0].capitalize())

#adding elements
#.append

print(zodiac_signs)
zodiac_signs.append('sheep')
print(zodiac_signs)

#build lists this way

idol = []
idol.append('de shaorong')
idol.append('do mai ni')
idol.append('da tyen')

print(idol)

#inserting elements into a list
#.insert
#data types must be one type when printing

idol.insert(0, 'super idol')
print(idol)
china = idol + zodiac_signs
print(str(china)+'AAAAAAAAAAH')

#removing elements from a list
#del
print('super idol lyrics '+str(idol))
del zodiac_signs[0]
print(zodiac_signs)

#delete a element from a list and transfer it to another
nujabes = ['aurarian', 'luvsic', 'battlecry']
print(nujabes)
fav_song = nujabes.pop(0)
print(nujabes)
print(f'I really love the song {fav_song.title()} by Nujabes')

#using keywords to remove an item
#.remove
nujabes.remove('luvsic')
print(nujabes)

best = 'battlecry'
nujabes.remove(best)
print(f'in my honest opinion, {best} is the best anime opening'.title())
print(nujabes)

