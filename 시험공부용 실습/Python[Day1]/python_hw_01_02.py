# 1번. 학생들의 이름과 점수를 딕셔너리에 저장하세요.

students = {
    'Alice': 85,
    'Bob': 78,
    'Charlie': 92,
    'David': 88,
    'Eve': 95
}
print('1. 학생들의 이름과 점수를 딕셔너리에 저장\nstudents type:', type(students))

# 2번. 모든 학생의 평균 점수를 계산하여 출력하시오.
sum = 0
for value in students.values():
    sum += value

print('2. 모든 학생의 평균 점수: ''%.2f' % float(sum/5))

# 3번. 80점 이상을 받은 학생들의 이름을 리스트 컴프리헨션을 사용하여 추출하시오.
higher_list = [key for key in students if students[key] >= 80]
print(f'3. 기준 점수(80점) 이상을 받은 학생 수: {higher_list}')

# 4번. 학생들의 점수를 높은 순서대로 정렬하여 출력하시오.
# result : 4. 점수 순으로 정렬: 
#          Eve: 95
#          Charlie: 92
#          David: 88
#          Alice: 85
#          Bob: 78

sorted_list = sorted(students.items(), key=lambda x:x[1], reverse=True)
print('4. 점수 순으로 정렬: ')
for name, score in sorted_list:
    print(f'{name}: {score}')

# 5번. 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이를 계산하여 출력하시오.
# result : 5. 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이: 17

diff = max(students.values())-min(students.values())
print(f'5. 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이: {diff}')

# 6번. 각 학생의 점수가 평균 점수보다 높은지 낮은지를 판단하여, 낮은 학생의 이름과 성적을 함께 출력하시오.
# result : 6. 각 학생의 점수가 평균보다 높은지 낮은지 판단:
#          Alice 학생의 점수(85)는 평균 이하입니다.
#          Bob 학생의 점수(78)는 평균 이하입니다.
#          Charlie 학생의 점수(92)는 평균 이상입니다.
#          David 학생의 점수(88)는 평균 이상입니다.
#          Eve 학생의 점수(95)는 평균 이상입니다.

print('6. 각 학생의 점수가 평균보다 높은지 낮은지 판단:')
for name, score in students.items():
    if score >= sum/5 :
        print(f'{name} 학생의 점수({score})는 평균 이상입니다.')
    else :
        print(f'{name} 학생의 점수({score})는 평균 이하입니다.')