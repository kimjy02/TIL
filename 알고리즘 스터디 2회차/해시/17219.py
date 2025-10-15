import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pw = {}
for _ in range(n):
    site, p = input().split()
    pw[site] = p


for _ in range(m):
    print(pw[input().strip()])
