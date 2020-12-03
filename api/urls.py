from django.urls import include, path  
from rest_framework import routers  
from . import views  
  
router = routers.DefaultRouter()  
router.register(r'search', views.SearchViewSet, basename='Search')
  
urlpatterns = [  
    path('', include(router.urls)),  
    path('api/',
        include('rest_framework.urls',
        namespace='rest_framework'))  
]
