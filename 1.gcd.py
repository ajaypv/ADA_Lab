def gcdc(m,n):
    t = min(m,n)
    while t >0:
        if m%t ==0 and n%t==0 :
            return t
        t = t-1
print(gcdc(6,9))

def gcde(m,n):
    if m<n:
        (m,n)= (n,m)
        while n!=0 :
            r =m%n
            m=n
            n=r
        return m
print(gcde(6,9))