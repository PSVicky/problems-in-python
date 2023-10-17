# import math


# print('{} It the wonderfull {}'.format("Hello","World"))

# a = 10
# b = 20
# c = a+b
# print(c)

# # square root number

# num = int(input("enter your number"))
# res = math.sqrt(num)
# print(res)
# res = num ** (1/2)
# print(res)

# b = int(input('Enter the triangle breadth'))
# l = int(input('Enter the triangle length'))
# res = (1/2)*b*l
# print(res)

# # swap two varibles

# a = 10
# b = 20
# a,b = b,a
# print(a,b)


# # kilo meter to miles

# kilometer = int(input('Enter the killometers'))
# miles = kilometer*1000
# print(f'{kilometer} kilometer is equal to {miles}miles')

# # celcius to fahrenhiet

# c = int(input('Enter your Celsius'))
# f = c *(9/5)+32
# print(f'{c} celsius is equal to {f} fahrehiet')

# # find the given number is a positive or even number
# n = int(input('enter a number'))
# if n==0:
#     print(f"{n} is an zero")
# elif n>0:
#     print(f'{n} is a positive number')
# else:
#     print(f'{n} is an negative7 number')
    
# # find the give number is odd or even
# if n%2==0:
#     print(f"{n} is an even number")
# else:
#     print(f'{n} is an odd number')

# n = 5

# def fac(n):
#     if n==0:
#         return 1
#     else:
#         return n*fac(n-1)
# print(fac(n))

# #fibonacci number
# n = 10
# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-2)+fib(n-1)


# for i in range(n+1):
#     print(fib(i))
    
# # find the maximum number
# a = int(input())
# b = int(input())
# c = int(input())
# res = sort[a,b,c]
# print(res[-1])

# #  leap year check
# year = int(input("Enter the year"))

# if year%400==0 and year%100!=0:
#     print(f"{year} is a leap year")
# elif year%4 ==0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# # check the give number is prime number or not
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

# table = int(input("enter a table number you want to display"))
# for i in range(1,11):
#     print(f'{i} X {table} = {i*table}')
    

# # quadratic equation

# a = 20
# res = a**2 + a +5
# print(res)

a = 10%100000
print(a)