from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt

from DBHW import models
from django.http import HttpResponseRedirect


def Customer_list(request):
    customer_list = models.Customer.objects.all()
    return render(request, 'customerlist.html', {"customer_list":customer_list})

def Nation_list(request):
    nation_list = models.Nation.objects.all()
    return render(request, 'nationlist.html', {"nation_list":nation_list})
@csrf_exempt
def Nation_Edit(request,nid):
    if request.method == "POST":
        print("the POST method")
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
        print("the POST method")
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