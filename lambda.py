x = lambda a : a * 10
print(x(4))

def lambda_func(b):
    return lambda x : x / b
func = lambda_func(5)
print(func(10))

def lambda_2(c):
    return lambda y : y ** c
func2 = lambda_2(5)
print(func2(434))
