def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1.00
    else:
        return base * recurPower(base, exp - 1)


print recurPower(3, 0) == 1.00
print recurPower(3, 3) == 27
print recurPower(5, 2) == 25
print recurPower(11, 2) == 121
