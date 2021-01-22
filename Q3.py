#from array import *


def max_repeted(a):
    count = 0
    ans = 0
    for i in range(0,len(a)):
        if (a[i]==0):
            count=0
        else:
            count+=1
            ans = max(ans,count)
    return ans



a = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]


print(max_repeted(a))
