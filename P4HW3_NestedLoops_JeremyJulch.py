# Making Nested Loops
# 10-17-2019
# CTI-110 PH4HW3-Nested Loops
# Jeremy Julch
#






# Making the first loop
for row in range(6):
    print('#', end='', sep='')
    # Making the nested loop to create the spaces between the #
    for spaces in range(row):
        print( ' ', end='', sep='')
    # Making the second #
    print('#', sep='')
