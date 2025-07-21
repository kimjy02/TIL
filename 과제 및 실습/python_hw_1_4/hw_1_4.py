'''
학생 점수 정보
   "Alice" = 85,
   "Bob" = 78,
   "Charlie" = 92,
   "David" = 88,
   "Eve" = 95
'''

# 학생들의 이름과 점수를 딕셔너리에 저장하시오.
# 모든 학생의 평균 점수를 계산하여 출력하시오.
# 80점 이상을 받은 학생들의 이름을 리스트 컴프리헨션을 사용하여 추출하시오.
# 학생들의 점수를 높은 순서대로 정렬하여 출력하시오.
# 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이를 계산하여 출력하시오.
# 각 학생의 점수가 평균 점수보다 높은지 낮은지를 판단하여, 낮은 학생의 이름과 성적을 함께 출력하시오.

# 아래에 코드를 작성하시오.

# 1번
students = {'Alice' : 85,
        'Bob' : 78,
        'Charlie' : 92,
        'David' : 88,
        'Eve' : 95}

# 2번
sum = 0
for v in students.values() :
   sum = sum + v

print('2. 모든 학생들의 평균 점수 :', sum/5)

# 3번
high = [name for name, score in students.items() if score >= 80]
print('3. 기준 점수(80점) 이상을 받은 학생 :', high)

# 4번
print('4. 점수 순으로 정렬 : ')
for k , v in sorted(students.items(), key=lambda item: item[1], reverse=True) :
   print(f"{k}: {v}")

# 5번
print('5. 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이:', max(students.values())- min(students.values()))

# 6번
print('6. 각 학생의 점수가 평균보다 높은지 낮은지 판단 :')
for k, v in students.items() :
   if (v <= sum/5) :
      print(f"{k}학생의 점수({v})는 평균 이하입니다.")
   else :
      print(f"{k}학생의 점수({v})는 평균 이상입니다.")