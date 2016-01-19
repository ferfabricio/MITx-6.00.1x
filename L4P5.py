def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return min(x, lo) == x and lo or (max(x, hi) == x and hi or x)

print clip(-4.01, 2.25, 9.29)
print clip(-4.01, 2.25, 9.29) == 2.25
print clip(-0.29, 0.84, 0.18)
print clip(-0.29, 0.84, 0.18) == 0.18
print clip(-5.62, 5.14, 5.23)
print clip(-5.62, 5.14, 5.23) == 5.14
