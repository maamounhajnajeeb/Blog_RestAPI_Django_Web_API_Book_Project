from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model

from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly # new

# Create your views here.

class PostsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, ) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly, ) # new
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
