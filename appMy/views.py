from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
# Create your views here.

def index(request):
    categorys = Category.objects.all()
    products = Product.objects.filter(likes__gte= 3.4)
    # products = Product.objects.filter(likes__lte= 3.4)

    context = {
        "products": products,
        "categorys": categorys,
    }
    return render(request, 'index.html',context)

def Products(request,cid="all"):
    categorys = Category.objects.all()
    if cid == "all":
        products = Product.objects.all()
    else:
        category = Category.objects.get(id=cid)
        products = Product.objects.filter(category=category)
        
    
    context = {
        "products": products,
        "categorys": categorys,
    }
    return render(request, 'products.html',context)

def Detail(request,id):
    product = Product.objects.get(id=id)
    comments = Comment.objects.filter(product=product) # 0 yorum varken
    
    context = {
        "product": product,
        "comments": comments,
    }
    if request.method == "POST":
        if request.POST["button"] == "formComment" and request.user.is_authenticated:
            title = request.POST["title"]
            text = request.POST["text"]
            like = request.POST["like"]
            if like != "puan":
                comment = Comment(user=request.user,title=title,text=text,like=like,product=product)
                comment.save()
                
                comments = Comment.objects.filter(product=product) # 1 yorum var
                product.comments_number = len(comments)
                product.save()
                likes = 0
                for i in comments:
                    likes += i.like
                product.likes = round(likes / (len(comments)),1)
                product.save()
                
                return HttpResponseRedirect("/detail/"+id+"/")
            else:
                context.update({"hata": "Puanlama yapmadınız!"})
       
        # SEPET EKLEME
        if request.POST["button"] == "formShop":
            count = int(request.POST["count"])
            total_price = count * product.price
            if Shops.objects.filter(user=request.user, product=product).exists(): # ürün sepette var mı
                shopget = Shops.objects.filter(user=request.user).get(product=product) # ürün1
                
                shopget.count = count + shopget.count # count inputttan gelen adet sayısı + sepette olan adet
                shopget.total_price = total_price + shopget.total_price # hesaplanan fiyat + sepette olan fiyat
                shopget.save()
            else:
                shopBasket = Shops(count = count, total_price=total_price, user=request.user,product=product)
                shopBasket.save()
            return HttpResponseRedirect("/detail/"+id+"/")
    
    
    return render(request,'detail.html',context)

def Shoping(request):
    toplam = 0
    shops = Shops.objects.filter(user=request.user)

    if request.method == "POST":
        if request.POST.get("button") == "formUpdate":
            shopid = request.POST.get("shopid")
            count = request.POST.get("count")
            
            shop = shops.get(id=shopid)
            shop.count = int(count)
            shop.total_price = shop.product.price * int(count)
            shop.save()
            return redirect('Shoping')
            
    for i in shops:
        toplam += i.total_price
    
    context = {
        "shops":shops,
        "toplam": toplam,
    }
    return render(request,'shoping.html', context)

def shopingDelete(request,sid):
    shop = Shops.objects.get(id=sid)
    shop.delete()
    
    return redirect('Shoping')
