from rest_framework import serializers
from .models import Post, Category

class PostSerializer(serializers.ModelSerializer):
    '''
    Class that defines post serializer
    '''
    class Meta:
        model = Post
        fields = ('id','image', 'title', 'content', 'timestamp', 'category', 'author', 'is_approved')

    def create(self,validated_data):
        return Post.objects.create(**validated_data)

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