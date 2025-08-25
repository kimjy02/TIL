'''
    다음과 같이 2X1, 2X2, 2X3 크기의 타일을 2XN 크기의 공간에 붙이려고 한다.
    N이 주어지면 붙이는 방법이 모두 몇 가지가 있는지 출력하는 프로그램을 작성하라.

    입력
        1. T : 테스트 케이스 수
        2. N

    출력
        - # {tc} {타일을 붙이는 방법의 수}
'''
# import sys
# sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    