# class CountDown:
#     def __init__(self, start):
#         self.current = start

#     def __iter__(self):
#         return self   # An iterator must return itself

#     def __next__(self):
#         if self.current <= 0:
#             raise StopIteration   # End of iteration
#         value = self.current
#         self.current -= 1
#         return value

# # Usage
# cd = CountDown(5)
# for num in cd:
#     print(num)
import time
class countDown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= 0 :
            raise StopIteration  # It will stop the iteration
        value = self.current
        self.current -= 1 # IT will calculate the next countdown value
        return value
    
cd = countDown(5)
for i in cd : 
    time.sleep(1)
    print(i)