from rest_framework import permissions



class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Custom permission to allow owneers of posts to edit it.
    '''

    def has_object_permission(self,request,view,obj):
        '''
        read permissions are allowed
        '''
        
        if request.method in permissions.SAFE_METHODS:
            return True
        

        return obj.author == request.user



class IsUserStaff(permissions.BasePermission):
    '''
    permission to check if user is staff
    '''

    def has_permission(self,request,view):


        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff