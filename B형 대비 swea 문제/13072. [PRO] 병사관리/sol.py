T, question_mark = map(int, input().split())

def hire(number, team, score):
    team_str.setdefault(team, []).append([score, number])
    return

def fire(number):



for tc in range(1, T+1):
    n = int(input())
    team_str = {}
    for i in range(n):
        input_value = list(map(int, input().split()))
        if len(input_value) == 1:
            continue
        elif input_value[0] == 2:
            hire(input_value[1], input_value[2], input_value[3])
        elif input_value[0] == 3:

