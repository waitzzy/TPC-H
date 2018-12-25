from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt

from DBHW import models
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re


def Customer_search(request):
    name = request.GET.get('name', '')
    if not name:
        error_msg = '请输入搜索关键字'
        return render(request, 'error.html', {'msg': error_msg})
    if name:
        obj = models.Customer.objects.filter(c_name__contains=name)
    return render(request, 'customerlist.html', {
        'customer_list': obj,
    })


def Nation_search(request):
    name = request.GET.get('name', '')
    if not name:
        error_msg = '请输入搜索关键字'
        return render(request, 'error.html', {'msg': error_msg})
    if name:
        obj = models.Nation.objects.filter(n_name__contains=name)
    return render(request, 'Nationlist.html', {
        'nation_list': obj,
    })


def Region_search(request):
    name = request.GET.get('name', '')
    if not name:
        error_msg = '请输入搜索关键字'
        return render(request, 'error.html', {'msg': error_msg})
    if name:
        obj = models.Region.objects.filter(r_name__contains=name)
    return render(request, 'regionlist.html', {
        'region_list': obj,
    })


def Part_search(request):
    name = request.GET.get('name', '')
    if not name:
        error_msg = '请输入搜索关键字'
        return render(request, 'error.html', {'msg': error_msg})
    if name:
        obj = models.Part.objects.filter(p_name__contains=name)
    return render(request, 'partlist.html', {
        'part_list': obj,
    })


def Supplier_search(request):
    name = request.GET.get('name', '')
    if not name:
        error_msg = '请输入搜索关键字'
        return render(request, 'error.html', {'msg': error_msg})
    if name:
        obj = models.Supplier.objects.filter(s_name__contains=name)
    return render(request, 'supplierlist.html', {
        'supplier_list': obj,
    })


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
    try:
        if request.method == "POST":
            nationkey = request.POST.get('n_nationkey')

            nation_regex = r"^\d+$"#nationkey整数判断
            p = re.compile(nation_regex)
            if not p.match(nationkey):
                return render(request, "error.html", {"msg": "国家编号必须是正整数，编辑失败!"})

            name = request.POST.get('n_name')
            regionkey = request.POST.get('n_regionkey')
            comment = request.POST.get('n_comment')
            models.Nation.objects.filter(n_nationkey=nid).update(n_nationkey=nationkey,n_name = name,n_regionkey =regionkey,n_comment =comment)
            return HttpResponseRedirect("/DBHW/nationlist/")

        else:
            obj = models.Nation.objects.filter(n_nationkey=nid).first()
            region_list = models.Region.objects.all().values_list('r_regionkey', 'r_name')
            # 一般返回objects .values_list返回字典 .value返回元组#
            return render(request, 'nationedit.html', {"obj": obj, "region_list": region_list})
    except:
        return render(request,"error.html",{"msg":"您的输入有误，编辑失败!"})


def Nation_delete(request,nid):
    try:
        models.Nation.objects.filter(n_nationkey=nid).delete()
        return render(request, 'nationdelete.html')
    except:
        return render(request, "error.html", {"msg": "删除失败！"})

@csrf_exempt
def Nation_view(request, nid):
        obj = models.Nation.objects.filter(n_nationkey=nid).first()
        return render(request, 'nationview.html', {"obj": obj})


