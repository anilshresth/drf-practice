from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self,request,view,obj):
        #read only permissons are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        #write permissions are allowd for only author of post
        return obj.author==request.user