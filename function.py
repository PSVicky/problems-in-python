# # # def my_function(**name):
# # #     print(type(name))
    
# # # my_function('Siva','Vicky')
# # # my_function()

# # # .format is method used to print the keys and values using for loop
# # def fact(n):
# #     if n ==0 :return 1
# #     return n*fact(n-1)
    
# # n = int(input('Enter a number'))
# # print(fact(n))

# class name:
#     # def __init__(self):
#         # print("a")
#         # self.a = None
#         # self.b = None
#         # self.c = None
#     def add(a,b,c):
#         if a!=None and self.b!=None and self.c!=None:
#             print(a+b+c)
#         elif self.a!=None and self.b!=None:
#             print(a+b)
#         else:
#             print(a)

# obs = name()
# print(obs.add(3,4))

class rent:
    def __init__(self,car,cost):
        self.car = car
        self.cost = cost
    
    
class total:
    def __init__(self,days):
        self.days = days
    def __mul__(self,other):
        return other.cost *self.days
        
obj1 = rent("Mustang",5000)
obj2 = total(30)
print(obj1.cost * obj2.days)