@csrf_exempt
def Nation_add(request):
    try:
        if request.method == "POST":
            nationkey = request.POST.get('n_nationkey')

            nation_regex = r"^\d+$"#nationkey整数判断
            p = re.compile(nation_regex)
            if not p.match(nationkey):
                return render(request, "error.html", {"msg": "国家编号必须是正整数，增加失败!"})

            name = request.POST.get('n_name')
            regionkey = request.POST.get('n_regionkey')
            comment = request.POST.get('n_comment')
            region = models.Region.objects.get(r_regionkey=regionkey)
            obj = models.Nation(n_nationkey=nationkey,n_name = name,n_regionkey =region,n_comment =comment)
            obj.save()
            return HttpResponseRedirect("/DBHW/nationlist/")
        else:
            region_list = models.Region.objects.all().values_list('r_regionkey', 'r_name')
            # 一般返回objects .values返回字典 .value_list返回元组#
            print(region_list)
            return render(request, 'nationadd.html', {"region_list": region_list})
    except:
        return render(request, "error.html", {"msg": "您的输入有误，增加失败!"})


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
    try:
        if request.method == "POST":
            custkey = request.POST.get('c_custkey')
            name = request.POST.get('c_name')
            address = request.POST.get('c_address')
            nationkey = request.POST.get('c_nationkey')
            phone = request.POST.get('c_phone')

            mobile_regex = r'^1[34578]\d{9}$'
            p=re.compile(mobile_regex)
            if not p.match(phone):
                return render(request, "error.html", {"msg": "请输入正确的联系方式"})

            accbal = request.POST.get('c_acctbal')
            if accbal == "":
                accbal = "0"

            accbal_regex = r'^[+]{0,1}(\d+)$|^[+]{0,1}(\d+\.\d+)$'
            p=re.compile(accbal_regex)
            if not p.match(accbal):
                return render(request, "error.html", {"msg": "请输入正确的可用余额"})

            mktsegment = request.POST.get('c_mktsegment')
            comment = request.POST.get('c_comment')
            models.Customer.objects.filter(c_custkey=nid).update(c_custkey=custkey,c_name = name,c_address =address,c_nationkey =nationkey,
                                                                   c_phone=phone,c_acctbal=accbal,c_mktsegment=mktsegment,c_comment=comment)
            return HttpResponseRedirect("/DBHW/customerlist/")

        else:
            obj = models.Customer.objects.filter(c_custkey=nid).first()
            nation_list = models.Nation.objects.all().values_list("n_nationkey", "n_name")
            return render(request, 'customeredit.html', {"obj": obj, "nation_list": nation_list})
    except:
        return render(request,"error.html",{"msg":"您的输入有误，编辑失败！"})

def Customer_delete(request, nid):
    try:
        models.Customer.objects.filter(c_custkey=nid).delete()
        return render(request, 'customerdelete.html')
    except:
        return render(request,"error.html",{"msg":"删除失败！"})


@csrf_exempt
def Customer_view(request, nid):
    obj = models.Customer.objects.filter(c_custkey=nid).first()
    return render(request, 'customerview.html', {"obj": obj})


@csrf_exempt
def Customer_add(request):
    try:
        if request.method == "POST":
            custkey = request.POST.get('c_custkey')
            name = request.POST.get('c_name')
            address = request.POST.get('c_address')
            nationkey = request.POST.get('c_nationkey')
            phone = request.POST.get('c_phone')

            mobile_regex = r'^1[34578]\d{9}$'
            p=re.compile(mobile_regex)
            if not p.match(phone):
                return render(request, "error.html", {"msg": "请输入正确的联系方式"})

            accbal = request.POST.get('c_acctbal')
            if accbal =='':
                accbal = "0"

            accbal_regex = r'^[+]{0,1}(\d+)$|^[+]{0,1}(\d+\.\d+)$'
            p = re.compile(accbal_regex)
            if not p.match(accbal):
                return render(request, "error.html", {"msg": "请输入正确的可用余额"})

            mktsegment = request.POST.get('c_mktsegment')
            comment = request.POST.get('c_comment')
            nation = models.Nation.objects.get(n_nationkey=nationkey)
            obj = models.Customer(c_custkey=custkey,c_name = name,c_address =address,c_nationkey =nation,
                                  c_phone=phone,c_acctbal=accbal,c_mktsegment=mktsegment,c_comment=comment)
            obj.save()
            return HttpResponseRedirect("/DBHW/customerlist/")
        else:
            nation_list = models.Nation.objects.all().values_list("n_nationkey", "n_name")
            return render(request, 'customeradd.html', {"nation_list": nation_list})
    except:
        return render(request,"error.html",{"msg":"您的输入有误，添加失败！"})

def Lineitem_list(request):
    lineitem_list = models.Lineitem.objects.all()
    paginator = Paginator(lineitem_list, 10)
    page = request.GET.get('page', 1)
    try:
        lineitem = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        lineitem = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        lineitem = paginator.page(paginator.num_pages)
    return render(request, 'lineitemlist.html', {"lineitem_list":lineitem})

