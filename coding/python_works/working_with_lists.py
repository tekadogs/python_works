#4-1
pizzas = ['pepperoni', 'new york', 'spinach','hawaian']
for pizza in pizzas:
    print('I really like the ' +pizza.title()+' in Yellow Cab')

print('\nThe cheesy pizza\nBest ever italian food\nTaste from the heavens\n')

#4-2
felines = ['cat', 'lion', 'tiger', 'leopard']
for feline in felines:
    print(feline.title()+'s are scary as hell!')

print('\nIf I were to get chased by one of these creatures, I would be dead')

#numerical list
print('\n')
for value in range(0,3):
    print(value)

#printing number into list
print('\n')
numbers = list(range(0,5))
print(numbers)

print('\n')
numbers = list(range(0,21,2)) #<--- Adds 2 until it reaches 21
print(numbers)

print('\n')
squares = []
for num in range(0,11):
    squares.append(num**2)

print(squares)
