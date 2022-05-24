A=[1,2,44,3]
max=0

A.sort()
for i in range(0,len(A)-1):
    for j in range(i,len(A)):
        if A[j]!=0:
            ans=A[i]%A[j]
            if ans>max:
                max=ans
print(max)