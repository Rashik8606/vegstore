from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ownerdescription
from product.models import Product

# Create your views here.


@login_required
def index(request):
    datas = ownerdescription.objects.all()
    cart = Product.objects.all()
    return render(request,'index.html',{'datas':datas,'cart':cart})

def about(request):
    return render(request,'about.html')

def blog_single(request):
    return render(request,'blog-single.html')

def blog(request):
    return render(request,'blog.html')



def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')





def wishlist(request):
    return render(request,'wishlist.html')

def profile_view(request):
    # Assuming you have a user object to get the profile information
    user = request.user  # Get the currently logged-in user
    context = {
        'user': user,  # Pass the user object to the template
    }
    return render(request, 'index.html', context)  # Render the profile template

from .models import Email_sub

def email_sub(request):
    if request.method == 'POST':
        email = request.POST['email']
        emailsave = Email_sub(email=email)
        emailsave.save()
    return render(request,'index.html')
