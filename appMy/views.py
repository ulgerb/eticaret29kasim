from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def Products(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    
    context = {
        "products": products,
        "categorys": categorys,
    }
    return render(request, 'products.html',context)

def Detail(request,id):
    product = Product.objects.get(id=id)
    comments = Comment.objects.filter(product=product)
    context = {
        "product": product,
        "comments": comments,
    }
    if request.method == "POST":
        if request.POST["button"] == "formComment" and request.user.is_authenticated():
            title = request.POST["title"]
            text = request.POST["text"]
            like = request.POST["like"]
            if like != "puan":
                comment = Comment(user=request.user,title=title,text=text,like=like,product=product)
                comment.save()
                return HttpResponseRedirect("/detail/"+id+"/")
            else:
                context.update({"hata": "Puanlama yapmadınız!"})
            
            
            
    
    
    return render(request,'detail.html',context)

def Shoping(request):
    return render(request,'shoping.html')