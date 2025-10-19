from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

# pair_score = dict()
# for i in range(N):
#     for j in range(N):
#         if i != j:
#             pair_score[(i, j)] = S[i][j]

# print(pair_score)

min_diff = float('inf')
people = [i for i in range(N)]

for team1 in combinations(people, N // 2):
    team2 = [p for p in people if p not in team1]

    score1 = 0
    score2 = 0

    for i, j in combinations(team1, 2):
        score1 += S[i][j] + S[j][i]

    for i, j in combinations(team2, 2):
        score2 += S[i][j] + S[j][i]

    diff = abs(score1 - score2)
    if diff == 0:
        min_diff = 0
        break
    min_diff = min(min_diff, diff)

print(min_diff)
