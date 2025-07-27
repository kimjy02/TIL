class Post:
    post_count = 0
    
    def __init__(self, title, content):
        self.title = title
        self.content = content
        Post.post_count += 1
    
    def show_content(self):
        print(f'Content: {self.content}')
    
    @classmethod
    def total_posts(cls):
        print(f'Total posts: {cls.post_count}')
    
    @staticmethod
    def description():
        print('SNS 게시물은 소셜 네트워크 서비스에서 사용자가 작성하는 글을 의미합니다.')

first_post = Post('First Post', 'This is the content of the first post.')
second_post = Post('Second Post', 'This is the content of the second post.')
print(f'Title: {first_post.title}')
first_post.show_content()
print(f'Title: {second_post.title}')
second_post.show_content()
Post.total_posts()
Post.description()