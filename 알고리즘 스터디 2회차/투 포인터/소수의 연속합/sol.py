import sys
input = sys.stdin.readline

N = int(input().strip())

if N < 2:
    print(0)
    sys.exit(0)

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(N**0.5) + 1):
    if is_prime[i]:
        step = i
        start = i * i
        is_prime[start:N+1:step] = [False] * (((N - start) // step) + 1)

primes = [i for i in range(2, N + 1) if is_prime[i]]
# print(primes)

l = r = 0
cur = 0
ans = 0
while True:

    if cur >= N:
        if cur == N:
            ans += 1
        cur -= primes[l]
        l += 1
    else:
        if r == len(primes):
            break
        cur += primes[r]
        r += 1
    # print(f'cur:{cur}, ans:{ans}')

print(ans)
