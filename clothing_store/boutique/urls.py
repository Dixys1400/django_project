from django.urls import path, include
from .views import ClothingItemViewSet, home
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clothing', ClothingItemViewSet)



urlpatterns = [
    path('catalog', views.catalog_view, name='catalog'),
    path('', include(router.urls)),
    path('home/', home, name='home')
]



