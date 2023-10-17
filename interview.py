# a = "Hello World"
# res = ""
# result = ["a","e","i","o","u"]
# for i in range(len(a)):
#     if a[i] not in result:
#         res+=a[i]

# print(res)

# a = "interview"
# res = set()

# result = ["a","e","i","o","u"]
# for i in range(len(a)):
#     if a[i] in result:
#         res.add(a[i])

# print(res)

# matrix1 = [[12, 7, 3],
#     [4, 5, 6],
#     [7, 8, 9]]
# matrix2 = [[5, 8, 1, 2],
#     [6, 7, 3, 0],
#     [4, 5, 9, 1]]
# res = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]

# for i in range(len(matrix1)):
#     for j in range(len(matrix2[0])):
#         for k in range(len(matrix2)):
#             res[i][j] +=matrix1[i][k]*matrix2[k][j]

# print(res)
# in2 = 153
# a = str(in2)
# res = 0
# for i in range(len(a)):
#     res+=int(a[i])**3
    
# if in2 == res:
#     print(f'{in2} is an armstrong number')
# else:
#     print(f"{in2} is not an armstrong number")
    
# a =12321
# a = str(a)
# if str(a) == a[::-1]:
#     print(f"{a} is an palindrome")
# else:
#     print(f"{a} is not a palindrome")
    
# result ="This an armstrong number in a string"
# res = result.split(' ')
# print(f"Number of word {len(res)}")
# # print(f"Number of character {len}")
# count = 0
# for i in range(len(result)):
#     if " "!=result[i]:
#         count+=1
# print(f"Number of character {count}")

# n = 5
# for i in range(2,n):
#     if n%i==0:
#         print(f"{n} is not a prime number")
#         break
# else:
#     print(f"{n} is an prime number")
    
# num = 10
# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-2) + fib(n-1)
    
# for i in range(num):
#     print(fib(i))
    
# a ="listen"
# b ="silent"

# if sorted(a) == sorted(b):
#     print("a and b are anagram")
# else:
#     print("a and b is not an anagram")
    
# a = "siva"
# b = "raj"

# a,b=b,a
# print(f"a is {a}")
# print(f"b is {b}")

# a = [3,4,5,4,2,4,3,3,3]
# res = {}
# for i in range(len(a)):
#     if a[i] in res:
#         continue
#     else:
#         res[a[i]] = a.count(a[i])
        
# max_count = max(zip(res.values(),res.keys()))[1]
# print(max_count)


# a = "the quick brown fox jumPs over the lazY dog"
# r= a.split(" ")

# for i in range(len(r)):
#     r[i] = r[i].lower()
   
# res = sorted(r)
# print(" ".join(res))

# a = "the quick brown fox jumPs over the lazY dog"

# res = {}
# for i in range(len(a)):
#     if " "== a[i]:
#         continue
#     elif a[i] in res:
#         continue
#     else:
#         res[a[i]] = a.count(a[i])

# print(res)

# num = 10
# n1= 0
# n2 = 1

# print(f"{n1},{n2}",end=',')
# for i in range(0,num):
#     n3 = n1+n2
#     print(n3,end=",")
#     n1 = n2
#     n2 = n3


# n = 100
# for i in range(2,n):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(f"{i} is an prime number")    
        
# print("LCM")
# a = 120
# b = 140
# for i in range(1,a+1):
#     if a%i == 0 and b%i == 0:
#         c=i
        
# res = (a*b)/c
# print(f"lcm of {a} and {b} is {res} and gcd is {c}")


 
# # driver code
# A = [ [1, 1, 1],
#  [2, 2, 2],
#  [3, 3, 3]]
 
 
# # To store result
# B = [[0 for i in range(len(A))] for j in range(len(A[0]))]

# for i in range(len(A[0])):
#   for j in range(len(A)):
#     B[i][j] = A[j][i]
    
# print(B)


# a = 220
# b = 284
# res1 = []
# for i in range(1,a):
#     if a%i==0:
#         res1.append(i)
        
# res2 = []
# for i in range(1,b):
#     if b%i==0:
#         res2.append(i)

# if a==sum(res2) and b == sum(res1):
#     print(f"{a} and {b} are an ambical number")
# else:
#     print(f"{a} and {b} are not an ambical number")

# # p = int(input("ENter your principal"))
# # rate = float(input("Enter your rate"))
# # time = int(input("Enter your time"))

# # si = (p* rate * time)/100
# # amount = p* (pow((1 + rate / 100), time))
# # ci = amount - p
# # print(si,ci)

# n = 100
# res = []
# for i in range(1,n+1):
#     if n%i == 0:
#         res.append(i)

# print(res)

# import itertools

# string = "abc"
# for i in range(len(string)):
#     for subset in itertools.combinations(string, i+1):
#         print(''.join(subset))

a=[11,42,43,36,67,14]
res = {}

for i in range(len(a)):
    res[a[i]] = 0
    for j in range(i,len(a)):
        if a[i] < a[j]:
            res[a[i]] = res[a[i]]+1

for a,b in res.items():
    print(f"{a}:{b}")
    
a=[1,2,3,4,5]
for i in range(len(a)):
    if i==0:
        continue
    elif a[i]<a[i-1]:
        print("It is not a a sequemce")
        break
    elif a[i] == a[i-1] +a[i-2]:
        print("It is not an a sequence")
        break
else:
    print("it is an a sequence")
