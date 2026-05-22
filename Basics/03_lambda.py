# Lambda functions
l= [1,2,3,4,5,6,7,8,9]

listcube = lambda x: x**3
print(listcube(l[4]))

# add10togivenlist = list(map(lambda x : x*10, l))
# print(add10togivenlist)

#filter

# myfileter = list(filter(lambda x: x>9,list(map(lambda x:x**3 , l))))
# print((myfileter))

#reduce

# from functools import reduce

# def mysum(x,y):
#     return x+y

# # print(reduce(mysum,l))
# print(reduce(lambda x,y:x+y, l))



