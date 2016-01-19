s = 'azcbobobegghakl'
counter = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        counter += 1
print 'Number of times bob occurs is: ' + str(counter)
