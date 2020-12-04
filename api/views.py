from rest_framework import viewsets, filters, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemSerializer, SellerSerializer
from .models import Item, Seller
from .utilities import get_city_name, get_city_code


class SearchResponse(object):
    def __init__(self, user=None, **args):
        self.response = {
            "query": args.get('query', ''),
            "total": args.get('total', 0),
            "seller": args.get('seller', {}),
            "items": args.get('items', [])
        }


class SearchViewSet(viewsets.ViewSet):
    def list(self, request):
        itemsQueryset = Item.objects.all()
        search_word = self.request.query_params.get('q')
        if search_word is not None:
            itemsQueryset = itemsQueryset.filter(name__icontains=search_word)
        itemsSerializer = ItemSerializer(itemsQueryset, many=True)

        sellerQueryset = Seller.objects.all()
        sellerSerializer = SellerSerializer(sellerQueryset, many=True)

        items = list(map(lambda item: {
            "id": item["_id"],
            "name": item["name"],
            "brand": item["brand"],
            "thumbnail": item["thumbnail"],
            "city": {"name": get_city_name(item["city"]),
                     "code": get_city_code(item["city"])},
            "price": float(item["price"]),
            "currency": item["currency"],
            "rating": float(item["rating"]),
        }, itemsSerializer.data))
        seller = sellerSerializer.data[0]
        return Response({
            "query": search_word or "",
            "total": len(items),
            "seller": seller,
            "items": items,
        })

class ItemResponse(object):
    def __init__(self, user=None, **args):
        self.response = {
            "item": args.get('item', {})
        }

class ItemViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk):

        itemsQueryset = Item.objects.all()
        itemsSerializer = ItemSerializer(itemsQueryset, many=True)

        sellerQueryset = Seller.objects.all()
        sellerSerializer = SellerSerializer(sellerQueryset, many=True)
        seller = sellerSerializer.data[0]

        item = None
        for item_details in itemsSerializer.data:
            if item_details["_id"] == pk:
                item = item_details
                break

        if item is not None:
            res = {
                "id": item["_id"],
                "name": item["name"],
                "brand": item["brand"],
                "thumbnail": item["thumbnail"],
                "pictures": item["pictures"],
                "city": {"name": get_city_name(item["city"]),
                         "code": get_city_code(item["city"])},
                "seller": seller,
                "description": item["description"],
                "price": float(item["price"]),
                "currency": item["currency"],
                "rating": float(item["rating"]),
            }
            return Response(res, 200)
        else:
            return Response({"message": "item not found"}, 404)
