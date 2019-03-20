#missing number

a = map(int,raw_input('Enter the Elements : ').split())
l = len(a)
#print a
for i in range(0,l+1):
    if (a[i] != i+1):
        print i+1,"is missing"
        break
        
#repeating number
temp = {}
o = 1
b = map(int,raw_input().split())
for i in range(0,len(b)-1):
    temp[i+1] = 1
for i in range(0,len(b)-1):
    if b[i] == b[i+1]:
        temp[b[i]] = temp[b[i]] + 1
        print b[i],
        
print temp

print 'are repeating'
