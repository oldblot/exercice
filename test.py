
from math import fabs

def fact(n):
    if n == 0 :
        return 1
    elif n > 0 :
        return n * fact(n-1)
    else :
        return "probleme"
#print(fact(13))

def syracuse(un):
    print(un)
    if un > 1 :
        if un % 2 == 0 :
            un1 = un/2
            syracuse(un1)
        else :
            un1 = 3 * un + 1
            syracuse(un1)
    else :
        return 
#syracuse(1456)

def serie(n, a, b):
    if n == 0 :
        return a
    if n == 1 :
        return b
    if n >= 2 :
        return 3*serie(n-1,a,b)+2*serie(n-2,a,b)+5

def boucle(i, k):
    print(i)
    if i == k :
        return
    if i<k :
        boucle(i+1, k)

def pgcd(a, b):
    if b == 0 :
        return a
    else :
        return pgcd(b, a%b)
    
def nb(n):
    if n//10 == 0 :
        return 1
    else :
        return 1+nb(n//10)

def C(n, p):
    if p == 0 or n == p:
        return 1
    else :
        return C(n-1,p-1)+C(n-1,p)
def pascal(n):
    for i in range(n+1):
        for j in range(i+1):
            print(C(i,j), end=" ")
        print()
#pascal(10)

from turtle import forward, left, right
def koch(n, l):
    #if n == 0 :
        #forward(l)
    #else :
        koch(n-1,l/3)
        left(60)
        koch(n-1,l/3)
        right(120)
        koch(n-1,l/3)
        left(60)
        koch(n-1,l/3)
        right(120)
        koch(n-1,l/3)
#koch(3,300)


pgcd(12, 18)









    

