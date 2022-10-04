def cree():
    return []

def cle(d, k):
    for (cle, valeur) in d :
        if cle == k :
            return True
    return False 
    
def lit(d, k):
    for (cle, valeur) in d :
        if cle == k :
            return valeur 
    return None

def ecrit(d, k, v):
    for i in range(len(d)) :
        if d[i][0]:
            d[i] = (k, v)
            return
    d.append((k,v))

def main(d, k, v):
    cree()
    cle(d, k)
    lit(d, k)
    ecrit(d, k, v)
    print(d)

main([("e", 3),("A", 6)], 3, "B") 