@csrf_exempt
def Lineitem_Edit(request,nid,uid):

        if request.method == "POST":
            orderkey = request.POST.get('l_orderkey')
            partkey = request.POST.get('l_partkey')
            suppkey = request.POST.get('l_suppkey')
            tem_partkey = request.POST.get('l_partkey')
            tem_suppkey = request.POST.get('l_suppkey')
            partsupp = models.Partsupp.objects.filter(ps_partkey=tem_partkey, ps_suppkey=tem_suppkey)
            print(partsupp)
            if partsupp.count()==0:
                return render(request,"error.html",{"msg":"零件供应表中没有该组合"})
            linenumber = request.POST.get('l_linenumber')
            quantity = request.POST.get('l_quantity')
            if quantity =="":
                quantity = "0"

            partkey = models.Part.objects.get(p_partkey=tem_partkey)
            extendedprice = partkey.p_retailprice * float(quantity)

            discount = request.POST.get('l_discount')
            if discount =="":
                discount = "0"
            tax = request.POST.get('l_tax')
            if tax =="":
                tax ="0"

            number_regex = r'^[+]{0,1}(\d+)$|^[+]{0,1}(\d+\.\d+)$'
            p = re.compile(number_regex)
            if not p.match(tax):
                return render(request, "error.html", {"msg": "请输入正确的税"})
            if not p.match(discount):
                return render(request, "error.html", {"msg": "请输入正确的折扣"})
            if not p.match(quantity):
                return render(request, "error.html", {"msg": "请输入正确的数量"})

            returnflag = request.POST.get('l_returnflag')
            linestatus = request.POST.get('l_linestatus')
            shipdate = request.POST.get('l_shipdate')
            commitdate = request.POST.get('l_commitdate')
            receiptdate = request.POST.get('l_receiptdate')
            shipinstruct = request.POST.get('l_shipinstruct')
            shipmode = request.POST.get('l_shipmode')
            comment = request.POST.get('l_comment')
            obj1 = models.Orders.objects.get(o_orderkey=nid)
            obj2 = models.Lineitem.objects.get(l_linenumber=uid,l_orderkey=nid)
            tem = float(extendedprice) - obj2.l_extendedprice       # 变化量
            sum = obj1.o_totalprice + tem         #母订单总金额
            models.Lineitem.objects.filter(l_linenumber=uid,l_orderkey=nid).update(l_orderkey=orderkey,l_partkey = partkey,l_suppkey =suppkey,
                                                                l_linenumber =linenumber,l_quantity=quantity,l_extendedprice=extendedprice,
                                                                l_discount=discount,l_tax=tax,l_returnflag=returnflag,l_linestatus=linestatus,
                                                                l_shipdate=shipdate,l_commitdate=commitdate,l_receiptdate=receiptdate,l_shipinstruct=shipinstruct,
                                                                l_shipmode=shipmode,l_comment=comment)
            models.Orders.objects.filter(o_orderkey=nid).update(o_totalprice=sum)
            return HttpResponseRedirect("/DBHW/lineitemlist/")
        else:
            obj = models.Lineitem.objects.filter(l_orderkey=nid,l_linenumber=uid).first()
            part_list = models.Part.objects.all().values_list("p_partkey", "p_name")
            supplier_list = models.Supplier.objects.all().values_list("s_suppkey", "s_name")
            order_list = models.Orders.objects.all().values_list("o_orderkey")
            return render(request, 'lineitemedit.html',
                          {"obj": obj, "part_list": part_list, "supplier_list": supplier_list,"order_list":order_list})





def Lineitem_delete(request, nid,uid):
    obj1 = models.Orders.objects.get(o_orderkey=nid)
    obj2 = models.Lineitem.objects.get(l_linenumber=uid,l_orderkey=nid)
    sum = obj1.o_totalprice - obj2.l_extendedprice
    models.Orders.objects.filter(o_orderkey=nid).update(o_totalprice=sum)
    models.Lineitem.objects.filter(l_linenumber=uid).delete()
    return render(request, 'lineitemdelete.html')


