from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from search_api.models import Search
from search_api.serializers import SearchSerializer
from rest_framework import viewsets,generics
# Create your views here.

class SearchListView(generics.ListAPIView):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('title', 'description')