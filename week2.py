str3 = "Hello Qantler"

res = {
    'a': '@',
    'e': '$',
    'i': '&',
    'o': '%',
    'u': '#',
}
result = ""
for i in range(len(str3)):
    if 'a' == str3[i] or 'e' == str3[i] or 'i' == str3[i] or 'o' == str3[i] or 'u' == str3[i]:
        result += res[str3[i]]
    else:
        result += str3[i]

print(result)

n = 5
for i in range(n):
    print("* "*(i))

for i in range(n, 0, -1):
    print(" "*(n-i)+"* "*(i))

input = 'I am an Indian'
print(input[::-1])

a = [2,3,4,5,6,7]
target = 10
res = {}
list2 = []
for i in range(n):
    sub_tar = target - a[i]
    if sub_tar in res:
        list2.append((sub_tar, a[i]))
    else:
        res[a[i]] = sub_tar

print(list2)

result = 'malayalam'
if result == result[::-1]:
    print(f"{result} is an palindromic string")
else:
    print(f'{res} is not a palindromic number')


