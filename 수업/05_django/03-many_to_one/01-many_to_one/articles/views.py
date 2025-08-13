from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleSerializer, ArticleListSerializer, CommentSerializer
from .models import Article, Comment

# Create your views here.

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True) 
        return Response(serializer.data)
    elif request.method == 'POST':
        # class에 인스턴스 생성하기 위한 인자 전달 시 ... 키워드 인자를 써야하는 이유?
        '''
            class Some:
                def __init__(self, arg1, arg2 = 'default', arg3 = 'default', ...):
                    pass
            
            s1 = Some('arg1', arg3 = 'other data')
        '''
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # article = Article.objects.annotate(num_of_comments=Count('comment')).get(
    #     pk=article_pk
    # )
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 댓글 생성
@api_view(['POST'])
def comment_create(request, article_pk):
    # 게시글을 하나 지정해서, 그곳에 댓글을 생성한다.
    # 댓글 생성은 사용자가 보낸 content 정보를 저장한다.
    # 유효성을 검사한다.
        # DB에 반영한다.
        # 완성된 댓글 정보를 사용자에게 반환한다. (JSON)
    

# 모든 댓글 조회
@api_view(['GET'])
def comment_list(request):
   pass

# 댓글 pk 값으로 조회, 삭제, 수정
@api_view(['GET'])
def comment_detail(request, comment_pk):
    pass
   

