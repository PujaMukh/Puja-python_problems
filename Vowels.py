#return a string containing all vowels from the given string
A="abcdye"

S=""
for i in range(0, len(A)):
    if A[i]=='a' or A[i]=='e' or A[i]=='i' or A[i]=='o' or A[i]=='u':
        S=S+A[i]
print(S)