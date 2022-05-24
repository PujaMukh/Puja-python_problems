#break the given string into max possible substrings of equal no of 0's and equal no of 1's

A="011100"
res=0
countZero=0
countOne=0
for i in range(0, len(A)):
    if A[i]=='0':
        countZero=countZero+1
    else:
        countOne=countOne+1
    if countZero==countOne:
        res=res+1
        countZero=0
        countOne=0

print(res)
