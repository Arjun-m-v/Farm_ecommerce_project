from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
        path('uhome',UhomeView.as_view(),name="uhome"),
        path('dtls/<str:cat>',ProductsView.as_view(),name="dtls"),
        path("det/<int:pid>",DetailsView.as_view(),name="det"),
        path("acart/<int:pid>",addtocart,name="acart"),
        path("lcart",CartListView.as_view(),name="lcart"),
        path("del/<int:cid>",CartDeleteView.as_view(),name="cdel"),
        path("phr/<int:cid>",PlaceOrderView.as_view(),name="por"),
        path("orl",OrderListView.as_view(),name="orl"),
        path("adtls",AnimalListView.as_view(),name="adtls"),
        path("codr/<int:oid>",cancelorder,name="codr"),
        path("addrw/<int:pid>",addreview,name="addr"),
        path("rear",RearingView.as_view(),name="rear"),


]