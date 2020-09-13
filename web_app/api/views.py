from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import F

from blog.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing posts.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing comments.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, post_pk):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        comment = self.perform_create(serializer)
        comment.post = Post.objects.get(pk=post_pk)
        comment.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        instance = serializer.save()
        return instance


@api_view(["POST"])
def post_vote(request, pk):
    Post.objects.filter(pk=pk).update(votes_amount=F("votes_amount") + 1)
    return Response(
        {"result": "Your vote has been successfully counted"},
        status=status.HTTP_201_CREATED,
    )
