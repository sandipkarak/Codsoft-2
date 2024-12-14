
# sum = 0 
# a = 9
# n = int (input("enter the number:"))
# for i in range (1,n+1):
#     sum = sum + a
#     a+=4
# print(sum)



sum = 0 
a = 1
n = int (input("enter the number of n:"))
x = int (input("enter the number of x:"))
for i in range (1,n+1):
    sum = sum + x**a
    a+=1
print(sum)