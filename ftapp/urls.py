from django.conf.urls import url
from ftapp import views

urlpatterns = [
   url(r'^index/',views.index),
   url(r'^index1/',views.index1),
   url(r'^index2/',views.index2),
   url(r'^shop/',views.shop),
   url(r'^detailsp1/',views.detailsp1),
   url(r'^detailsp2/$',views.detailsp2),
   url(r'^detailsp3/$',views.detailsp3),
   url(r'^detailsp4/$',views.detailsp4),
   url(r'^huoguo/$',views.huoguo),
   url(r'^tiandian/$',views.tiandian),
   url(r'^binggan/$',views.binggan),
   url(r'^zaocan/$',views.zaocan),
   url(r'^lingshi/$',views.lingshi),
    url('^register/$',views.register),
    url(r'^getname/$',views.getname),
    url(r'^getpwd/$',views.getpwd),
    url(r'^getnum/$',views.getnum),
    url(r'^submit/$',views.submit),
    url(r'^getlgcount/$',views.getlgcount),
    url(r'^getlgpassword/$',views.getlgpassword),
    url(r'^loginverify/$',views.loginverify),
    url(r'^Main/$',views.MainView),
    url(r'^111/$',views.dianji),
    url(r'^quzhi/$',views.quzhi)
]