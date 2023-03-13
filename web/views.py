from django.shortcuts import render
from django.shortcuts import render
from .models import Property,Banner,Testimonial,Blog,Property1,professionals,Agent,professionalservices,services,brandspartners,Contact,Popularplaces

# Create your views here.
def Index(request):
    # banner =Banner.objects.all()
    
    context={
        'Property': Property.objects.all(),
        'Banner': Banner.objects.all(),
        'Services':services.objects.all(),
        'Testimonial':Testimonial.objects.all(),
        'Popularplaces':Popularplaces.objects.all(),
        'professionals':professionals.objects.all(),
        'blog':Blog.objects.all(),

    }
    return render(request,"web/index.html",context)


def About(request):
    context={
        'Testimonial':Testimonial.objects.all(),
        'agent':Agent.objects.all(),
        'services':services.objects.all(),
        'brandspartners':brandspartners.objects.all()
    }
    return render(request,"web/about.html",context)

def Services(request):
    context={
        'Testimonial':Testimonial.objects.all(),
        'professionalservices':professionalservices.objects.all()
    }
    return render(request,"web/services.html",context)


def Properties(request):
    context={
        'Property1': Property1.objects.all()
    }
    return render(request,"web/properties.html",context)


def contact(request):
        if request.method == 'POST':
             name = request.POST['name']
             email = request.POST['email']
             subject = request.POST['subject']
             phone = request.POST['phone']
             message = request.POST['message']

             contactform = Contact(name=name,email= email,subject=subject,phone=phone,message=message)
             contactform.save()
    
        return render(request, "web/contact.html")
            

    
    

    

def base(request):
    context={}
    return render (request,"web/partials/base.html",context)

def blog(request,id):
    blog=Blog.objects.get(id=id)
    context={
        'blog':blog,
    }
    return render(request,"web/blog.html",context)

# def blog_details(request):
#     context={}
#     return render ()