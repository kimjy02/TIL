num = 0  # 전역 변수

def increment():
    global num  # num를 전역 변수로 선언
    num += 1

print(num)  # 0
increment()
print(num)  # 1

###############
# 필기 내용
# LEGB rule -> 변수 탐색 순서
# Local -> 
# En-Closed
# Global
# Built-In

def outer():
    x = 0

    def inner() :
        x = 10
        print(x)

    inner()
    print(x)

x = 10
outer()

def outer():
    # 탐색 순서에 다라서 outer에 x가 없어서
    # global에 있는 x=100을 참조해서 100을 출력함.
    # 그럼 내가 x에 0을 할당했을 때, 왜 global에는 영향을 미치치 않는가?
    # 나의 local 영역에 x라는 새로운 변수를 만든 것.
        # 함부로 내 상위의 변수를 바꿀 수 없음
        # LEGB 중, G와 B를 생각해보면,
        # global과 built-in에 이미 정의된 어떤 값들이 다른 곳에서 이미 사용되고 있을 수 있다.
        # 그런데 local 영역에서 그렇게 함부로 값을 바꿔서는 안됨.
    # 그럼에도 불구하고, 내가 직접적으로 global 영역에 있는 값에 영향을 끼치고 싶다면,
    global x
    x = '안녕하세요'
    def inner() :
        x = 10
        print(x)

    inner()
    print(x)
    
x = 100
outer()



# global에 정의된 값을 사용하고 싶고 그 값을 내가 바꾸거나 조작하고자 한다면
# 권장하는 방법
def some(y) : # 매개변수로 만들어서, 인자로 전달하는 방식
    y = '안녕하세요'
    return y

y = 100
# y = some(y) # some 함수의 실행 결과를 y에 다시 할당하거나, 혹은 완전히 다른 변수에 할당해서 사용가능
z = some(y)
print(y, z)