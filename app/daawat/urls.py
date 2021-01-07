from django.contrib import admin
from django.urls import path

from .views.home import Index 
from .views.signup import Signup
from .views.login import Login , logout
from .views.hotel import Hotel, generate_qr
from .views.food import Food, update_food, delete_food
from .views.category import Category
from .views.menu import Menu
# from .views.cart import Cart
# from .views.checkout import CheckOut
# from .views.orders import OrderView
# from .views.productdetails import ProductView
# from .views.allorders import AllOrders
# from .views.invoice import GeneratePDF
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    
    path('hotel', auth_middleware(Hotel.as_view()) , name='hotel'),
    path('food', auth_middleware(Food.as_view()) , name='food'),
    path('category', auth_middleware(Category.as_view()) , name='category'),
    path('update_food', auth_middleware(update_food) , name='update_food'),
    path('delete_food', auth_middleware(delete_food) , name='delete_food'),
    path('generate_qr', auth_middleware(generate_qr) , name='generate_qr'),

    path('<str:hotel_id>/<str:table_no>',Menu.as_view(),name="menu"),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    
    # path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    # path('check-out', CheckOut.as_view() , name='checkout'),
    # path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    # path('allorders', auth_middleware(AllOrders.as_view()) , name='allorders'),
    # path('productdetails', ProductView.as_view() , name='productdetails'),
    # path('invoice',GeneratePDF.as_view()  , name='invoice'),
]
