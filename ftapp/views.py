from django.shortcuts import render
from ftapp.models import Fantuan
from ftapp.models import Fantuan2
from ftapp.models import user
# Create your views here.


# def shop(request):
#     alli=Fantuan.objects.all()
#     iid=alli[0].id
#     ishop=alli[0].shop
#     iphoto=alli[0].photo
#     iaddress=alli[0].address
#     iphone=alli[0].phone
#     ifood=alli[0].food
#     ifood1 = ifood[0:4]
#     ifood2 = ifood[5:10]
#     ifood3 = ifood[11:16]
#     ifood4 = ifood[17:20]
#     itime=alli[0].time
#     irate=alli[0].rate
#     # print(ifood,ifood[0:4])
#     return render(request, 'shop1.html', {'iid':iid, 'ishop':ishop, 'iphoto':iphoto, 'iaddress':iaddress,
#                                        'iphone':iphone,'ifood':ifood,'itime':itime,'irate':irate,
#                                        'ifood1':ifood1,'ifood2':ifood2,'ifood3':ifood3,'ifood4':ifood4})


alli=Fantuan.objects.all()
allc=Fantuan2.objects.all()
def index(request):
    return render(request,'index.html',{'alli':alli})
def index1(request):
    return render(request,'index1.html',{'alli':alli})
def index2(request):
    return render(request,'index2.html',{'alli':alli})
def shop(request):
    si = int(request.GET.get('i'))
    return render(request,'shop.html',{'alli':alli[si],'allc':allc[si]})
def detailsp1(request):
    return render(request, 'detailsp1.html')
def detailsp2(request):
    return render(request, 'detailsp2.html')
def detailsp3(request):
    return render(request, 'detailsp3.html')
def detailsp4(request):
    return render(request, 'detailsp4.html')
def huoguo(request):
    return render(request,'huoguo.html',{'alli':alli})
def tiandian(request):
    return render(request,'tiandian.html',{'alli':alli})
def binggan(request):
    return render(request,'binggan.html',{'alli':alli})
def zaocan(request):
    return render(request,'zaocan.html',{'alli':alli})
def lingshi(request):
    return render(request,'lingshi.html',{'alli':alli})
# def change(request):
#     si=int(request.GET.get('i'))
#     return render(request,'shop1.html',{'si':si,'alli':alli[si]})

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from  ftapp.models import user
import json
import re
# Create your views here.
def login(request):
    return  render(request,'login.html')

def register(request):
    return  render(request,'register.html')


def getname(request):
    userObj=user.objects.all()
    namelist=[i.nickname for i in userObj]
    nickname=request.POST.get('nickname')
    expression=r'[\u4e00-\u9fbf]{2,4}$'
    if re.match(expression,nickname)==None:
        return JsonResponse({"status":"0"})


    elif nickname=="昵称":
        return JsonResponse({"status":"2"})
    else:
        return JsonResponse({"status":"3"})
    # return  HttpResponse()
def getpwd(request):
    password=request.POST['password']
    expression='[\w]{6,12}$'
    m=re.match(expression,password)

    if password=="":
        print("密码为空")
        return HttpResponse()
    if m!=None:
        return JsonResponse({"status":"1"})
    else:
        return JsonResponse({"status": "0"})

def getnum(request):
    num=request.POST['rg_num']
    expression='^1[3,5,7,8,9]\d{9}$'
    numobjs=user.objects.all()
    global numlist
    numlist=[i.num for i in numobjs]
    if int(num) in numlist:
        print("已被注册")
        return JsonResponse({"status":"3"})
    if num=="手机号":
        return JsonResponse({"status":"2"})
    if re.match(expression,num)!=None:
        return JsonResponse({'status':"1"})
    else:
        return JsonResponse({'status': "0"})

def submit(request):
    count=request.POST['count']
    password=request.POST['password']
    num=request.POST['num']
    if re.match(r'[\u4e00-\u9fbf]{2,4}$',count)!=None \
        and re.match(r"[\w]{6,12}$",password)!=None \
        and int(num) not in numlist \
        and re.match(r'^1[35789]\d{9}$',num)!=None:
        u1=user(nickname=count,password=password,num=num)
        u1.save()
        return JsonResponse({"status":"1"})
    else:
        return JsonResponse({"status": "0"})

def getlgcount(request):
    u1=user.objects.all()
    numlist=[ i.num for i in u1]
    inputNum=request.POST['lgcount']
    if re.match(r'^1[356789]\d{9}$',inputNum):
        if int(inputNum) in numlist:
            return JsonResponse({"status": "1"})
        else:
            return JsonResponse({"status": "2"})
    if inputNum=="":
        pass
    else:
        return JsonResponse({"status":"0"})

def getlgpassword(request):
    lgpassword=request.POST['lgpassword']
    print(lgpassword)
    if lgpassword=="":
        return JsonResponse({"status":"2"})
    if re.match(r'\w{6,12}',lgpassword):
        return JsonResponse({"status":"1"})
    else:
        return HttpResponse(json.dumps({"status":"0"}),content_type="application/json")

def loginverify(request):
    count=int(request.POST["lgcount"])
    password=request.POST["lgpassword"]
    print(str(count)+"+++++++++++"+password)
    if re.match(r'^1[356789]\d{9}$',str(count)):
        u1=user.objects.all()
        countlist=[i.num for i in u1]

        if count in countlist:
            nickname=user.objects.get(num=count).nickname
            print(nickname)
            if password == user.objects.get(num=count).password:
                return JsonResponse({"status":"1","nickname":nickname})
            else:
                return JsonResponse({"status":"2"})
        else:
            return JsonResponse({"status":"3"})
    else:
        print("账号格式错误")
        return JsonResponse({"status": "0"})

def MainView(request):
    return render(request,'Main.html')

def dianji(request):
    return render(request,'111.html')
def quzhi(request):
    num2=request.POST.get("phonenum")
    print(num2+"***********************")
    uname=user.objects.get(num=int(num2)).nickname
    return HttpResponse(uname)


