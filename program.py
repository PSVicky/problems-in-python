# # # a = "hello world"
# # # print(a.split(" "))
# # # print(a[2:5:1])
# # # print(a[-2:-5:-1])
# # # print(a[::-1])
# # # print(a[-3:-1])
# # # for i in range(len(a)):
# # #     print(a[i])
# # # print(a[2:-2])
# # # print(a[:-3:-1])

# # # slice method
# # """
# #  list can hve index or mutable and ordered and duplicate
# #  tuple can have index are imutable are duplicate
# #  index or immutable  and no index
# #  dict ordered mutable keys and value
# # """
# # # a = [1,2,3,4,5]
# # # s = 9
# # # for i in range(len(a)):
# # #     for j in range(i+1,len(a)):
# # #         m = sum(a[i:j+1])
# # #         if m == s:
# # #             print(i,j)

# # # S = "aaaabbaa"
# # total = 0
# # # num =12
# # num = int(input())
# # while num !=0:
# #     total += num
# #     num = int(input())       
    
# # print(total)


# n = 5
# # for i in range(0,n+1):
# #     print(' '*(n-i)+'* '*(i))
# # for j in range(n-1,0,-1):
# #     print(' '*(n-j)+"* "*(j))

# # pyramid pattern

# # for i in range(0,n+1):
# #     for j in range(n-i):
# #         print(end=' ')
# #     for k in range(i):
# #         print("* ",end='')
# #     print('\n')

# # for i in range(0,n+1):
# #     for j in range(i):
# #         if j==i-1 or j==0 or i==n:
# #             print("* ",end='')
# #         else:
# #             print(" ",end=" ")
# #     print("\r")
    
# # for i in range(n):
# #     for j in range(n-i):
# #         print(' ',end=' ')
# #     for k in range(2*i+1):
# #         if k==0 or k==2*i or i==n-1:
# #             print(i,end=' ')
# #         else:
# #             print(' ',end=' ')
# #     print("\r")

# # n = 50
# # for i in range(0,n+1,2):
# #     print(i)
    
# # for i in range(0,n+1):
# #     if i%2 == 0:
# #         print(i)
        

# n = 6
# result = 1
# for i in range(1,n+1):
#     result*=i
# print(result)

# n = 153
# num = str(n)
# result =0
# for i in range(len(num)):
#     result += int(num[i])**3

# if n==result:
#     print(f'the {num} is armstrong number')
# else:
#     print(f"This {num} is not a amrmstrong number")
    
# year = int(input("Enter your year"))

# if year%400==0 and year%100!=0:
#     print(f'{year} is leap year')
# elif year%4==0 :
#     print(f'{year} is leap year')
# else:
#     print(f'{year} is not a leap year')
    
# n= 8
# for i in range(2,n):
#     if n%i == 0:
#         print(f'{n} is not a prime number')
#         break
# else:
#     print(f'{n} is a prime number')
    
# n =100
# for i in range(2,100):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)
        
# n = 10
# def fibnoic(n):
#     if n == 0:
#         return 0
#     elif n ==1:
#         return 1
#     else:
#         return fibnoic(n-2) + fibnoic(n-1)

# for i in range(n):
#     print(fibnoic(i))
    
    
a = 10
b = 20
a+=b
print(a)
a-=b
print(a)
a = 10
b = 0
print(bool(a and b))
print(bool(a or b))
print(a and b)
print( a or b)

