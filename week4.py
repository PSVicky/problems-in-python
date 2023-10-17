# # # a = [2,5,6,1,7,8]

# # # maximum = 0
# # # for i in a:
# # #     if maximum > i:
# # #         continue
# # #     else:
# # #         maximum = i
# # # print(i)

# # # a = ["2","3","4","5","6","7","2","3","2"]
# # # res = []
# # # for i in range(len(a)):
# # #     if a[i] in res:
# # #         print(a[i])
# # #     else:
# # #         res.append(a[i])

# # a = [1,2,3,4,5]
# # b = [2,3,4,5]

# # for i in range(len(a)):
# #     if a[i] in b:
# #         continue
# #     else:
# #         print(a[i])
        
# # a = [2,3,4,5,6,7,8]
# # max = 0
# # min = a[0]
# # for i in a:
# #     if max < i:
# #          max = i
# #     elif min>i:
# #          min = i
# #     else:
# #         continue
# # print(max)
# # print(min)

# def func(a,b,c):
#     res = [a,b,c]
#     res.sort()
#     return res[-1]
def total(res):
    if len(res)==1:
        return res[0]
    else:
        return res[0] +total(res[1:])
print(total([1,2,3,4,5]))
def fac(res):
    if len(res) ==1:
        return res[0]
    else:
        return res[0]* fac(res[1:])
print(fac([1,2,3,4,5]))
# arr = [1,2,3,4,5,-7]
# print(f"multiplication of the number : {fac(arr)}")
# print(f"maximuum number :{func(34,24,12)}")
# print(f"total of array :{total([8,2,3,0,7])}")

def factorial(num):
    if num ==1:
        return 1
    else:
        return num *factorial(num-1)
print(factorial(5))


# def happu_number(n):
#     past = set()
#     while n!=1:
#         n =  sum(int(i)**2 for i in str(n))
#         if n in past:
#             return "It is not a happy number"
#         past.add(n)
#     return "It is a happy number"

# print(happu_number(34))

# ans = []
# n= 5
# for i in range(n):
#     ans.append([1]*(i+1))
    
# for i in range(2,n):
#     for j in range(1,len(ans[i])-1):
#         ans[i][j] = ans[i-1][j-1]+ans[i-1][j]
# print(ans)

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
sum = 0
n =654
for i in str(n):
    sum+=fac(int(i))
    
if sum == n:
    print(f'{n} is an strong number')
else:
    print(f"{n} is not a strong number")