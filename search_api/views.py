from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from search_api.models import Search
from search_api.serializers import SearchSerializer
from rest_framework import viewsets, generics, filters
from .pagination import *

# Create your views here.
class SearchListView(generics.ListAPIView):
    # Queryset to search upon
    queryset = Search.objects.all()
    # Serializer to use for data transfer
    serializer_class = SearchSerializer
    # Pagination settings
    pagination_class = ResultsPagination
    # Search Filter fields to query on
    search_fields = ["title", "description"]
    # Filters to apply to queryset
    filter_backends = (
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    )
    # Ordering fields (if any)
    ordering = "-published_at"
