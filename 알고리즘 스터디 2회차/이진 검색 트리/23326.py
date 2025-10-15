import sys
import heapq

input = sys.stdin.readline

N, Q = map(int, input().split())

A = list(map(int, input().split()))

start = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if A[query[1]] == 0:
            A[query[1]] = 1
        else:
            A[query[1]] = 0
    elif query[0] == 2:
        start += query[1]
        if start > N-1:
            start %= N
    else:
        for _ in range(start, )