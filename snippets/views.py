from django.shortcuts import render
from snippets.permissions import IsOwnerOrReadOnly
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
import django_filters
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })




class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000



class SnippetViewSet(viewsets.ModelViewSet):
# class SnippetViewSet(generics.ListAPIView):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    pagination_class = StandardResultsSetPagination
    # permission_classes = (IsOwnerOrReadOnly,)

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    #     queryset = Snippet.objects.all()
    #     title = self.request.query_params.get('title', None)
    #     if title is not None:
    #         queryset = queryset.filter(title=title)
    #     return queryset

        #
    # @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     snippet = self.get_object()
    #     return Response(snippet.highlighted)
    #
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)