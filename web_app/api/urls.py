from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("post/", views.PostViewSet.as_view({"post": "create"}), name="post-create"),
    path(
        "post/<int:pk>",
        views.PostViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="post-detail",
    ),
    path("post-vote/<int:pk>", views.post_vote, name="post-vote"),
    path(
        "comment/post-<int:post_pk>",
        views.CommentViewSet.as_view({"post": "create"}),
        name="comment",
    ),
    path(
        "comment/<int:pk>",
        views.CommentViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="comment",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
