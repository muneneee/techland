from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import User,Profile
from .serializer import RegistrationSerializer, ProfileSerializer, ProfileSerializerwithoutUser, TokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.mixins import ListModelMixin
from django.http import Http404
from rest_framework_simplejwt.views import TokenViewBase
from utils.media_handler import CloudinaryResourceHandler





@api_view(['POST',])
def register_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully created new user'
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)



class ProfileList(ListModelMixin,GenericAPIView):
    '''
    List that allows you to view all the profiles
    '''

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def get(self, request, *args, **kwargs):
        '''
        Function that gives you a list of all the profiles
        '''
        return self.list(request,*args,*kwargs)

Uploader =  CloudinaryResourceHandler() 

class ProfileDetails(RetrieveAPIView, UpdateAPIView):
    '''
    View that allows you to access one profile on the list
    '''
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = ProfileSerializerwithoutUser
        return serializer_class

    def get_profile(self,pk):
        try:
            return Profile.objects.get(user=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self,request, pk, format=None):
        '''
        Function that retrieves specified post
        '''
        profile = self.get_profile(pk)


        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, pk, format = None):
        '''
        Function that allows user to update a profile
        '''
        
        payload = request.data
        image = Uploader.upload_image_from_request(request)
        payload['image'] = image

        profile = self.get_profile(pk)
        serializer = ProfileSerializerwithoutUser(instance=profile, data = payload, partial=True)


        if serializer.is_valid(raise_exception=True):
            profile = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 





class TokenObtainPairView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = TokenObtainPairSerializer


token_obtain_pair = TokenObtainPairView.as_view()




       
