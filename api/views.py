from rest_framework import viewsets, filters
from .serializers import ItemSerializer, SellerSerializer
from .models import Item, Seller

class SearchViewSet(viewsets.ModelViewSet) :
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        sellers = Seller.objects.all()
        search_word = self.request.query_params.get('q')
        
        if search_word is not None:
            queryset = queryset.filter(name__icontains=search_word)

        return queryset
