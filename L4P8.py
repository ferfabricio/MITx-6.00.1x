def square(x):
    '''
    x: int or float.
    '''
    return x * x

def fourthPower(x):
    return square(square(x))

print fourthPower(3)
print fourthPower(7)
