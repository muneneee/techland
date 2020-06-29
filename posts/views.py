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
from .models import Post, Category,Wishlist, Like, Dislike
from authentication.models import User
from .serializer import PostSerializer, CategorySerializer,PostSerializerWithoutAuthor,WishlistSerializer,ListwishtSerializer, LikeSerializer, DislikeSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import generics

from django.utils import timezone

from rest_framework.decorators import api_view


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

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = PostSerializerWithoutAuthor
        return serializer_class

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
        serializers = PostSerializerWithoutAuthor(instance=post, data= request.data, partial=True)
        if serializers.is_valid(raise_exception=True):
            post = serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        '''
        Function that deletes a specified post
        '''
        post = self.get_post(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryList(ListModelMixin,GenericAPIView,CreateModelMixin):
    '''
    View that allows you to view and add to the list of all categories
    '''

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        '''
        Function that gives you list of all the categories
        '''
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        '''
        Function that lets you add a new category to the list of all categories
        '''
        return self.create(request,*args, *kwargs)

class CategoryDetails(RetrieveAPIView):
    '''
    View that allows you to access one item on the list 
    '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_category(self,pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Http404

    def get(self,request, pk, format=None):
        '''
        Function that retrieves specified category
        '''
        category = self.get_category(pk)
        serializers =CategorySerializer(category)
        return Response(serializers.data)

    def put(self,request,pk, format=None):
        '''
        Function that updates a specified category
        '''
        category = self.get_category(pk)
        serializers = CategorySerializer(category, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        '''
        Function that deletes a specified category
        '''
        category = self.get_category(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Wishlists(generics.ListCreateAPIView):
    '''
    View that allows you to view and add to the list of all posts
    '''

    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    
    def get(self,request):
        wishlist = Wishlist.objects.all()
        serializer = ListwishtSerializer(wishlist,many=True)
        return Response(serializer.data)



class WishlistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

@api_view(['GET'])
def get_likes(requests):
    query_set = Like.objects.all()
    serializer = LikeSerializer(query_set, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_likes(requests, post_id):
    post = Post.objects.get(id=post_id)
    serializer = LikeSerializer(post, request.user)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_dislikes(requests):
    query_set = Dislike.objects.all()
    serializer = DislikeSerializer(query_set, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_dislikes(requests, post_id):
    post = Post.objects.get(id=post_id)
    data = [post, user]
    serializer = DislikeSerializer(data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

#current_user=request.user
#    user_exists = Dislike.objects.filter(user = current_user).exists()
#    if user_exists:
#        Dislikes.objects.remove(current_user)