@csrf_exempt
def Lineitem_view(request, nid,uid):
    obj = models.Lineitem.objects.filter(l_linenumber=uid,l_orderkey=nid).first()
    return render(request, 'lineitemview.html', {"obj": obj})

@csrf_exempt
def Lineitem_Add(request):
    try:
        if request.method == "POST":
            orderkey = request.POST.get('l_orderkey')
            tem_partkey = request.POST.get('l_partkey')
            tem_suppkey = request.POST.get('l_suppkey')
            partsupp = models.Partsupp.objects.filter(ps_partkey=tem_partkey,ps_suppkey=tem_suppkey)
            if partsupp.count()==0:
                return render(request, "error.html", {"msg": "零件供应表中没有该组合"})

            linenumber = request.POST.get('l_linenumber')
            quantity = request.POST.get('l_quantity')
            if quantity == '':
                quantity = "0"

            partkey = models.Part.objects.get(p_partkey=tem_partkey)
            suppkey = models.Supplier.objects.get(s_suppkey=tem_suppkey)
            extendedprice = partkey.p_retailprice * float(quantity)

            discount = request.POST.get('l_discount')
            if discount == '':
                discount = "0"
            tax = request.POST.get('l_tax')
            if tax == '':
                tax = "0"

            number_regex = r'^[+]{0,1}(\d+)$|^[+]{0,1}(\d+\.\d+)$'
            p = re.compile(number_regex)
            if not p.match(tax):
                return render(request, "error.html", {"msg": "请输入正确的税"})
            if not p.match(discount):
                return render(request, "error.html", {"msg": "请输入正确的折扣"})

            if not p.match(quantity):
                return render(request, "error.html", {"msg": "请输入正确的数量"})

            returnflag = request.POST.get('l_returnflag')
            linestatus = request.POST.get('l_linestatus')
            shipdate = request.POST.get('l_shipdate')
            commitdate = request.POST.get('l_commitdate')
            receiptdate = request.POST.get('l_receiptdate')
            shipinstruct = request.POST.get('l_shipinstruct')
            shipmode = request.POST.get('l_shipmode')
            comment = request.POST.get('l_comment')
            obj1 = models.Orders.objects.get(o_orderkey=orderkey)
            sum = obj1.o_totalprice + float(extendedprice)
            obj = models.Lineitem(l_orderkey=orderkey, l_linenumber=linenumber, l_partkey = partkey,l_suppkey=suppkey,
                                                                l_quantity=quantity,l_extendedprice=extendedprice,
                                                                l_discount=discount,l_tax=tax,l_returnflag=returnflag,l_linestatus=linestatus,
                                                                l_shipdate=shipdate,l_commitdate=commitdate,l_receiptdate=receiptdate,l_shipinstruct=shipinstruct,
                                                                l_shipmode=shipmode,l_comment=comment)
            obj.save()
            models.Orders.objects.filter(o_orderkey=orderkey).update(o_totalprice=sum)
            return HttpResponseRedirect("/DBHW/lineitemlist/")
        else:
            order_list = models.Orders.objects.all().values_list("o_orderkey")
            part_list = models.Part.objects.all().values_list("p_partkey", "p_name")
            supplier_list = models.Supplier.objects.all().values_list("s_suppkey", "s_name")
            return render(request, 'lineitemadd.html', {"part_list": part_list, "supplier_list": supplier_list,"order_list":order_list})
    except:
        return render(request,"error.html",{"msg":"您的输入有误，添加失败！"})

def Order_list(request):
    order_list = models.Orders.objects.all()
    paginator = Paginator(order_list, 10)
    page = request.GET.get('page', 1)
    try:
        order = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        order = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        order = paginator.page(paginator.num_pages)
    return render(request, 'orderlist.html', {"order_list":order})

