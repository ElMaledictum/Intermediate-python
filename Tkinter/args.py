

def add(*args):
    return sum(args)

def multiply(*args):
    product = 1
    for i in args:
        product *= i
    return product

print (add(5,5,5,44,4,5,45,4,5,45,4,5,22,2,2,3))


def calculate(*args, **kwargs):
    return (kwargs["func"](*args))



print (calculate(10, 3, func=multiply))

