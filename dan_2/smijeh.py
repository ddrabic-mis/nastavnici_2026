N = int(input())
BR = 0

for i in range(N):
    X = int(input())
    if(X % 10 == 6 or X % 10 == 7):
        BR += 1

print(BR)
