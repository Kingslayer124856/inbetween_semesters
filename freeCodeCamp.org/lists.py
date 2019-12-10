"""
lists
"""
# basics
dnd_friends = ['Matthew', 'Lachlan', 'Saxon', 'Jordan', 'Brett']
print(dnd_friends[0])

# list functions
lucky_numbers = [4, 8, 42, 16, 23, 56]
dnd_friends = ['Matthew', 'Lachlan', 'Saxon', 'Jordan', 'Brett']
friends = dnd_friends.copy()
# dnd_friends.extend(lucky_numbers) # extends the list by adding another list to the end of it
# dnd_friends.append('Creed') # adds to the end of the list
# dnd_friends.insert(1, 'Kelly')
# dnd_friends.remove('Saxon')
# dnd_friends.clear()
# dnd_friends.pop() # removes that last item
# . reverse()
dnd_friends.sort()
lucky_numbers.sort()
# print(dnd_friends.index("Jordan"))
print(lucky_numbers)
print(friends)

# Tuples [1.19.00]


