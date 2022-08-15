from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from post.models import Post, Like, Comment, Favorite, Contact
from post.serializers import PostSerializer, CommentSerializer, ContactSerializer


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]

    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'title']
    filterset_fields = ['owner']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    @action(methods=['POST'], detail=True)
    def like(self, request, pk, *args, **kwargs):
        try:
            like_object, _ = Like.objects.get_or_create(owner=request.user, post_id=pk)
            like_object.like = not like_object.like
            like_object.save()
            status = 'liked'

            if like_object.like:
                return Response({'status': status})
            status = 'unliked'
            return Response({'status': status})
        except:
            return Response('Нет поста')


    @action(methods=['POST'], detail=True)
    def favorite(self, request, pk, *args, **kwargs):
        try:
            favorite_object, _ = Favorite.objects.get_or_create(owner=request.user, post_id=pk)
            favorite_object.favorite = not favorite_object.favorite
            favorite_object.save()
            status = 'You added to favorite'

            if favorite_object.favorite:
                return Response({'status': status})
            status = 'You removed out favorite'
            return Response({'status': status})
        except:
            return Response('Нет поста')


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactView(mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer







