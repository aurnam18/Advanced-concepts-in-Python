#map function
#returns a map object (iterator) of the results after applying the given function
#to each item of a given iterable (list, tuple etc.)
#syntax: map(fun, iter)
#fun : It is a function to which map passes each element of given iterable
#iter : It is a iterable which is to be mapped
# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Double all numbers using map and lambda
# Going through each number in numbers
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test) 
