#factorial using for loop
num = int(input("Enter the number: ")) #this is way we take dynamic input in python we declare the type of variable it is and then write the input function

factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("factorial is:", factorial)