import re
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from serializers import PostSerializer
from models import Post
from collections import Counter
from web.settings import POST_COMMON_WORDS_COUNT


class PostsView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class StatsView(APIView):
    def get(self, request, format=None):
        posts_content = ""
        for post in Post.objects.all():
            posts_content += post.text
        words = re.findall(r'\w+', posts_content.lower())
        return Response(Counter(words).most_common(POST_COMMON_WORDS_COUNT))


class StatsAuthorView(APIView):
    def get(self, request, *args, **kwargs):
        posts_content = ""
        post_author_name = '{"' + kwargs.get('pk').title().replace('_', " ") + '"}'
        for post in Post.objects.filter(author=post_author_name):
            posts_content += post.text
        words = re.findall(r'\w+', posts_content.lower())
        return Response(Counter(words).most_common(POST_COMMON_WORDS_COUNT))
