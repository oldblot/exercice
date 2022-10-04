#---EXERCICE1---#

def cree():
    return []

def contient(s, x):
    return x in s

def ajout(s, x):
    s.append(x)

#---EXERCICE2---#

def cree():
    return [0]

def contient(s, x):
    return s[0] & (1 << x) != 0 

def ajout(s, x):
    return s[0] | (1 << x)

#---EXERCICE3---#

def enumeres(s):
    tab = []
    for entier in s :
        for bit in range(64):
            if entier & (1 << bit) != 0 :
                tab.append(entier*64+bit)
        return tab

#---EXERCICE4---#

#1)

def union(s1, s2):
    tab = s1[:]
    for x in s2:
        if x not in s1 :
            tab.append(x)
    return tab

def intersection(s1, s2):
    L = []
    for x in s2:
        if x in s1 :
            L.append(x)
    return L

#2)

def union(s1, s2):
    tab = []
    for i in range(6) :
        tab.append(s1[i] | s2[i])
    return tab

def intersection(s1, s2):
    L = []
    for i in range(6):
        L.append(s1[i] & s2[i])
    return L




    
