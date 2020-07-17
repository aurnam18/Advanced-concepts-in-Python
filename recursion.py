#Write a Python program to calculate the sum of a list of numbers.
def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])

print(list_sum([2, 4, 5, 6, 7]))

#Factorial with recursion
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

#4 * 3 * 2 * 1

#Write a Python program to multiply a list of numbers
def list_product(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] * list_product(num_list[1:])

print(list_product([2, 4, 6]))
