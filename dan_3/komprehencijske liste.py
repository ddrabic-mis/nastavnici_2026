A=[0]*10 # lista od 10 nula
print(f"{A=}" )
# komprehencijska lista
B=[ 0 for i in range(10) ]
print(f"{B=}" )

# kreirajmo listu koja sadrži kvadrate brojeva od 1 do 9
K=[ i**2 for i in range(1,10) ]
print(f"{K=}" )
# kreirajmo listu koja sadrži kvadrate brojeva od 1 do 9 koji nisu parni
K=[ i**2 for i in range(1,10) if i**2%2 ]