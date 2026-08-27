n=input()
Z=[0]*10 #frekvencijska tablica

znamenka=''
broj_ponavljanja=0
for x in n: 
    Z[int(x)] +=1
    if Z[int(x)]>broj_ponavljanja:
        znamenka=x
        broj_ponavljanja=Z[int(x)]
    elif Z[int(x)]==broj_ponavljanja:
        znamenka=min(znamenka,x)
 
#print(Z.index(max(Z)))
print(znamenka)