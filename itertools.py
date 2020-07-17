#import the needed modules
import itertools

#for loop, itertools.count
#syntax is: (start of the sequence, steps or difference between consecutive numbers)
#start defaults to 0
#step defaults to 1
for i in itertools.count(5, 5):
   if i == 35:
        break
   else:
        print(i, end =" ") #this will make the numbers formatted in a horizontal line (string)

for x in itertools.count(1, 3):
    if x >= 12:
        break
    else:
        print(x, end =" ")

#itertools.cycle
count = 0

# for in loop, once AB reaches 8 times, the loop breaks
for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i, end = " ")
        count += 1

#itertools.repeat
#syntax: (val, num)
#passed value repeated infinite times if num of times is not specified
print(list(itertools.repeat(1, 7)))
