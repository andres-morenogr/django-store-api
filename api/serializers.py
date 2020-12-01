from rest_framework import serializers
from .models import Item, Seller

class ItemSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Item
        fields = ('name', 'data')

class SellerSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Seller
        fields = ('name', 'data')
