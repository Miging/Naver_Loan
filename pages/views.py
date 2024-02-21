from django.shortcuts import render

from pages.models import MainContent


# Create your views here.

def mainpage(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request,'pages/mainpage.html',context)

def company(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request,'pages/company_info.html',context)

def service(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request,'pages/service_info.html',context)
def notice(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request,'pages/notice.html',context)

def customer(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request,'pages/customer_center.html',context)
