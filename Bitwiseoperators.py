#bitwise operators-first the int values will be converted to binary values and then any bitwise operation is performed on it
a = 10
b = 5

print(a & b) #bitwise and operation - set's to 1 if both the bit's are 1
print(a | b) #bitwise or operation - set's to 1 if any one of the bit is 1 
print(a ^ b) #bitwise xor operation - set's to 1 if only one of the bit is 1
print(~(a+b)) #bitwise not operaiton - converts the bit to it's inverse if the bit is 1 the output will be 0 and viceversa
print(a << 1) #bitwise left shift-the left side bit is moved to left side by 1 bit and a 0 is added to the right side
print(b >> 1) #bitwise right shift-the right side bit is removed and a 0 is added to the left side