from rest_framework import viewsets, filters
from .serializers import ItemSerializer, SellerSerializer
from .models import Item, Seller

class SearchViewSet(viewsets.ModelViewSet) :
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class SellerViewSet(viewsets.ModelViewSet) :
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']