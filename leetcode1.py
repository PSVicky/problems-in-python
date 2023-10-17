


# # # # def pivot():
# # # #     nums =[2,1,-1]
# # # #     i = 0
# # # #     j = 0
# # # #     while i <len(nums):
# # # #         if i==0:
# # # #             if 0==sum(nums[1:]):
# # # #                 return i
# # # #         else:
# # # #             if sum(nums[:i]) == sum(nums[i+1:]):
# # # #                 return i
# # # #         i+=1
# # # #     return -1

# # # # print(pivot())


# # # # left = 66
# # # # right = 708
# # # # res = []
# # # # for i in range(left,right):
    
# # # #     k = str(i)
# # # #     if  "0" in k :
# # # #         continue
# # # #     for j in k:
# # # #         if i%int(j) !=0:
# # # #             break
# # # #     else:
# # # #         res.append(i)

# # # # print(res)
# # # # nums = [3,6,1,0]

# # # # a = sorted(nums)
# # # # if a[-1] >= a[-2]*2:
# # # #     print(nums.index(a[-1]))


# # # # nums = [1,2,3]
# # # # def subsets(nums):
# # # #         """
# # # #         :type nums: List[int]
# # # #         :rtype: List[List[int]]
# # # #         """
# # # #         def dfs(depth, start, valuelist):
# # # #             res.append(valuelist)
# # # #             if depth == len(nums): return
# # # #             for i in range(start, len(nums)):
# # # #                 dfs(depth+1, i+1, valuelist+[nums[i]])
# # # #         nums.sort()
# # # #         res = []
# # # #         dfs(0, 0, [])
# # # #         return res

# # # # print(subsets(nums))
# # # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# # # word = "ABCB"
# # # res = list(word)
# # # print(res)
# # # print(board)

# # # found = False

# # # for i in range(len(word)):
# # #     for j in range(len(board)):
# # #         if word[i] in board[j]:
# # #             res.remove(word[i])
# # #             board[j].remove(word[i])
# # #             found = True
# # #             break

# # #     if not found:
# # #         break

# # # if not res:
# # #     print(True)
# # # else:
# # #     print(False)

# # s = "abcdddeeeeaabbbcd"
# # i = 0
# # j = 1
# # res = []
# # while i < len(s) and j< len(s):
# #     result = []
# #     if s[i] == s[j]:
# #         while s[i]!=s[j]:
# #             i=j
# #             j+=1
# #             result.append(j)
# #             res.append(result)
# #         else:
# #             result.append(i)
# #             j+=1
# #     i+=1
# #     j+=1
# # print(res)

# matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,3]]

# def diagonal(row,col):
#     val = matrix[row][col]
#     while row < len(matrix) and col < len(matrix[0]):
#         if matrix[row][col] != val:
#             return False
#         row+=1
#         col+=1
#     return True

# for col in range(len(matrix[0])):
#     if not diagonal(0,col):
#         print(False)
#         break
# # for row in range(len(matrix)):
# #         if not diagonal(row,0):
# #             print(False)
# # else:
# #     print(True)

# s = "abcde"
# goal = "cedab"
# a = list(s)
# a.append(a[0])
# a.remove(a[0])

# i = 0
# print(a)
# res = ""
# while i < len(s) and res != s:
#     if res == goal:
#         print(True)
#         break
#     a.append(a[0])
#     a.remove(a[0])
#     res = "".join(a)
#     i+=1
# else:
#     print(False)

# find the maximum occurenece of the array except the banned element

# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# # paragraph = paragraph.translate(str.maketrans('', '', ',.\'\"'))

# # res = re.split(r'\W+', paragraph.lower())
# banned = ["hit"]

# res = paragraph.split(" ")

# result =list(map(lambda x:x.lower(),res))
# maping = {}

# for i in result:
#     if i not in maping and i not in banned:
#         maping[i] = 1
#     elif i in maping and i not in banned:
#         maping[i]+=1

# maximum = max(zip(maping.values(),maping.keys()))[1]
# print(maximum)        
        
# s = "loveleetcode"
# c = "e"
# res = []

# for i in range(len(s)):
#     if s[i] ==c:
#         res.append(i)
# result = []
# for i in range(len(s)):
#     minimum = len(s)
#     for j in res:
#         maping = abs(i - j)
#         minimum = min(minimum,maping)
#     result.append(minimum)
# print(result)

# image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# res = []
# for i in image:
#     dummy = i[::-1]
#     j = 0
#     while j < len(dummy):  
#         if dummy[j] ==0:
#             dummy[j]=1
#         else:
#             dummy[j]=0
#         j+=1
#     res.append(dummy)
# print(res)

