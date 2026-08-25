A=15
print(A)
print(f"{A*A=}")
if A>10:
  print("A je veće od 10")
else:
  print("A je manje ili jednako 10")

# strukture Pythona
# nterac - tuple -> lista koja služi samo za čitanje
B=(1,2,3,4,5,2,3,4,5,6,7,8,9) 
# lista - može se mijenjati
C=[1,2,3,4,5,2,3,4,5,6,7,8,9] 
print(f"prvi element {B[0]=}")
print(f"zadnji element { B[len(B)-1]= }")
print(f"zadnji element { B[-1]= }")
# mješovita lista
D=[1,2,3,"Dobar dan", 15.5, True, [4,5,6]]
print(f"prvi element {D[0]=}")
print(f"četvrti element {D[3]=}")
print(f"zadnji element { D[-1]= }")
print(f"zadnji element { D[-1][2]= }") # ispisuje treći element zadnjeg elementa liste D
# specifičnosti koje su važne za Python
Y=[1,2,3,4,5]
X=Y # X i Y dijele istu listu, promjena u jednoj listi utječe na drugu
Z=X[:] # Z je kopija liste X, promjena u jednoj listi ne utječe na drugu
X[0]=100
X[-1]=100
print(f"{Y=}")
print(f"{X=}")
print(f"{Z=}")
#exit() # prekida izvođenje programa
# skupovi - neuređene kolekcije bez ponavljanja elemenata
E={1,2,3,4,5,2,3,4,5,6,7,8,9}
print(f"{C=}")
print(f"{E=}")
E.add(2) # dodaje element 10 u skup E
print(f"{E=}")
# učitaj tekst i ispiši koliko slova  se u tekstu koristi
# napomena: praznina, zarez... nisu slova
F="Volim informatiku, pa stoga vise sudjelujem na edukacijskom kampu u Puli."
F2=F.replace(" ","").replace(",","").replace(".","").replace("!","").upper()
slova=set(F2)
print(f"{slova=}")
print(f"Broj različitih slova u tekstu je {len(slova)}")
# riječnici
R={1:"jedan", 2:"dva", 3:"tri", 4:"četiri", 5:"pet"}
# učitaj broj od 1 do 5 i ispiši ga tekstom
T=int(input())
print(f"Broj {T} se piše kao {R[T]=}")