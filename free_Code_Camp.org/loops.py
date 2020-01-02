"""
Loops
by: Cassandra King
date: 18/12/19
"""
# While Loops
i = 1
while i <= 10:
    print(i)
    i += 1
print("done with loop")

# while loop menu example
MENU = ["L - list"
        "S - Status"
        "E - Edit"
        "Q - quit"
        ]
print(MENU)
choice = input("Menu Choice").upper()
while choice != 'Q':
    if choice == 'L':
        print("list")
    elif choice == "S":
        print("Status")
    elif choice == "E":
        print("Edit")
    else:
        print("Invalid Input, try again")
        print(MENU)
        choice = input("Menu Choice").upper()
breakpoint()

# For Loop
# Examples
# printing each letter in string on its own line
for letter in "Giraffe Academy":
    print(letter)
# in each iteration the list is added by the array
friends = ["Jim", "Karen", "Kevin"]

for friend in friends:
    print(friend)
# Printing a list from 0 to 10 not including 10 as it starts with 0 not 1
for index in range(10):
    print(index)
# able to access the array using index
len(friends)
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not First")
