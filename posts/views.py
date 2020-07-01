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
from authentication.models import User
from rest_framework import status,viewsets,serializers,status,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from .models import Post, Category,Subscription,Wishlist
from authentication.models import User
from .serializer import PostSerializer, CategorySerializer,PostSerializerWithoutAuthor, SubscriptionSerializer,SubcriptionSerializerwithoutUser,WishlistSerializer,WishlistSerializerwithoutUser
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.parsers import FormParser,MultiPartParser, JSONParser, FileUploadParser
from rest_framework import filters
# from .permissions import IsOwnerOrReadOnly,IsUserStaff
from .permissions import IsOwnerOrReadOnly, IsUserStaff
from .serializer import PostCreateSerializer
from authentication.models import Profile
from utils.media_handler import CloudinaryResourceHandler




class PostList(ListModelMixin,GenericAPIView,CreateModelMixin):
    '''
    View that allows you to view and add to the list of all posts
    '''
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = (FormParser,MultiPartParser,JSONParser, FileUploadParser)
    

    def get(self, request, *args, **kwargs):
        '''
        Function that gives you list of all the posts
        '''
        return self.list(request, *args, *kwargs)

Uploader =  CloudinaryResourceHandler() 

class CreatePost(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def post(self, request, format = None):
        '''
        Function that lets you add a new post to the list of all post
        '''
        payload = request.data
        image = Uploader.upload_image_from_request(request)
        payload['image'] = image
        
        serializers = self.serializer_class(data = payload)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

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
        self.check_object_permissions(self.request, post)
        serializers = PostSerializer(post)
        return Response(serializers.data)

    def put(self,request,pk, format=None):
        '''
        Function that updates a specified post
        '''
        post = self.get_post(pk)
        user = request.user
        serializers = PostSerializerWithoutAuthor(instance=post, data= request.data, partial=True)

        if post.author != user:
            return Response('You do not have permission to change post')

        if serializers.is_valid(raise_exception=True):
            post = serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        '''
        Function that deletes a specified post
        '''
        post = self.get_post(pk)
        user = request.user

        # if post.author != user:
        #     return Response('You do not have permission to change post')

        self.check_object_permissions(self.request, post)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryList(ListModelMixin,GenericAPIView,CreateModelMixin):
    '''
    View that allows you to view and add to the list of all categories
    '''

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsUserStaff,)

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
    # permission_classes = (IsUserStaff,)


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

class SubscriptionList(ListModelMixin,GenericAPIView):
    '''
    List that allows you to view all the subscriptions
    '''

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    
    def get(self, request, *args, **kwargs):
        '''
        Function that gives you a list of all the subscriptions
        '''
        return self.list(request,*args,*kwargs)

class SubscriptionDetails(RetrieveAPIView, UpdateAPIView):
    '''
    View that allows you to access one subscription on the list
    '''
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = SubcriptionSerializerwithoutUser
        return serializer_class

    def get_subscription(self,pk):
        try:
            return Subscription.objects.get(user=pk)
        except Subscription.DoesNotExist:
            return Http404

    def get(self,request, pk, format=None):
        '''
        Function that retrieves specified post
        '''
        subscription = self.get_subscription(pk)
        categories = subscription.categories.all()
        posts = Post.objects.all()
        
        for i in posts:
            if i.category in categories:
                subscription.posts.add(i)

        serializers = SubscriptionSerializer(subscription)
        return Response(serializers.data)


    def put(self,request,pk, format=None):
        '''
        Function that updates a specified subscription
        '''
        subscription = self.get_subscription(pk)
        user = request.user  

        # if subscription.user != user:
        #     return Response('You do not have permission to edit')

        serializers = SubcriptionSerializerwithoutUser(instance =subscription,data= request.data, partial=True)

        if serializers.is_valid(raise_exception=True):
            subscription = serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscriptionsDelete(DestroyAPIView,):
    '''
    View that allows you to delete one category  on the list
    '''

    def destroy(self,request,pk, cat_id, format=None): 
        def get_subscription(self,pk):
            try:
                return Subscription.objects.get(user=pk)
            except Subscription.DoesNotExist:
                return Http404

        def get_category(self,pk):
            try:
                return Category.objects.get(id=cat_id)
            except Category.DoesNotExist:
                return Http404

        

        subscription = Subscription.objects.get(user=pk)
        category = Category.objects.get(id=cat_id)

        if category in subscription.categories.all():
            subscription.categories.remove(category)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


    



class WishlistList(ListModelMixin,GenericAPIView):
       
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    
    def get(self, request, *args, **kwargs):
      
        return self.list(request,*args,*kwargs)

class WishlistDetails(RetrieveAPIView, UpdateAPIView):
    
    queryset =Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = WishlistSerializerwithoutUser
        return serializer_class

    def get_wishlist(self,pk):
        try:
            return Wishlist.objects.get(user=pk)
        except Wishlist.DoesNotExist:
            return Http404

    def get(self,request, pk, format=None):

        wishlist = self.get_wishlist(pk)
        serializers = WishlistSerializer(wishlist)
        return Response(serializers.data)

    def put(self,request,pk, format=None):
       
        wishlist = self.get_wishlist(pk)  
        user =request.user
        serializers = WishlistSerializerwithoutUser(instance = wishlist,data= request.data, partial=True)


        # if wishlist.user != user:
        #     return Response('You do not have permission to edit')

        if serializers.is_valid(raise_exception=True):
            wishlist = serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class WishlistDelete(DestroyAPIView,):
  
    def destroy(self,request,pk, post_id, format=None): 
        def get_wishlist(self,pk):
            try:
                return  Wishlist.objects.get(user=pk)
            except  Wishlist.DoesNotExist:
                return Http404

        def get_post(self,pk):
            try:
                return Post.objects.get(id=post_id)
            except Post.DoesNotExist:
                return Http404

        

        wishlist= Wishlist.objects.get(user=pk)
        post = Post.objects.get(id=post_id)

        if post in  wishlist.posts.all():
            wishlist.posts.remove(post)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class getUserPosts(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, pk):
        '''
        Function that gives you a list of all the subscriptions
        '''
        posts = Post.objects.filter(author=pk)
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)


    


        
    
