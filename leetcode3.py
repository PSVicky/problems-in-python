from collections import Counter
n =5
i = 0
res = ""
for i in range(n):
    result = ""
    k = 0
    if len(res) == 0:
        res+="1"
    else:
        while k < len(res):
            leng = 0
            j = k
            while j <len(res) and res[k]==res[j] :
                leng+=1
                j+=1
            result += str(f"{str(leng)}{res[k]}")
            k=j
        
        res = result
print(res)

# n = 4

# i = 0
# res = ''
# while i < n:
#     j = i
#     if i == 0:
#         res+="1"

a = [2,3,4,5,7,2,4,8,3,5,6,7,2,3,4,8,9,5,6,7,1,2]
first = 6
second = 8
# indexOfi=[]
# indexOfj=[]
# for i in range(len(a)):
#     if a[i]==first:
#         indexOfi.append(i)
#     elif a[i]==second:
#         indexOfj.append(i)
#     else:
#         continue
# minimum = len(a)

# for i in range(len(indexOfi)):
#     for j in range(len(indexOfj)-1):
#         res = abs(indexOfi[i]-indexOfj[j])
#         minimum = min(res,minimum)

# print(f"the minimum distance between {first} and {second} is :{minimum}")

# i = 0
# j = len(a)-1

# minimum = len(a)
# while i<=j and j>=i:
#     if (a[i] == first or a[i]==second) and (a[j]==first or a[j]==second):
#         res = j-i
#         minimum=min(res,minimum)
#         i+=1
#         j-=1
#     elif (a[i]==first or  a[i]==second ) and (a[j]!=first or a[j]!=second):
#         j-=1
#     elif (a[i]!=first or  a[i]!=second ) and (a[j]==first or a[j]==second):
#         i+=1
#     else:
#         i+=1
#         j-=1

# print(f"The minimum distance between {first} and {second} is: {minimum}")

# nums = [2,3,1,1,4]
# steps = 1
# i = nums[0]
# res = 1
# while i <= len(nums)-2:
#     i += nums[i]
#     res+=1
# print(res)

# nums = [-2,1]
# print(nums[1:1])
# maximum = sum(nums)
# print(maximum)
# for i in range(len(nums)):
#     for j in range(i,len(nums)-1):
#         res = sum(nums[i:j+1])
#         maximum = max(res,maximum)
        
# print(maximum)

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
res = [[0 for i in range(len(matix))] for j in range(len(matrix[0]))]
print(res)