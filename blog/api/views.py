from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import *
from .serializers import *

from blog.models import *
from blango_auth.models import User


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    
    def get_serializer_class(self):
        return PostSerializer if self.action in ('list', 'create') else PostDetailSerializer


class UserDetail(generics.RetrieveAPIView):
    lookup_field = 'email'
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @action(methods=['get'], detail=True, name='Posts with the Tag')
    def posts(self, request, pk=None):
        return Response(PostSerializer(self.get_object().posts, many=True, 
                    context={"request": request}).data)