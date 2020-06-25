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




class UserLoginSerializer(serializers.ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank =True)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token',
        ]
        extra_kwargs = {"password":
                            {'write_only':True}
                            }
    def validate(self,data):
        user_obj= None
        username = data.get('username', None)
        password = data['password']
        if not username:
            raise serializers.ValidationError('Username is required')

        user = User.objects.filter(
            Q(username=username)
        ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError('This username is not valid')

        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError('Incorrect credentials, try again')


        data['token'] = '123456789' 
        return data

class ProfileSerializer(serializers.ModelSerializer):
    ''' 
    Class that defines profile serializer
    '''
    class Meta:
        model = Profile
        fields = ('user', 'bio' ,'picture')
     

class ProfileSerializerwithoutUser(serializers.ModelSerializer):
    '''
    Class that defines profile serializer without user
    '''
    class Meta:
        model = Profile
        fields = ('bio' ,'picture')

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.save()
        return instance