@csrf_exempt
def Order_Add(request):
    try:
        if request.method == "POST":
            orderkey = request.POST.get('o_orderkey')
            tem_custkey = request.POST.get('o_custkey')
            custkey = models.Customer.objects.get(c_custkey=tem_custkey)
            orderstatus = request.POST.get('o_orderstatus')
            orderdate = request.POST.get('o_orderdate')
            orderpriority = request.POST.get('o_orderpriority')
            clerk = request.POST.get('o_clerk')
            shippriority = request.POST.get('o_shippriority')
            if shippriority =='':
                shippriority = "0"
            comment = request.POST.get('o_comment')
            obj = models.Orders(o_orderkey=orderkey,o_custkey = custkey,o_orderstatus =orderstatus,
                                                                o_totalprice =0,o_orderdate=orderdate,o_orderpriority=orderpriority,
                                                                o_clerk=clerk,o_shippriority=shippriority,o_comment=comment)
            #不允许用户直接写订单总金额
            obj.save()
            return HttpResponseRedirect("/DBHW/orderlist/")
        else:
            customer_list = models.Customer.objects.all().values_list('c_custkey','c_name')
            return render(request, 'orderadd.html',{'customer_list':customer_list})
    except:
        return render(request,"error.html",{"msg":"您的输入有误，添加失败！"})

def Order_delete(request, nid):
    try:
        models.Orders.objects.filter(o_orderkey=nid).delete()
        models.Lineitem.objects.filter(l_orderkey=nid).delete()
        return render(request, 'orderdelete.html')
    except:
        return render(request,"error.html",{"msg":"删除失败！"})

@csrf_exempt
def Order_view(request, nid):
    obj = models.Orders.objects.filter(o_orderkey=nid).first()
    return render(request, 'orderview.html', {"obj": obj})


def Part_list(request):
    part_list = models.Part.objects.all()
    paginator = Paginator(part_list, 10)
    page = request.GET.get('page', 1)
    try:
        part = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        part = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        part = paginator.page(paginator.num_pages)
    return render(request, 'partlist.html', {"part_list":part})

@csrf_exempt
def Part_Edit(request,nid):
    try:
        if request.method == "POST":
            partkey = request.POST.get('p_partkey')
            name = request.POST.get('p_name')
            emfgr = request.POST.get('p_emfgr')
            brand = request.POST.get('p_brand')
            type = request.POST.get('p_type')
            size = request.POST.get('p_size')
            if size == '':
                size = "0"
            container = request.POST.get('p_container')
            retailprice = request.POST.get('p_retailprice')
            if retailprice == '':
                retailprice = "0"

            number_regex = r'^[+]{0,1}(\d+)$|^[+]{0,1}(\d+\.\d+)$'
            p = re.compile(number_regex)
            if not p.match(retailprice):
                return render(request, "error.html", {"msg": "请输入正确的零售价"})

            comment = request.POST.get('p_comment')
            models.Part.objects.filter(p_partkey=nid).update(p_partkey=partkey,p_name = name,p_emfgr=emfgr,
                                                                p_brand =brand,p_type=type,p_size=size,
                                                                p_container=container,p_retailprice=retailprice,p_comment=comment)
            return HttpResponseRedirect("/DBHW/partlist/")
        else:
            obj = models.Part.objects.filter(p_partkey=nid).first()
            return render(request, 'partedit.html', {"obj":obj})
    except:
        return render(request,"error.html",{"msg":"您的输入有误，编辑失败！"})


def Part_delete(request, nid):
    try:
        models.Part.objects.filter(p_partkey=nid).delete()
        return render(request, 'partdelete.html')
    except:
        return render(request, "error.html", {"msg": "删除失败！"})


@csrf_exempt
def Part_view(request, nid):
    obj = models.Part.objects.filter(p_partkey=nid).first()
    return render(request, 'partview.html', {"obj": obj})

