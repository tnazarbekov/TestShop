from .forms import UserAuthentication, RegisterForm, ContactForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('main:home')
        else:
            return messages.error(request, 'Ошибка регистрации')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserAuthentication(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:product_list')
    else:
        form = UserAuthentication()
    context = {
        'form': form
    }
    return render(request, 'main/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('main:product_list')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['surname'], form.cleaned_data['message'], 'tnazarbekov@bk.ru',
                             ['tima103@mail.ru'], fail_silently=False)
            if mail:
                messages.success(request, 'Ваше письмо ушло к нам на почту!')
                return redirect('main:product_list')
            else:
                messages.error(request, 'УПС! Что-то пошло не так!')
                return redirect('main:product_list')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'main/contact.html', context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'main/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'main/detail.html', {'product': product, 'cart_product_form': cart_product_form})


def delivery(request):
    return render(request, 'main/delivery.html')
