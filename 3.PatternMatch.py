def search(text,pattern):
    n = len(text)
    m = len(pattern)
    s = n-m+1
    for i in range(s):
        j=0
        while j<m:
            if pattern[j] != text[j+i]:
                break
            j+=1
        if j ==m:
            print('the pattern was found at ',i)

t = input('enter a text')
p = input('entera a text')

search(t,p)