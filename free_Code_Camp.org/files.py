"""
Working with Text files
By: Cassandra King
Date: 3/1/20
Note:
"""
# Reading files
# 'r' read, 'w' write, 'a' append, 'r+' read and write
employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    # read(), readable(), readline(), readlines()
    print(employee)
employee_file.close()

# Writing to files
# adding to the file
employee_file = open("employees.txt", "a")
employee_file.write("Kelly - Customer Service \n")
employee_file.close()
# Writing a new file
employee_file = open("employees.txt", "w")
employee_file.write("Kelly - Customer Service \n")
employee_file.close()
