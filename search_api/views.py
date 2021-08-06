from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from search_api.models import Search
from search_api.serializers import SearchSerializer
from rest_framework import viewsets,generics,filters
from .pagination import *

class SearchListView(generics.ListAPIView):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    pagination_class = ResultsPagination
    search_fields = ['title','description']
    filter_backends = (filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter)
    ordering = ('-published_at')
    #filter_fields = ('title', 'description')