from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers, vary_on_cookie

from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from .permissions import *
from .serializers import *

from blog.models import *
from blango_auth.models import User


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    
    def get_serializer_class(self):
        return PostSerializer if self.action in ('list', 'create') else PostDetailSerializer

    @method_decorator(cache_page(120))
    def list(self, *args, **kwargs):
        return super(PostViewSet, self).list(*args, **kwargs)

    @method_decorator(cache_page(300))
    @method_decorator(vary_on_headers("Authorization", "Cookie"))
    @action(methods=['get'], detail=False, name='Posts by logged in User')
    def mine(self, request):
        if request.user.is_anonymous:
            raise PermissionDenied("Access Denied")
        return Response(PostSerializer(self.get_queryset().filter(author=self.user), many=True, context={'request': request}).data)

class UserDetail(generics.RetrieveAPIView):
    lookup_field = 'email'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @method_decorator(cache_page(300))
    def get(self, *args, **kwargs):
        return super(UserDetail, self).get(*args, **kwargs)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @method_decorator(cache_page(300))
    def list(self, *args, **kwargs):
        return super(TagViewSet, self).list(*args, **kwargs)

    @method_decorator(cache_page(300))
    def retrieve(self, *args, **kwargs):
        return super(TagViewSet, self).retrieve(*args, **kwargs)

    @action(methods=['get'], detail=True, name='Posts with the Tag')
    def posts(self, request, pk=None):
        return Response(PostSerializer(self.get_object().posts, many=True, 
                    context={"request": request}).data)