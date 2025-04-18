from django.contrib import admin
from django.urls import path

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from main.views import *

schema_view = get_schema_view(
    openapi.Info(
        title="Omborxona API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('Suv/', SuvListCreate.as_view()),
    path('Suv/<int:pk>/', SuvRetrieveUpdateDeleteAPIView.as_view()),
    path('mijoz/', MijozListCreate.as_view()),
    path('mijoz/<int:pk>/', MijozRetrieveUpdateDeleteAPIView.as_view()),
    path('buyurtma/', BuyurtmaListCreateAPIView.as_view()),
    path('sotuvchi/', SotuvchiListCreateAPIView.as_view()),
    path('haydovchi/', HaydovchiListAPIView.as_view()),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
