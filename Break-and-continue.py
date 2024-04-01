#break statement - when ever the break statement is executed in a loop terminates and the next peice of code executes
for i in range(10):
    if(i==5):
        break
    print(i, end =' ')
#output = 0 1 2 3
#continue statement - when ever the continue statement is executed in a loop, the loop skips the present iteration and jumps to the next one and execute the remaining loop
for i in range(10):
    if(i==5):
        continue
    print(i, end =' ')
#output - 0 1 2 3 4 6 7 8 9
#in the above 2 codes you can clearly see the result that the first code prints the values up until 5 and 2nd code prints all the values just skipping 5.