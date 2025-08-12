from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('products/', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:product_id>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('products/info/', views.ProductInfoAPIView.as_view(), name='product-info'),
    path('users/', views.UserListView.as_view(), name='user-list'),
]

router = DefaultRouter()
router.register('orders', views.OrderViewSet)
urlpatterns += router.urls