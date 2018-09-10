import math
import sys
n=int(input())
k=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
if(k==n):
    print(max(l)-min(l))
    sys.exit()
l.sort()
i=0
minimum=math.inf
count=0
while(i<=n):
    if(count>=k):
        mini=l[i-1]-l[i-k]
        if(minimum > mini ):
            minimum=mini
        i=i+1
    else:
        count=count+1
        i=i+1
print(minimum)