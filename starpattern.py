n = 5
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(i))
    
for i in range(n):
    for j in range(n-i,0,-1):
        print(" ",end=' ')
    for k in range(2*i+1):
        if k==0 or k==2*i or i==n-1:
            print("* ",end='')
        else:
            print(" ",end=' ')
    print("\r")
    
for i in range(n):
    for j in range(i+1):
        if j==0 or j==i or i==n-1:
            print("* ",end="")
        else:
            print(' ',end=" ")
    print("\r")
    
# power of 11 is the sort term to print the pascal traingle
for i in range(n):
    print(' '*(n-i)+" ".join(map(str,str(11**i))))

# while loop problem start

# i = 0
# j = 0
# while j <=10:
#     if i %2 == 0:
#         print(i)
#         j+=1
#     i+=1

# i = 0

# while i <300:
# #     i+=10
# #     print(i)

# i = 105
# while i >=1:
#     print(i)
#     i-=7
    
# num = 10
# while num>=0:
#     print(num)
#     num-=1
    

# res = 0
# for i in range(10):
#     res+=i
# print(res) 
 
n = 5
for i in range(n):
    print(" "*(n-i)+"* "*(i))


n = 5
for i in range(n):
    for j in range(2*n-i,0,-1):
        print(' ',end=' ')
    for j in range(2*i+1):
        print('* ',end='')
    print("\n")
        
n = 5
for i in range(n):
    print(" "*(n-i)+" ".join(map(str,str(11**i))))

n = 5
for i in range(n):
    for j in range(n-i,0,-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        if k==0 or k==2*i or i==n-1:
            print("* ",end='')
        else:
            print(" ",end=' ')
    print('\r')
    
for i in range(n):
    for j in range(i):
        if j==0 or j==i-1 or i==n-1:
            print("* ",end="")
        else:
            print(" ",end=" ")
    print("\r")

n = 5
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=' ')
    print("\r")
    
for i in range(1,n):
    for j in range(i+1):
        print("*",end=' ')
    print('\r')
    
for i in range(n):
    for j in range(i):
        print('*',end=" ")
    print("\r")
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print("\r")    

n = 5
for i in range(1,n):
    for j in range(1,n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print("\r")
    
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*(i))
for i in range(2,n+1):
    print(" "*(n-i)+"* "*(i))
    
for i in range(1,n):
    print(" "*(n-i)+"* "*(i))
    
res = 1 
for i in range(n):
    for j in range(i):
       print(res,end=" ")
       res+=1 
    print("\r")
def function(bits):
    while len(bits) > 1:
            current = bits.pop(0)
            if current == 1:
                bits.pop(0)
    if len(bits) == 0:
        return False
    return bits[0] == 0

print(function([1,1,1,0]))