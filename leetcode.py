# nums = [8,8,7,7,7]
# start = 0
# end = len(nums)-1
# max_len = len(nums)
# map_func = {}
# for i in range(len(nums)):
#     if nums[i] in map_func:
#         continue    
#     else:
#         map_func[nums[i]] = nums.count(nums[i])
# print(map_func)

# maximum = max(zip(map_func.values(),map_func.keys()))[1]
# print(maximum)
# a = True
# while a:
    
#     if nums[0] != maximum:
#         nums.pop(0)    
#     elif nums[-1]!=maximum:
#         nums.pop()
#     else:
#         a= False
    
# print(len(nums))

n=11**5
print(n)