from django.shortcuts import render

from users.models import User


def index(request):
    context = {'title': 'GeekShop - Админ Панель'}
    return render(request, 'admins/index.html', context)


# Create
def admin_users_create(request):
    context = {'title': 'GeekShop - Создание пользователя'}
    return render(request, 'admins/admin-users-create.html', context)


# Read
def admin_users(request):
    context = {
        'title': 'GeekShop - Пользователи',
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)


# Update
def admin_users_update(request):
    context = {'title': 'GeekShop - Обновление пользователя'}
    return render(request, 'admins/admin-users-update-delete.html', context)


# Delete
def admin_users_delete(request):
    pass