@csrf_exempt
def Part_Add(request):
    try:
        if request.method == "POST":
            partkey = request.POST.get('p_partkey')
            name = request.POST.get('p_name')
            emfgr = request.POST.get('p_emfgr')
            brand = request.POST.get('p_brand')
            type = request.POST.get('p_type')
            size = request.POST.get('p_size')
            if size == '':
                size=0
            container = request.POST.get('p_container')
            retailprice = request.POST.get('p_retailprice')
            if retailprice == '':
                retailprice="0"

            number_regex = r'^[+]{0,1}(\d+)$|^[+]{0,1}(\d+\.\d+)$'
            p = re.compile(number_regex)
            if not p.match(retailprice):
                return render(request, "error.html", {"msg": "请输入正确的零售价"})

            comment = request.POST.get('p_comment')
            obj = models.Part(p_partkey=partkey,p_name = name,p_emfgr=emfgr,
                             p_brand =brand,p_type=type,p_size=size,
                             p_container=container,p_retailprice=retailprice,p_comment=comment)
            obj.save()
            return HttpResponseRedirect("/DBHW/partlist/")
        else:
            return render(request, 'partadd.html')
    except:
        return render(request, "error.html", {"msg": "您的输入有误，添加失败！"})


def Partsupp_list(request):
    partsupp_list = models.Partsupp.objects.all()
    paginator = Paginator(partsupp_list, 10)
    page = request.GET.get('page', 1)
    try:
        partsupp = paginator.page(page)
    except PageNotAnInteger:
        partsupp = paginator.page(1)
    except EmptyPage:
        partsupp = paginator.page(paginator.num_pages)
    return render(request, 'partsupplist.html', {"partsupp_list":partsupp})

@csrf_exempt
def Partsupp_Edit(request,nid,uid):
    try:
        if request.method == "POST":
            tem_partkey = request.POST.get('ps_partkey')
            tem_suppkey = request.POST.get('ps_suppkey')
            partkey = models.Part.objects.get(p_partkey=tem_partkey)
            suppkey = models.Supplier.objects.get(s_suppkey=tem_suppkey)
            availqty = request.POST.get('ps_availqty')
            if availqty =="":
                availqty = "0"
            ava_regex = r'^\d+$'
            p = re.compile(ava_regex)
            if not p.match(availqty):
                return render(request, "error.html", {"msg": "请输入正确的数量"})
            supplycost = tem_partkey.p_retailprice * float(availqty)
            '''
            supplycost = request.POST.get('ps_supplycost')
            number_regex = r'^[+]{0,1}(\d+)$|^[+]{0,1}(\d+\.\d+)$'
            p = re.compile(number_regex)
            if not p.match(supplycost):
                return render(request, "error.html", {"msg": "请输入正确的供应价格"})
            '''
            comment = request.POST.get('ps_comment')

            models.Partsupp.objects.filter(ps_partkey=nid).update(ps_partkey=partkey, ps_suppkey =suppkey,ps_availqty=availqty,
                                                             ps_supplycost =supplycost,ps_comment=comment)
            return HttpResponseRedirect("/DBHW/partsupplist/")
        else:
            obj = models.Partsupp.objects.filter(ps_partkey=nid,ps_suppkey=uid).first()
            part_list = models.Part.objects.all().values_list("p_partkey", "p_name")
            supplier_list = models.Supplier.objects.all().values_list("s_suppkey", "s_name")
            return render(request, 'partsuppedit.html',
                          {"obj": obj, "part_list": part_list, "supplier_list": supplier_list})
    except:
        return render(request, "error.html", {"msg": "您的输入有误，添加失败！"})


def Partsupp_delete(request, nid,uid):
    try:
        models.Partsupp.objects.filter(ps_partkey=nid,ps_suppkey=uid).delete()
        return render(request, 'partsuppdelete.html')
    except:
        return render(request, "error.html", {"msg": "删除失败！"})

