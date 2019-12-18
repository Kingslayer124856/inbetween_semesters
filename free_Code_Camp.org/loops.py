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
