'''
    N X N개의 cell로 구성
    1개의 cell에는 1개의 Core 혹은 1개의 전선
    가장자리에는 전원이 흐르고 있음
    Core와 전원을 연결하는 전선은 직선으로만 설치 가능
    전선은 절대로 교차해서는 안됨
    
    초기 상태로는 전선을 연결하기 전 사앹의 멕시노스 정보가 주어짐
    가장자리에 위치한 Core는 이미 전원이 연결된 것으로 간주
    
    최대한 많은 Core에 전원을 연결했을 경우, 전선 길이의 합을 구하고자 한다.
    단, 전선 길이의 합이 최소가 되는 값을 구하라.
    
    제약 사항
        1. 7 <= N <= 12
        2. 1 <= Core 개수 <= 12
        3. 최대한 많은 Core에 전원을 연결해도, 전원이 연결되지 않는 Core 존재할 수 있음

    입력
        1. T : 테스트 케이스 수
        2. N : 가로 세로 길이
        3. N X N 배열 [0은 빈 cell, 1은 core]

    출력
        - #{tc} {전선 길이의 합이 최소가 되는 값}
'''
import sys
sys.stdin = open('sample_input.txt')

#     상  하  좌   우
dc = [-1, +1, +0, +0]
dr = [+0, +0, -1, +1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
