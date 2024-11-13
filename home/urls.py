from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('blog-single/',views.blog_single,name='blog-single'),
    path('blog/',views.blog,name='blog'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('emailsave/',views.email_sub,name='emailsave'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)