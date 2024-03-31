#for loop - it used for a range of numbers or character or anything 
#for loop is the best used when we know the range of something
#example let us consider the below code which prints the range of numbers inclusively
for i in range(1,10):
    print(i, end=' ')
print("\n")
#example let us consider the below code which prints the elements of the array 
for i in [1,2,3,4,5]:
    print(i, end =' ')
print("\n")
#end here is used to print all the elements in the same line
for i in "hello":
    print(i,end =' ')
print("\n")
# "\n" adds a new line in python 

#for-else loop
#in a for else loop the else statment will only run if the loop runs all its iterations
#if the loop fails to run all its iterations due to a break statment the else statment will not be run
for i in range(10):
    print(i)
else:
    print("Finsihed running the loop")

for i in range(10):
    print(i)
    if(i == 5): break
else:
    print("Finished running the loop")


#using underscore in a for loop
#if you are not using a variable initaited in the for loop you can use a underscore to not create memory for a variable
for _ in range(5):
    print("hello world")