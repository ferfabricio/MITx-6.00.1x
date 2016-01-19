s = 'azcbobobegghakl'
counter = 0
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        counter += 1
print 'Number of vowels: ' + str(counter)
