import math
n = int(input("enter a n value"))
arr = [i for i in range(n+1)]
print(arr)
s = int(math.sqrt(n))+1
for i in range(2,s):
    if (arr[i] !=0):
        j = i*i 
        while( j<=n):
            arr[j]=0
            j=j+i
print(arr)