import sys
input = sys.stdin.readline

N = int(input().strip())
having_lst = set(map(int, input().split()))
M = int(input().strip())
comparing_lst = list(map(int, input().split()))

result = ['1' if x in having_lst else '0' for x in comparing_lst]
print(' '.join(result))