@csrf_exempt
def Partsupp_Add(request):
    try:
        if request.method == "POST":
            tem_partkey = request.POST.get('ps_partkey')
            partkey = models.Part.objects.get(p_partkey=tem_partkey)
            tem_suppkey = request.POST.get('ps_suppkey')
            suppkey = models.Supplier.objects.get(s_suppkey=tem_suppkey)
            availqty = request.POST.get('ps_availqty')
            if availqty =='':
                availqty = "0"
            ava_regex = r'^\d+$'
            p = re.compile(ava_regex)
            if not p.match(availqty):
                return render(request, "error.html", {"msg": "请输入正确的数量"})
            supplycost = partkey.p_retailprice * float(availqty)
            '''
            number_regex = r'^[+]{0,1}(\d+)$|^[+]{0,1}(\d+\.\d+)$'
            p = re.compile(number_regex)
            if not p.match(supplycost):
                return render(request, "error.html", {"msg": "请输入正确的供应价格"})
            '''
            comment = request.POST.get('ps_comment')
            obj = models.Partsupp(ps_partkey=partkey, ps_suppkey =suppkey,ps_availqty=availqty,
                                                             ps_supplycost =supplycost,ps_comment=comment)
            obj.save()
            return HttpResponseRedirect("/DBHW/partsupplist/")
        else:
            part_list = models.Part.objects.all().values_list("p_partkey", "p_name")
            supplier_list = models.Supplier.objects.all().values_list("s_suppkey", "s_name")
            return render(request, 'partsuppadd.html', {"part_list": part_list, "supplier_list": supplier_list})
    except:
        return render(request, "error.html", {"msg": "您的输入有误，添加失败！"})

@csrf_exempt
def Partsupp_view(request, nid,uid):
    obj = models.Partsupp.objects.filter(ps_partkey=nid,ps_suppkey=uid).first()
    return render(request, 'partsuppview.html', {"obj": obj})

def Region_list(request):
    region_list = models.Region.objects.all()
    paginator = Paginator(region_list, 10)
    page = request.GET.get('page', 1)
    try:
        region = paginator.page(page)
    except PageNotAnInteger:
        region = paginator.page(1)
    except EmptyPage:
        region = paginator.page(paginator.num_pages)
    return render(request, 'regionlist.html', {"region_list":region})


@csrf_exempt
def Region_Edit(request,nid):
    try:
        if request.method == "POST":
            regionkey = request.POST.get('r_regionkey')
            name = request.POST.get('r_name')
            comment1 = request.POST.get('r_comment')
            supplycost = request.POST.get('ps_supplycost')
            if supplycost == "":
                supplycost = "0"

            number_regex = r'^[+]{0,1}(\d+)$|^[+]{0,1}(\d+\.\d+)$'
            p = re.compile(number_regex)
            if not p.match(supplycost):
                return render(request, "error.html", {"msg": "请输入正确的供应价格"})

            comment2 = request.POST.get('ps_comment')
            models.Region.objects.filter(r_regionkey=nid).update(r_regionkey=regionkey,r_name = name,r_comment=comment1,
                                                             ps_supplycost =supplycost,ps_comment=comment2)
            return HttpResponseRedirect("/DBHW/regionlist/")
        else:
            obj = models.Region.objects.filter(r_regionkey=nid).first()
            return render(request, 'regionedit.html', {"obj":obj})
    except:
        return render(request, "error.html", {"msg": "您的输入有误，编辑失败！"})

def Region_delete(request, nid):
    try:
        models.Region.objects.filter(r_regionkey=nid).delete()
        return render(request, 'regiondelete.html')
    except:
        return render(request, "error.html", {"msg": "删除失败！"})


@csrf_exempt
def Region_view(request, nid):
    obj = models.Region.objects.filter(r_regionkey=nid).first()
    return render(request, 'regionview.html', {"obj": obj})

@csrf_exempt
def Region_Add(request):
    try:
        if request.method == "POST":
            regionkey = request.POST.get('r_regionkey')
            name = request.POST.get('r_name')
            comment1 = request.POST.get('r_comment')
            supplycost = request.POST.get('ps_supplycost')
            if supplycost =='':
                supplycost = "0"

            number_regex = r'^[+]{0,1}(\d+)$|^[+]{0,1}(\d+\.\d+)$'
            p = re.compile(number_regex)
            if not p.match(supplycost):
                return render(request, "error.html", {"msg": "请输入正确的供应价格"})

            comment2 = request.POST.get('ps_comment')
            obj = models.Region(r_regionkey=regionkey,r_name = name,r_comment=comment1,
                                                             ps_supplycost =supplycost,ps_comment=comment2)
            obj.save()
            return HttpResponseRedirect("/DBHW/regionlist/")
        else:
            return render(request, 'regionadd.html')
    except:
        return render(request, "error.html", {"msg": "您的输入有误，添加失败！"})


