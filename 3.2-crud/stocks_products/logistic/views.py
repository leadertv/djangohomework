from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'description')
    pagination_class = StandardResultsSetPagination


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = (DjangoFilterBackend,)
    # Установите filterset_fields в соответствии с вашими полями
    filterset_fields = ['id', 'address']  # пример на основе наличия id и адреса
    pagination_class = StandardResultsSetPagination
