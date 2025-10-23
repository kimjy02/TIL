A, B, C = map(int, input().split())

def recursive(total, A, i):
    if i==B:
        return total
    total *= A
    return recursive(total, A, i+1)

print(recursive(1, A, 0)%C)