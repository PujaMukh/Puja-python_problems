a=[]
n=int(input())

for i in range(0,n):
    l=int(input())
    a.append(l)

for i in range(0,n):
    print(a[i])
for i in range(n-1,-1,-1):
    print(a[i])