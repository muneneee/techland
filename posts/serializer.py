from rest_framework import serializers
from .models import Post, Category, Wishlist
from rest_framework.serializers import ModelSerializer,SerializerMethodField,ValidationError
from django.contrib.auth import get_user_model
from comment.models import Comment
from comment.api.serializers import CommentSerializer


User = get_user_model()


class WishlistSerializer(serializers.ModelSerializer):
    ''' 
    Class that defines wishlist serializer
    '''
    user = serializers.SlugRelatedField(read_only = True, slug_field = 'username')

    class Meta:
        model = Wishlist
        fields = ('user', 'posts')
        extra_kwargs = {'posts': {'required': False}}
        depth = 1



class PostSerializer(serializers.ModelSerializer):
    '''
    Class that defines post serializer
    '''
    comments =SerializerMethodField()
    wishlists = WishlistSerializer(many=True, read_only=True)
    category = serializers. SlugRelatedField(read_only= True, slug_field= 'name')
    author = serializers.SlugRelatedField(read_only = True, slug_field = 'username')
    class Meta:
        model = Post
        fields = ('id','image', 'title', 'content', 'timestamp', 'category', 'comments','author', 'is_approved', 'wishlists')
        extra_kwargs = {'wishlists': {'required': False}}



    def create(self,validated_data):
        return Post.objects.create(**validated_data)

    def get_comments(self, obj):
        comments_qs = Comment.objects.filter_parents_by_object(obj)
        return CommentSerializer(comments_qs, many=True).data


class PostSerializerWithoutAuthor(serializers.ModelSerializer):
    '''
    Class that defines post without author
    '''
    class Meta:
        model = Post
        fields = ('id','image', 'title', 'content', 'timestamp', 'category','is_approved')
    
    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.category = validated_data.get('category', instance.category)
        instance.is_approved = validated_data.get('is_approved', instance.is_approved)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance

class  CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

    def create(self,validated_data):
        return Category.objects.create(**validated_data)






# class WishlistSerializerwithoutUser(serializers.ModelSerializer):
#     '''
#     Class that defines wishlist serializer without user
#     '''
#     class Meta:
#         model = Wishlist
#         fields = ('posts',)

#     def update(self, instance, validated_data):
#         instance.user = validated_data.get('user', instance.user)
#         instance.posts = validated_data.get('posts', instance.posts)
#         instance.save()
#         return instance
    
    

    
