# matrix = [[ 0 for i in range(3)] for j in range(3)]

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         matrix[i][j] = int(input(f"Enter a number in {i},{j}"))

# diagonal1 = 0
# diagonal2 = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if i==j:
#             diagonal1 +=matrix[i][j]
#         elif ((i+j) == (n-1)):
#             diagonal2+=matrix[i][j]
        
        
# print(matrix)           
# print(diagonal1)
# print(diagonal12)


a = str(234)

i = 0
res = 0
while i < len(str(a)):
    res+=int(a[i])
    i+=1
print(res)