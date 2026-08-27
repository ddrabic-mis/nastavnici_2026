N=int(input())
L=dict() # struktura podataka za pohranu bodova - {key=ime :  value=broj bodova}
for i in range(N):
  ime,bod=input().split()
  bod=int(bod)
  L[ime]=L.get(ime, 0) + bod
#print(L.keys())
#print(L.values())
#print(L.items())

# sortiranje po broju bodova (opadajuće) i po imenu (rastuće)
popis=sorted(L.items(), key=lambda x: (-x[1], x[0]))
for ime, bod in popis[:3]:
  print(ime, bod)