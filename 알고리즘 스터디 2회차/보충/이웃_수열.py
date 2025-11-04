import sys
input = sys.stdin.readline

def next_term(s):
    res = []
    i, n = 0, len(s)
    while i < n:
        j = i + 1
        while j < n and s[j] == s[i]:
            j += 1
        res.append(s[i])
        res.append(str(j - i))  # 값 뒤에 개수
        print(res)
        i = j
    return ''.join(res)

n = int(input().strip())
s = "1"
for _ in range(1, n):
    s = next_term(s)
print(int(max(s)))

