l = [2,4,6,7,9,4,3,5,8,1]
# create a map function to square each element in the list
# print(list(map(lambda x: x**3,l)))

# Filter
# myfileter = list(filter(lambda x: x>9,list(map(lambda x:x**3 , l))))
print(list(filter(lambda x: x>9,list(map(lambda x:x**3 , l)))))

newl = filter(lambda x: x>4,l)


# print(list(newl))

# print currant date and time
from datetime import datetime
nowtime = datetime.strftime("%Y-%m-%d %H:%M:%S")
nowtime = str(nowtime).replace(" ","_")

print(datetime.now())


