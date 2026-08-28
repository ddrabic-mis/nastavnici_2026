def pretvorba(val):
    return val if val.isalpha() else int(val)

N=int(input())
ucenici=[]
for i in range(N):
    #ime, ocjena = map(pretvorba, input().split())
    #ucenici.append([ input(), int(input()) ])
    #ucenici.append(list(map(pretvorba, input().split())))
    ime, ocjena = input().split()
    ucenici.append([ime, int(ocjena)])

#print(ucenici)
ucenici.sort(key=lambda x: (-x[1], x[0]))

finalisti = ucenici[ : min(5, len(ucenici)) ][::-1]

dodatni_bodovi=list(map(int, input().split()))
for i, bodovi in enumerate(dodatni_bodovi):
    finalisti[i].append(bodovi)  #   ['Ema', 79]

#print(finalisti)
finalisti.sort(key=lambda x: ( -(x[1]+x[2]), -x[2]) )

pobjednici = finalisti[ : min(3, len(finalisti)) ]
for el in pobjednici:
    print(el[0], el[1]+el[2])