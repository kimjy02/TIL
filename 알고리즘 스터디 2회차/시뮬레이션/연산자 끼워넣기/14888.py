N = int(input())
A = list(map(int, input().split()))
operator = {0: 0, 1: 0, 2: 0, 3: 0}
operator[0], operator[1], operator[2], operator[3] = map(int, input().split())

def calculator(idx, A, operator):
    global result, max_value, min_value
    if idx >= N:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        # answer.append(result)
        # result = A[0]
        return 

    if operator[0] != 0:
        result += A[idx]
        operator[0] -= 1
        calculator(idx+1, A, operator)
        result -= A[idx]
        operator[0] += 1
    if operator[1] != 0:
        result -= A[idx]
        operator[1] -= 1
        calculator(idx+1, A, operator)
        result += A[idx]
        operator[1] += 1
    if operator[2] != 0:
        result *= A[idx]
        operator[2] -= 1
        calculator(idx+1, A, operator)
        result //= A[idx]
        operator[2] += 1
    if operator[3] != 0:
        r = result
        if result < 0 and result % A[idx] != 0:
            result = result // A[idx] + 1
            operator[3] -= 1
            calculator(idx+1, A, operator)
            result = r
            operator[3] += 1
        else:
            result //= A[idx]
            operator[3] -= 1
            calculator(idx+1, A, operator)
            result = r
            operator[3] += 1

# print(operator)

max_value = -1000000000
min_value = 1000000000
result = A[0]

# answer = []
calculator(1, A, operator)
print(max_value)
print(min_value)
# print(-(1//2))
# print(answer)
# print(-1//2)

