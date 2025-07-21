import sys
T = int(input())
for i in range(T) :
    A, B = sys.stdin.readline().rsplit()
    print(int(A)+int(B))