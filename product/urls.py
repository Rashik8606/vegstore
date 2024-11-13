

from django.urls import path
from . import views


urlpatterns = [
    path('shop/',views.product_list,name='shop'),
    path('product/add/', views.add_product, name='add_product'),  
    path('product/delete/<int:pk>', views.delete_product, name='delete_product'),
    path('product/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('shop/', views.shop, name='shop'), 
    path('cart/add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('cart/', views.cart, name='cart'),
    path('product/<int:pk>/', views.product_details, name='product_details'),
    # path('cart_item/', views.cart, name='cart_item'),
    path('display/',views.display,name='display'),
    

    path('update/', views.update_cart, name='update_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('cart/<Pk>',views.cart,name='cart1'),
    
    
    
]



