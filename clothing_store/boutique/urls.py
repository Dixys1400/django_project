from django.urls import path, include
from .views import ClothingItemViewSet, home
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'clothing', ClothingItemViewSet)



urlpatterns = [
    path('catalog', views.catalog_view, name='catalog'),
    path('api/', include(router.urls)),
    # path('register/', RegisterAPIView.as_view(), name='register'),
    path('home/', home, name='home'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]



