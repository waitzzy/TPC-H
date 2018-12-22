from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt

from DBHW import models
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger





def Region_list(request):
    region_list = models.Region.objects.all()
    return render(request, 'regionlist.html',{"region_list":region_list})

def Nation_list(request):
    nation_list = models.Nation.objects.all()
    paginator = Paginator(nation_list, 10)
    page = request.GET.get('page', 1)
    try:
        nation = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        nation = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        nation = paginator.page(paginator.num_pages)
    return render(request, 'nationlist.html', {"nation_list":nation})
@csrf_exempt
def Nation_Edit(request,nid):
    if request.method == "POST":
        nationkey = request.POST.get('n_nationkey')
        name = request.POST.get('n_name')
        regionkey = request.POST.get('n_regionkey')
        comment = request.POST.get('n_comment')
        models.Nation.objects.filter(n_nationkey=nid).update(n_nationkey=nationkey,n_name = name,n_regionkey =regionkey,n_comment =comment)
        return HttpResponseRedirect("/DBHW/nationlist/")
    else:
        obj = models.Nation.objects.filter(n_nationkey=nid).first()
        return render(request, 'nationedit.html', {"obj":obj})


def Nation_delete(request,nid):
        models.Nation.objects.filter(n_nationkey=nid).delete()
        return render(request, 'nationdelete.html')

@csrf_exempt
def Nation_view(request, nid):
        obj = models.Nation.objects.filter(n_nationkey=nid).first()
        return render(request, 'nationview.html', {"obj": obj})


@csrf_exempt
def Nation_add(request):
    if request.method == "POST":
        nationkey = request.POST.get('n_nationkey')
        name = request.POST.get('n_name')
        regionkey = request.POST.get('n_regionkey')
        comment = request.POST.get('n_comment')
        region = models.Region.objects.get(r_regionkey=regionkey)
        obj = models.Nation(n_nationkey=nationkey,n_name = name,n_regionkey =region,n_comment =comment)
        obj.save()
        return HttpResponseRedirect("/DBHW/nationlist/")
    else:
        return render(request, 'nationadd.html')


def Customer_list(request):
    customer_list = models.Customer.objects.all()
    paginator = Paginator(customer_list, 10)
    page = request.GET.get('page', 1)
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        customer = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        customer = paginator.page(paginator.num_pages)
    return render(request, 'customerlist.html', {"customer_list":customer})


@csrf_exempt
def Customer_Edit(request,nid):
    if request.method == "POST":
        custkey = request.POST.get('c_custkey')
        name = request.POST.get('c_name')
        address = request.POST.get('c_address')
        nationkey = request.POST.get('c_nationkey')
        phone = request.POST.get('c_phone')
        accbal = request.POST.get('c_acctbal')
        mktsegment = request.POST.get('c_mktsegment')
        comment = request.POST.get('c_comment')
        models.Customer.objects.filter(c_custkey=nid).update(c_custkey=custkey,c_name = name,c_address =address,c_nationkey =nationkey,
                                                           c_phone=phone,c_acctbal=accbal,c_mktsegment=mktsegment,c_comment=comment)
        return HttpResponseRedirect("/DBHW/customerlist/")
    else:
        obj = models.Customer.objects.filter(c_custkey=nid).first()
        return render(request, 'customeredit.html', {"obj":obj})

def Customer_delete(request, nid):
    models.Customer.objects.filter(c_custkey=nid).delete()
    return render(request, 'customerdelete.html')


@csrf_exempt
def Customer_view(request, nid):
    obj = models.Customer.objects.filter(c_custkey=nid).first()
    return render(request, 'customerview.html', {"obj": obj})


@csrf_exempt
def Customer_add(request):
    if request.method == "POST":
        custkey = request.POST.get('c_custkey')
        name = request.POST.get('c_name')
        address = request.POST.get('c_address')
        nationkey = request.POST.get('c_nationkey')
        phone = request.POST.get('c_phone')
        accbal = request.POST.get('c_acctbal')
        mktsegment = request.POST.get('c_mktsegment')
        comment = request.POST.get('c_comment')
        obj = models.Customer(c_custkey=custkey,c_name = name,c_address =address,c_nationkey =nationkey,
                                                           c_phone=phone,c_acctbal=accbal,c_mktsegment=mktsegment,c_comment=comment)
        obj.save()
        return HttpResponseRedirect("/DBHW/customerlist/")
    else:
        return render(request, 'customeredit.html')