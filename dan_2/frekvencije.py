'''
Učitaj neki broj N (1<= N <=9999999) te ispiši koliko puta se svaka znamenka pojavila u broju.
ULAZ
123123
IZLAZ
1 - 2
2 - 2
3 - 2
 
ULAZ
123331
IZLAZ
1 - 2
2 - 1
3 - 3
'''
#F=[0,0,0,0,0,0,0,0,0,0]
# indeks u listi mi predstavlja vrijenost znamenke, 
# a vrijednost na tom indeksu koliko puta se ta znamenka pojavila
F=[0]*10
N=input()
for znak in N:
  F[int(znak)]+=1
'''
for broj in range(10):
  print(f"{broj} - {F[broj]}")
'''
for i,v in enumerate(F):
  if v>0:
    print(f"{i} - {v}")