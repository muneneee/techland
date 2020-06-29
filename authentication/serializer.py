from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,CharField,EmailField
from django.db.models import Q
from .models import User, Profile
from django.core.exceptions import ValidationError



class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only':True}
        }

    
    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )

        password = self.validated_data['password']
        password2=self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'passwords must match'})
        user.set_password(password)
        user.save()
        return user




class ProfileSerializer(serializers.ModelSerializer):
    ''' 
    Class that defines profile serializer
    '''
    user = serializers.SlugRelatedField(read_only = True, slug_field = 'username')

    class Meta:
        model = Profile
        fields = ('id','user', 'bio' ,'picture')
    

class ProfileSerializerwithoutUser(serializers.ModelSerializer):
    '''
    Class that defines profile serializer without user
    '''
    class Meta:
        model = Profile
        fields = ('id','bio' ,'picture')

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.save()
        return instance
