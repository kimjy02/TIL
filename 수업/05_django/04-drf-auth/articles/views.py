from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# authentication Decorators
# from rest_framework.decorators import authentication_classes
# from rest_framework.authentication import TokenAuthentication

# permission Decorators
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            # 유저 정보 저장하려면,
            # 요청 보내는 시점에, 본인이 누구인지를 밝힐 토큰을 전송
            # 인증을 위한 토큰이므로, form-data가 아닌
            # headers 영역에 Authorization 키에, 벨류로 토큰을 보내고
                # 그 벨류는 'Token 실제토큰' 형식으로 전송한다.
                # 이때, 실제 토큰은 ? 로그인 or 회원가입 시
                # dj-rest-auth가 발급해준 그 토큰
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
