def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 0
    if exp == 0:
        return 1.0
    else:
        result = 1
        while exp > 0:
            result = result * base
            exp -= 1
    return round(result, 4)


print iterPower(5.27, 0) == 1.0000
print iterPower(3.5, 3) == 42.8750
print iterPower(-2.25, 4) == 25.6289
print iterPower(9.18, 10) == 4250370728.5438
print iterPower(-1.77, 4) == 9.8151
