from django.urls import path

from admins.views import index, UserCreateView, UserListView, UserUpdateView, UserDeleteView, \
    ProductCreateView, ProductListView, ProductUpdateView, ProductDeleteView, \
    admin_categories_create, admin_categories, admin_categories_update, admin_categories_delete

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),
    path('products/', ProductListView.as_view(), name='admin_products'),
    path('products-create/', ProductCreateView.as_view(), name='admin_products_create'),
    path('products-update/<int:pk>/', ProductUpdateView.as_view(), name='admin_products_update'),
    path('products-delete/<int:pk>/', ProductDeleteView.as_view(), name='admin_products_delete'),
    path('categories/', admin_categories, name='admin_categories'),
    path('categories-create/', admin_categories_create, name='admin_categories_create'),
    path('categories-update/<int:id>/', admin_categories_update, name='admin_categories_update'),
    path('categories-delete/<int:id>/', admin_categories_delete, name='admin_categories_delete'),
]
