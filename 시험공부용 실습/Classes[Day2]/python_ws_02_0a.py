class User:
    user_count = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.user_count += 1
        print(self.name)
        print(self.email)
    
    @staticmethod
    def description():
        print("SNS 사용자는 소셜 네트워크 서비스를 이용하는 사람을 의미합니다.")
    
Alice = User('Alice', 'alice@example.com')
Bob = User('Bob', 'bob@example.com')
print(f'현재까지 생성된 사용자 수: {User.user_count}')
User.description()