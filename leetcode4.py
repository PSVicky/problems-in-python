# # x = 2.10000
# # parts = str(x).split(".")

# # # Check if there is a decimal part
# # if len(parts) > 1:
# #     decimal_part = parts[1]
    
# #     # Count the length of the decimal part, including trailing zeros
# #     lenght =  len(decimal_part)
# # else:
# #     lenght = 0
# # n = 3
# # if n == 0:
# #     print(1)
# # elif n ==1:
# #     print(n)
# # elif n >1:
# #     res = x**n
# #     print(f"{res:.{lenght}f}")
# # else:
# #     res = (x**abs(n))
# #     print(res)
# #     result = 1/res
# #     print(f'{result:.{lenght}f}')
# # strs = ["eat","tea","tan","ate","nat","bat"]

# # result= []
# # maping ={}
# # for i in range(len(strs)): 
    
# #     if "".join(sorted(strs[i])) in maping:
# #         maping["".join(sorted(strs[i]))].append(strs[i])
# #     else:
# #         maping["".join(sorted(strs[i]))]=[strs[i]]
        
# # for i in maping.values():
# #     result.append(i)
# # print(result)

# # nums =[3,2,1,0,4]
# # i = 1
# # j = len(nums)
# # while i <= len(nums):
# #     if i == len(nums)-1:
# #         print(True)
# #         break
# #     elif nums[i]==0:
# #         print(False)
# #         break
# #     i += nums[i]        
# # else:
# #     print(False)

# # # num = [1,2,0,0]
# # # k = 34
# # # a= ""
# # # for i in num:
# # #     a+=str(i)

# # # res = int(a)


# # # 

# # head = [1,2,3,3,4,4,5]
# # from collections import Counter

# # maping = Counter(head)

# # res = []
# # for i in maping:
# #     if maping[i] ==1:
# #         res.append(i)
# #     else:
# #         continue
# # print(res)
    
# # nums = [3,6,9,1]
# # nums=sorted(nums)
# # i =0
# # j =1
# # res = 0
# # while j<len(nums) and i!=j:
# #     res = max(res,abs(nums[j]-nums[i]))
# #     i+=1
# #     j+=1

# # print(res)

# # numerator = 1
# # denominator = 2
# # a = str(numerator/denominator)
# # print(type(a))
# # words = ["cool","lock","cook"]
# # maping = []

# # for i in words[0]:
# #     result = 1
# #     for j in range(1,len(words)):
# #         if i in words[j]:
# #             result+=1
# #             res = list(words[j])
# #             res.remove(i)
# #             words[j] = "".join(res)
# #     if result == len(words):
# #         maping.append(i)
# # print(maping)

# # s = "azxxzy"
# # lis=[s[0]]
# # for i in range(1,len(s)):
# #     if len(lis)==0 or lis[len(lis)-1]!=s[i]:
# #         lis.append(s[i])
# #     else:
# #         lis=lis[:len(lis)-1]        
# # s="".join(lis)


# # print(s)
# # stones = [2,7,4,1,8,1]

# # new = sorted(stones)
# # for i in range(1,len(new)):
# #     if len(new)==1:
# #         break
# #     if new[-1]== new[-2]:
# #         new.remove(new[-2])
        
# #         new[-1]=0
# #     elif new[-1]!=new[-2]:
# #         res = abs(new[-1]-new[-2])
# #         new.remove(new[-2])
# #         new[-1] = res
# #         new.sort()
    
# # print(new)
# # heights = [1,2,3,4,5]

# # res = 0

# # maping = sorted(heights)

# # for i in range(len(heights)):
# #     if heights[i]!=maping[i]:
# #         res+=1
# #     else:
# #         continue 
# # print(res) 
# arr1 = [28,6,22,8,44,17]
# arr2 = [22,28,8,6]
# res = []
# for i in range(len(arr2)):
#     while arr2[i] in arr1:
#         res.append(arr2[i])
#         arr1.remove(arr2[i])
# if arr1:
#     res+=arr1        
# print(res)
# arr = [1,0,2,3,0,4,5,0]
# lenght = len(arr)
# i = 0
# while i < lenght:
#     if arr[i]==0:
#         arr.insert(i+1,0)
#         i+=2
#     else:
#         i+=1
# print(arr[:lenght]) 

candies = 7
result = candies
num_people = 4
res = [1]
i = 2
while i <= candies+2:
    candies-=i
    res.append(i)
    i+=1
print(res)