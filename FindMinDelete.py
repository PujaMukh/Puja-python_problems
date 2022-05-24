#given an array, find min no of ele to be deleted so that any corresponding numbers are even
#corresponding will be even only if both are even or both are odd

A=[1,2,3,4,5]
even=0
odd=0
ans=0
if len(A)==1:
    print(0)
else:
    for i in range(0, len(A)):
        if A[i]%2==0:
            even=even+1
        else:
            odd=odd+1
    if even<odd:
        print(even)
    else:
        print(odd)
