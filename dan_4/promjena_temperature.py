N=int(input())
T=list( map(int, input().split()) )
brojac=0
for i in range(1,N):
  if T[i]>T[i-1]:
    brojac+=1
print(brojac)