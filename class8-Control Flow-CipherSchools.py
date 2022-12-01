n=5
for i in range(5):
    for j in range(n):
        print(i,end="")
    print()
n=7

for i in range(n):
    for j in range(n):
        print(max(i+1,j+1,n-1,n+-j),end=" ")
    print()
max(1,5,6,7,5)

for i in range(n):
    for j in range(n):
        print(n-i-1,end=" ")
    print()

for i in range(n):
    for j in range(n):
        print(n-j-1,end=" ")
    print()


for i in range(n):
    for j in range(n):
        print(max(i,j),max(n-j,n-i),end=" ")
    print()


