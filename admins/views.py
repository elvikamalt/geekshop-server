from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from users.models import User
from products.models import Product, ProductCategory
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, ProductAdminCreateForm, \
    ProductCategoryAdminCreateForm


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'GeekShop - Админ Панель'}
    return render(request, 'admins/index.html', context)


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'


class UserCreateView(CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admins:admin_users')
    template_name = 'admins/admin-users-create.html'


class UserUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    template_name = 'admins/admin-users-update-delete.html'


# Create
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Пользователь успешно создан')
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminRegistrationForm()
#     context = {'title': 'GeekShop - Создание пользователя', 'form': form}
#     return render(request, 'admins/admin-users-create.html', context)


# Read
# @user_passes_test(lambda u: u.is_staff)
# def admin_users(request):
#     context = {
#         'title': 'GeekShop - Пользователи',
#         'users': User.objects.all(),
#     }
#     return render(request, 'admins/admin-users-read.html', context)


# Update
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_update(request, id):
#     selected_user = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Данные пользователя {selected_user.username} успешно обновлены')
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#
#     context = {
#         'title': 'GeekShop - Обновление пользователя',
#         'form': form,
#         'selected_user': selected_user,
#     }
#     return render(request, 'admins/admin-users-update-delete.html', context)


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
            messages.success(request, f'Продукт успешно добавлен')
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductAdminCreateForm()
    context = {'title': 'GeekShop - Добавление продукта', 'form': form}
    return render(request, 'admins/admin-products-create.html', context)


# Read products
@user_passes_test(lambda u: u.is_staff)
def admin_products(request):
    context = {
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
            messages.success(request, f'Данные продукта {selected_product.name} успешно обновлены')
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductAdminCreateForm(instance=selected_product)

    context = {
        'title': 'GeekShop - Редактирование продукта',
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


# Create category
@user_passes_test(lambda u: u.is_staff)
def admin_categories_create(request):
    if request.method == 'POST':
        form = ProductCategoryAdminCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Категория успешно добавлена')
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:
        form = ProductCategoryAdminCreateForm()
    context = {'title': 'GeekShop - Добавление категории', 'form': form}
    return render(request, 'admins/admin-categories-create.html', context)


# Read categories
@user_passes_test(lambda u: u.is_staff)
def admin_categories(request):
    context = {
        'title': 'GeekShop - Категории',
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'admins/admin-categories-read.html', context)


# Update category
@user_passes_test(lambda u: u.is_staff)
def admin_categories_update(request, id):
    selected_category = ProductCategory.objects.get(id=id)
    if request.method == 'POST':
        form = ProductCategoryAdminCreateForm(instance=selected_category, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Данные категории {selected_category.name} успешно обновлены')
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:
        form = ProductCategoryAdminCreateForm(instance=selected_category)

    context = {
        'title': 'GeekShop - Редактирование категории',
        'form': form,
        'selected_category': selected_category,
    }
    return render(request, 'admins/admin-categories-update-delete.html', context)


# Delete category
@user_passes_test(lambda u: u.is_staff)
def admin_categories_delete(request, id):
    category = ProductCategory.objects.get(id=id)
    category.delete()
    return HttpResponseRedirect(reverse('admins:admin_categories'))
