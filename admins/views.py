from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from users.models import User
from products.models import Product
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, ProductAdminCreateForm


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'GeekShop - Админ Панель'}
    return render(request, 'admins/index.html', context)


# Create
@user_passes_test(lambda u: u.is_staff)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {'title': 'GeekShop - Создание пользователя', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)


# Read
@user_passes_test(lambda u: u.is_staff)
def admin_users(request):
    context = {
        'title': 'GeekShop - Пользователи',
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)


# Update
@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)

    context = {
        'title': 'GeekShop - Обновление пользователя',
        'form': form,
        'selected_user': selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


# Delete
@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.safe_delete()
    return HttpResponseRedirect(reverse('admins:admin_users'))


# Create product
@user_passes_test(lambda u: u.is_staff)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductAdminCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductAdminCreateForm()
    context = {'title': 'GeekShop - Добавление продукта', 'form': form}
    return render(request, 'admins/admin-products-create.html', context)


# Read products
@user_passes_test(lambda u: u.is_staff)
def admin_products(request):
    context ={
        'title': 'GeekShop - Продукты',
        'products': Product.objects.all(),
    }
    return render(request, 'admins/admin-products-read.html', context)


# Update product
@user_passes_test(lambda u: u.is_staff)
def admin_products_update(request, id):
    selected_product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductAdminCreateForm(instance=selected_product, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductAdminCreateForm(instance=selected_product)

    context = {
        'title': 'GeekShop - Обновление продукта',
        'form': form,
        'selected_product': selected_product,
    }
    return render(request, 'admins/admin-products-update-delete.html', context)


# Delete product
@user_passes_test(lambda u: u.is_staff)
def admin_products_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect(reverse('admins:admin_products'))
