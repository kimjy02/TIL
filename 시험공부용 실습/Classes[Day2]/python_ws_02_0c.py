class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def show_info(self):
        print(f'Name: {self.name}, Email: {self.email}')
    
class AdminUser(User):
    def __init__(self, name, email, permissions):
        super().__init__(name, email)
        self.permissions = permissions
    
    def show_info(self):
        print(f'Name: {self.name}, Email: {self.email}, Permissions: {self.permissions}')

Alice = User('Alice', 'alice@example.com')
Bob = User('Bob', 'bob@example.com')
Charlie = AdminUser('Charlie', 'charlie@example.com', 'Full Access')
Alice.show_info()
Bob.show_info()
Charlie.show_info()