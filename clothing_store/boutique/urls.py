from django.urls import path, include
from .views import ClothingItemViewSet, home, RegisterAPIView
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'clothing', ClothingItemViewSet)



urlpatterns = [
    path('catalog', views.catalog_view, name='catalog'),
    path('api/', include(router.urls)),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('home/', home, name='home')
]



