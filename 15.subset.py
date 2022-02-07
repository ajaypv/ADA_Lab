def ss(set,n,sum):
    if sum ==0:
        return True
    elif n==0 and sum !=0:
        return False
    elif set[n-1] > sum :
        return ss(set,n-1,sum)
    return ss(set,n-1,sum) or ss(set,n-1,sum-set[n-1])

set  =[3,34,4,15,5,2]
sum =9
n = len(set)
if(ss(set,n,sum)==True):
    print('found a subsert with given sum')
else:
    print('No subset with given sum')
    