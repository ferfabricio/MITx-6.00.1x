import math

def polysum(n, s):
    '''
    n: number of sides
    s: side length
    '''
    perimeter = (n*s)**2
    area = (0.25 * n * (s**2)) / math.tan(math.pi/n)
    return round(perimeter + area, 4)

print polysum(59,46) == 7951393.3494
print polysum(95, 13) == 1646554.3017
print polysum(2, 59) == 13924.0
print polysum(23, 33) == 621638.6146
