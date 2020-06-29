from mod2 import mod10_to_mod2 as dec2bin

n=3

for i in range(2**n):
    binary_number=dec2bin(i,n)
    print(binary_number)