def Supplier_list(request):
    supplier_list = models.Supplier.objects.all()
    paginator = Paginator(supplier_list, 10)
    page = request.GET.get('page', 1)
    try:
        supplier = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        supplier = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        supplier = paginator.page(paginator.num_pages)
    return render(request, 'supplierlist.html', {"supplier_list":supplier})

@csrf_exempt
def Supplier_Edit(request,nid):
    try:
        if request.method == "POST":
            suppkey = request.POST.get('s_suppkey')
            name = request.POST.get('s_name')
            address = request.POST.get('s_address')
            tem_nationkey = request.POST.get('s_nationkey')
            nation = models.Nation.objects.get(n_nationkey=tem_nationkey)
            phone = request.POST.get('s_phone')

            mobile_regex = r'^1[34578]\d{9}$'
            p = re.compile(mobile_regex)
            if not p.match(phone):
                return render(request, 'error.html', {'msg': '请输入正确手机号'})

            acctbal = request.POST.get('s_acctbal')
            if acctbal == "":
                acctbal = "0"

            number_regex = r'^[+]{0,1}(\d+)$|^[+]{0,1}(\d+\.\d+)$'
            p = re.compile(number_regex)
            if not p.match(acctbal):
                return render(request, "error.html", {"msg": "请输入正确的可用余额"})

            comment = request.POST.get('s_comment')
            obj = models.Supplier(s_suppkey=suppkey, s_name=name, s_address=address,
                                  s_nationkey=nation, s_phone=phone, s_acctbal=acctbal,
                                  s_comment=comment)
            obj.save()
            return HttpResponseRedirect("/DBHW/supplierlist/")


        else:
            obj = models.Supplier.objects.filter(s_suppkey=nid).first()
            nation_list = models.Nation.objects.all().values_list("n_nationkey", "n_name")
            return render(request, 'supplieredit.html', {"obj": obj, "nation_list": nation_list})
    except:
        return render(request, "error.html", {"msg": "您的输入有误，编辑失败！"})

def Supplier_delete(request, nid):
    try:
        models.Supplier.objects.filter(s_suppkey=nid).delete()
        return render(request, 'supplierdelete.html')
    except:
        return render(request, "error.html", {"msg": "删除失败！"})


@csrf_exempt
def Supplier_view(request, nid):
    obj = models.Supplier.objects.filter(s_suppkey=nid).first()
    return render(request, 'supplierview.html', {"obj": obj})

@csrf_exempt
def Supplier_Add(request):
    try:
        if request.method == "POST":
            suppkey = request.POST.get('s_suppkey')
            name = request.POST.get('s_name')
            address = request.POST.get('s_address')
            tem_nationkey = request.POST.get('s_nationkey')
            nation = models.Nation.objects.get(n_nationkey=tem_nationkey)
            phone = request.POST.get('s_phone')
            mobile_regex = r'^1[34578]\d{9}$' #手机号正则表达
            p = re.compile(mobile_regex)
            if not p.match(phone) :
                return render(request, 'error.html', {'msg': '请输入正确联系方式'})

            acctbal = request.POST.get('s_acctbal')
            if acctbal =='':
                acctbal = "0"
            number_regex = r'^[+]{0,1}(\d+)$|^[+]{0,1}(\d+\.\d+)$'
            p = re.compile(number_regex)
            if not p.match(acctbal):
                return render(request, "error.html", {"msg": "请输入正确的可用余额"})

            comment = request.POST.get('s_comment')
            obj=models.Supplier(s_suppkey=suppkey,s_name = name,s_address=address,
            s_nationkey=nation,s_phone=phone,s_acctbal=acctbal,
            s_comment=comment)
            obj.save()
            return HttpResponseRedirect("/DBHW/supplierlist/")

        else:
            nation_list = models.Nation.objects.all().values_list("n_nationkey", "n_name")
            return render(request, 'supplieradd.html', {"nation_list": nation_list})
    except:
        return render(request, "error.html", {"msg": "您的输入有误，添加失败！"})