from django.shortcuts import render,redirect
from django.views.generic import TemplateView,DetailView,ListView,DeleteView
from django.views import View
from account.models import products,Cart,Review,Orders
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from typing import Any


# Create your views here.

def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            return redirect("log")
    return inner

dec=[signin_required,never_cache]

@method_decorator(dec,name="dispatch")   
class UhomeView(TemplateView):
    template_name="uhome.html"

# CowProductsDetailsView
# class CowProductsDetailsView(DetailView):
#     template_name="cowproductsdetails.html"
# class CowProductsDetailsView(View):
#     def get(self,request):
#         return render(request,"cowproductsdetails.html")
    
# class GoatProductsDetailsView(View):
#     def get(self,request):
#         return render(request,"goatproductsdetails.html")

# class ChickenProductsDetailsView(View):
#     def get(self,request):
#         return render(request,"chickenproductsdetails.html")

# class PigProductsDetailsView(View):
#     def get(self,request):
#         return render(request,"pigproductsdetails.html")
    
# class DetailsView(TemplateView):
#     template_name="products.html"

# class DetailsView(DetailView):
#     template_name="products.html"
#     queryset=products.objects.all()
#     # pk_url_kwarg='pid'
#     context_object_name="product"
@method_decorator(dec,name="dispatch")   
class ProductsView(ListView):
    template_name="products.html"
    queryset=products.objects.all()
    context_object_name="products"

    def get_context_data(self, **kwargs):
        res=products.objects.filter(categories=self.kwargs.get('cat'))
        print(res)
        print(self.kwargs)
        return{"products":res}
    
@method_decorator(dec,name="dispatch")      
class DetailsView(DetailView):
    template_name="details.html"
    queryset=products.objects.all()
    pk_url_kwarg='pid'
    context_object_name="product"
    def get_context_data(self,**kwargs: Any):
        context=super().get_context_data(**kwargs)
        pid=self.kwargs.get('pid')
        product=products.objects.get(id=pid)
        rev=Review.objects.filter(product=product)
        context["reviews"]=rev
        return context

dec
def addtocart(request,*args,**kwargs):
    pid=kwargs.get("pid")
    pro=products.objects.get(id=pid)
    user=request.user
    Cart.objects.create(product=pro,user=user)
    return redirect('uhome')

@method_decorator(dec,name="dispatch")  
class CartListView(ListView):
    template_name="cartlist.html"
    queryset=Cart.objects.all()
    context_object_name="cart"

    def get_queryset(self):
        res=super().get_queryset()
        res=res.filter(user=self.request.user)
        return res

@method_decorator(dec,name="dispatch")  
class CartDeleteView(DeleteView):
    model=Cart
    success_url=reverse_lazy("lcart")
    template_name="deletecart.html"
    pk_url_kwarg="cid"

# dec
# def addreview(request,**kwargs):
#     review=request.POST.get("rev")
#     product_id=kwargs.get("pid")
#     user=request.user
#     product=products.objects.get(id=product_id)
#     print(review,product_id)
#     Review.objects.create(review=review,user=user,product=product)
#     return redirect("uhome")

dec
def addreview(request,**kwargs):
    review=request.POST.get("rev")
    product_id=kwargs.get("pid")
    user=request.user
    product=products.objects.get(id=product_id)
    print(review,product_id)
    Review.objects.create(review=review,user=user,product=product)
    # messages.success(request,"Review Added!!")
    return redirect("uhome")

@method_decorator(dec,name="dispatch")  
class PlaceOrderView(ListView):
    template_name="placeorder.html"
    queryset=Orders.objects.all()
    def post(self,request,*args,**kwargs):
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        cid=kwargs.get("cid")
        cart=Cart.objects.get(id=cid)
        product=cart.product
        user=request.user
        Orders.objects.create(product=product,user=user,address=address,phone=phone,order_status='Order Placed')
        Cart.status="Order Placed"
        cart.save()
        to_mail=request.user.email
        msg=f"Order for the product is Placed successfully!!Check your email account for more details!"
        from_mail="farmco968@gmail.com"
        subject="Order Confirmed"
        send_mail(subject,msg,from_mail,[to_mail])
        return redirect("uhome")

@method_decorator(dec,name="dispatch")    
class OrderListView(ListView):
    template_name="orderlist.html"
    queryset=Orders.objects.all()
    context_object_name="orders"

    def get_queryset(self):
        queryset=super().get_queryset()
        queryset=queryset.filter(user=self.request.user)
        return queryset

@method_decorator(dec,name="dispatch")  
class AnimalListView(TemplateView):
    template_name="animaldetails.html"

dec
def cancelorder(request,**kwargs):
    oid=kwargs.get('oid')
    order=Orders.objects.get(id=oid)
    Orders.order_status="Cancelled"
    order.delete()
    # mail service
    to_mail=request.user.email
    msg=f"Order for the product {order.product.title} is cancelled successfully!!Check your email account for more details!"
    from_mail="farmco968@gmail.com"
    subject="Order Cancellation Confirmed"
    send_mail(subject,msg,from_mail,[to_mail])
    return redirect('orl')


class RearingView(View):
    def get(self,request):
        return render(request,"rearing.html")