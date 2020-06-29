from rest_framework import serializers
from .models import Post, Category,Wishlist, Like, Dislike
from rest_framework.serializers import ModelSerializer,SerializerMethodField,ValidationError
from django.contrib.auth import get_user_model
from comment.models import Comment
from comment.api.serializers import CommentSerializer


User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    '''
    Class that defines post serializer
    '''
    comments =SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id','image', 'title', 'content', 'timestamp', 'category', 'comments','author', 'is_approved')

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


class WishlistSerializer(serializers.ModelSerializer):
    
    user = serializers.SlugRelatedField(read_only = True, slug_field = 'username')

    class Meta:
        model = Wishlist
        fields = ('user', 'post') 
        extra_kwargs= {'post': {'required': False}} 
        depth =1

class WishlistSerializerwithoutUser(serializers.ModelSerializer):
   
    class Meta:
        model = Wishlist
        fields = ('post',)

    def update(self, instance, validated_data):
        post = validated_data.pop('post')
        wishlist = instance
        for (key, value) in validated_data.items():
            setattr(wishlist, key, value)

        for i in post:
            wishlist.post.add(i)

        wishlist.user = validated_data.get('user', instance.user)
        wishlist.save()

        return wishlist
    

# class WishlistSerializer(serializers.ModelSerializer):
#     '''
#     Class that defines post serializer
#     '''
#     class Meta:
#         model = Wishlist
#         fields = '__all__'

# class ListwishtSerializer(serializers.ModelSerializer):
#     post = PostSerializer(read_only=True,many=True)
#     '''
#     Class that defines post serializer
#     '''
#     class Meta:
#         model = Wishlist
#         fields = '__all__'




class LikeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Like
        fields = ('user','post')  

class DislikeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Dislike
        fields = ('user', 'post')