# for i in range(len(image)):
#     dummy = image[i][::-1]
#     j = 0 
#     while j <len(dummy):
#         if dummy[j]==0:
#             dummy[j]=1
#         else:
#             dummy[j]=0
#         j+=1
#     image[i] = dummy
# print(image)

# def sorting(a):
#     for i in range(len(a)-1):
#         for j in range(i+1,len(a)):
#             if a[i] > a[j]:
#                 a[i],a[j] = a[j],a[i]
#     return a
# res = []
# while True:
#     a = input("Enter Your number")
#     if a == "q":
#         break
#     else:
#         res.append(int(a))
        
# print(sorting(res))


# def duplicate(a,index1 = 0):
#     if index1 == len(a)-1:
#         return a
#     current = a[index1]
#     if current in a[index1+1:]:
#         a = [n for n in a if current !=n]
#     return duplicate(a,index1+1)
    
# a = [1,2,1,3,4,5,5]
# print(duplicate(a))
# bills = [5,5,10,10,20]


# total_cost = 0
# for i in range(len(bills)):
#     if bills[i] == 5:
#         total_cost+=bills[i]
#     else:
#         res = 0
#         mo = bills[i]
#         while mo > 5:
#             res+=1
#             mo-=1
#         dummy = bills[i] - res
#         total_cost-=res
#         if i < len(bills)-1:
#             total_cost+=dummy
# if total_cost >= 0:
#     print(True)
# else:
#     print(False)        

# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# res = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         res[j][i] = matrix[i][j]
        
# print(res)

# nums = [3,1,2,10,1]


# res = []
# for i in range(len(nums)):
#     if i == 0:
#         res.append(nums[i])
#     elif i == len(nums)-1:
#         res.append(sum(nums))
#     else:
#         dummy = sum(nums[:i+1])
#         res.append(dummy)
# print(res)
        
# Function to convert decimal number
# to binary using recursion

# n = 22

# def binaryDigit(n):
#     res = ""
#     if n >=1:
#         binaryDigit(n//2)
#     res+=str(n%2)
    

# print(binaryDigit(n))

# res = "sum"
# a = "vicky"
# res+=a
# print(res)

# from Collection import Counter
# import Counter
# s1 = "this apple is sweet"
# s2 = "this apple is sour"

# a = s1.split() +s2.split()
# res = []
# for i in a:
#     if a.count(i) ==1:
#         res.append(i)
#     else:
#         continue
# print(res)

# nums = [1,2,4,3]

# i = 0
# j = 1
# if nums[i]<nums[j]:
#     while i < len(nums) and i<=j:
#         if nums[i] > nums[j]:
#             print(False)
#             break
#         elif j == len(nums)-1:
#             print(True)
#             i+=1
#         else:
#             i+=1
#             j+=1


# nums = [3,1,2,4]
# # res = sorted(nums)
# for i in range(len(nums)):
#     if nums[i]%2==0:
#         a = nums[i]
#         nums.remove(a)
#         nums.insert(0,a)
# print(nums)

# deck = [1,1,2,2,2,2,1]
# res = {}
# for i in deck:
#     if deck.count(i)%2!=0:
#         print(False)
#         break
# print(True)

# s = "Test1ng-Leet=code-Q!"
# s = [i for i in s]
# print(s)
# i = 0
# j = len(s)-1

# while i < len(s) and i < j:
#     if (not s[i].isalpha()) and (not s[j].isalpha()):
#         i+=1
#         j-=1
#     elif not s[i].isalpha():
#         i+=1
#     elif not s[j].isalpha():
#         j-=1
#     else:
#         s[i],s[j] = s[j],s[i]
#         i+=1
#         j-=1
# print(s)

# nums =[3,4]
# i = 0
# j = 1
# print(nums[0]%2!=0)
# while i <= len(nums) and j<= len(nums):
#     if nums[0]%2!=0:
#         while j <len(nums):
#             if nums[j]%2 == 0:
#                 nums[0],nums[j] = nums[j],nums[0]
#                 j+=1
#                 i=j
#                 break
#             elif nums[j]%2!=0:
#                 j+=1
            
#     elif nums[i]%2==0 and nums[j]%2==0:
#         nums[j],nums[j+1] = nums[j+1],nums[j]
#         j+=1
#         i=j
#     i+=1
#     j+=1
    
# print(nums)

name = "rick"
typed = "kric"

for i in name:
    if name.count(i) > typed.count(i):
        print(False)
        break
else:
    print(True)
         