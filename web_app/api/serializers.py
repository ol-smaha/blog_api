from rest_framework import serializers
from blog.models import Author, Post, Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name"]


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = ["author", "title", "link"]

    def create(self, validated_data):
        author_data = validated_data.pop("author")
        author = Author.objects.create(**author_data)
        post = Post.objects.create(author=author, **validated_data)
        return post

    def update(self, instance, validated_data):
        author_data = validated_data.get("author")
        if author_data:
            instance.author = Author.objects.create(**author_data)
        instance.title = validated_data.get("title", instance.title)
        instance.link = validated_data.get("link", instance.link)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Comment
        fields = ["author", "content"]

    def create(self, validated_data):
        author_data = validated_data.pop("author")
        author = Author.objects.create(**author_data)
        comment = Comment.objects.create(author=author, **validated_data)
        return comment

    def update(self, instance, validated_data):
        author_data = validated_data.get("author")
        if author_data:
            instance.author = Author.objects.create(**author_data)
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance
