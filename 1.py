'''print(1+1)'''

'''def is_odd(n):
    return n%2 ==1
    
print(list(filter(is_odd,[1,2,3,4,5,6,9,10,15])))'''


'''def not_empty(s):
    return s and s.strip()
    
print(list(filter(not_empty,['A','','B',None,'C',' '])))'''


'''def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
        
def _not_divisible(n):
    return lambda x:x%n>0
    
def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n 
        it=filter(_not_divisible(n),it)
        
for n in primes():
    if n<1000:
        print(n)
    else:
        break'''
        
        
        
'''def is_palindrome(n):
    n=str(n)
    return n[::]==n[::-1]

    
output=filter(is_palindrome,range(1,1000))
print(list(output))'''

'''output=sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True)
print(output)'''


L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

def by_name(t):
    return t[0].lower()
    
    
L1=sorted(L,key=by_name)
print(L1)

def by_score(t):
    return t[1]
    
L2=sorted(L,key=by_score,reverse=True)
print(L2)