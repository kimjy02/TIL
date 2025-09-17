'''
    알파벳 소문자로 이루어진 N개의 단어가 들어오면
    아래와 같은 조건에 따라 정렬하는 프로그램을 작성

        1. 길이가 짧은 것부터
        2. 길이가 같으면 사전 순
            단, 중복된 단어는 하나만 남기고 제거

    [입력]
        1. N : 단어의 개수 (1 <= N <= 20,000)
        2. 알파벳 소문자로 이루어진 단어 N개 (한 줄에 하나씩)
            주어진 문자열의 길이는 50 이하
'''
# import heapq
#
# N = int(input())
# words = []
# answers = []
# for _ in range(N):
#     word = str(input())
#     if [len(word),word] not in words:
#         words.append([len(word), word])
#
# while words:
#     heapq.heapify(words)
#     num, word = heapq.heappop(words)
#     answers.append(word)
#
# for answer in answers:
#     print(answer)

N = int(input())
words = {input().strip() for _ in range(N)}

for w in sorted(words, key = lambda x : (len(x), x)):
    print(w)