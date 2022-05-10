from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.product_list, name='product_list'),
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('contact', views.contact, name='contact'),
    path('delivery', views.delivery, name='delivery'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'
         ),
    path('<int:id>/<slug:slug>', views.product_detail,
         name='product_detail')
]
