# 99_MRO.py
O = object
class D(O) : pass
class E(O) : pass
class F(O) : pass
class B(D, E) : pass
class C(D, F) : pass
class A(B, C) : pass

# A 클래스의 상속 탐색 순서
print(A.__mro__) # A B C D E F O


class D(O) : pass
class E(O) : pass
class F(O) : pass
class B(D, E) : pass
class C(F, D) : pass # 변경
class A(B, C) : pass

# A 클래스의 상속 탐색 순서
print(A.__mro__) # A B C F D E O
