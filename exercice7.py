def tranche(t, i, j):
    tab = []
    if j <= i :
        return
    for n in range(j-i) :
        tab.append(t[i+n])
    return tab

t = [1,2,3,4,5,6]
tranche(t, 1, 3)

def concatenation(t1, t2):
    t3=[]
    for i in range(len(t1)):
        t3.append(t1[i])
    for j in range(len(t1)):
        t3.append(t2[j])
    return t3
