N = int(input())

T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())

# print(T)
# print(P)

for i in range(N):
    if T[i] > N - i:
        T[i] = 0
        P[i] = 0


# print(T)
# print(P)

dp = P[:]

for i in range(N):
    total_time = i + T[i]
    current_time = i
    print(f'i:{i}, total_time : {total_time}')
    while total_time <= N-1:
        if T[total_time] == 0:
            print(f'T[total_time] == 0')
            print(f'i : {i}, current_time :{current_time}, total_time : {total_time}')
            print()
            # if total_time == i:
            #     break
            # else:
            #     total_time = total_time - T[current_time] + 1
            #     for j in range(current_time-1, -1, -1):
            #         if j + T[j] == current_time:
            #             current_time = j
            #             break
            if total_time == N-1:
                break
            else:
                total_time += 1

        else:
            # dp[current_time] = max(dp[current_time], dp[i]+P[current_time])
            dp[total_time] = max(dp[total_time], dp[current_time] + P[total_time])
            print(f'T[total_time] != 0')
            print(dp)
            print(f'i : {i}, current_time :{current_time}, total_time : {total_time}')
            print()
            current_time = total_time
            total_time += T[total_time]

print(max(dp))