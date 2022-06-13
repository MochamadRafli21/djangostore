from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views
urlpatterns = [
    # category
    path('category/', views.categoryOverView, name="category"),
    path('category/create/', views.add_categorys, name='category-add'),
    path('category/list/', views.view_categorys, name="category-list"),
    path('category/<int:pk>/', views.detail_category, name='category-detail'),
    path('category/<int:pk>/update/', views.update_category, name='category-update'),
    path('category/<int:pk>/delete/', views.delete_category, name='category-delete'),
    # jwt endpoint
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # product
        path('product/', views.product_list, name="product-list"),
    path('product/create/', views.add_products, name='product-add'),
]