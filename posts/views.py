from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
    )
from .serializer import PostSerializer
from .models import  Post
from authentication.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from authentication.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404



class PostList(ListModelMixin,GenericAPIView,CreateModelMixin):
    '''
    View that allows you to view and add to the list of all posts
    '''

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        '''
        Function that gives you list of all the posts
        '''
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        '''
        Function that lets you add a new post to the list of all post
        '''
        return self.create(request,*args, *kwargs)

class PostDetails(RetrieveAPIView):
    '''
    View that allows you to access one item on the list 
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_post(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Http404

    def get(self,request, pk, format=None):
        '''
        Function that retrieves specified post
        '''
        post = self.get_post(pk)
        serializers = PostSerializer(post)
        return Response(serializers.data)

    def put(self,request,pk, format=None):
        '''
        Function that updates a specified post
        '''
        post = self.get_post(pk)
        serializers = PostSerializer(post, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        '''
        Function that deletes a specified post
        '''
        post = self.get_post(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


