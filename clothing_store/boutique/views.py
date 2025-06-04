from .serializers import ClothingItemSerializer
from django.shortcuts import render
from .models import ClothingItem
from rest_framework import viewsets


class ClothingItemViewSet(viewsets.ModelViewSet):
    queryset = ClothingItem.objects.all()
    serializers_class = ClothingItemSerializer


def catalog_view(request):
    items = ClothingItem.objects.all()
    return render(request, 'catalog.html', {'items': items})

def home(request):
    return render(request, 'home.html')