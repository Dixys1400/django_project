from django.urls import path, include
from .views import ClothingItemViewSet, home, RegisterAPIView, UserProfileView
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
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('home/', home, name='home'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='user-profile')

]



