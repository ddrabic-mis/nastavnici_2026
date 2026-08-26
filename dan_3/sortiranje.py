A=[2, 5 , 1, 3, 4, 8, 3, 0]
C=A[:] # duplciranje liste
B=sorted(A, reverse=True)
A.sort()
print(f"{A=}")

# iamo ime učenika i njegovu ocjenu uspjeha,
# te želimo sortirati učenike po ocjeni uspjeha
# ako 2 učenika imaju isto ime, onda ih sortiramo po imenu
U=[
  ("Perica", 5),
  ("Ivan",   5),
  ("Marija", 4),
  ("Ivan",   3)
]
U.sort()
print(*U, sep="\n")
print("--------------------")
U.sort(key=lambda el: (-el[1], el[0]) )
print(*U, sep="\n")