from django.urls import path,re_path,include
from DBHW.views import *
app_name = 'DBHW'
urlpatterns = [
<<<<<<< HEAD
    re_path(r'^customerlist/',Customer_list,name='customerlist'),

=======
>>>>>>> 123323a3612af5a0c78095787c9cff83ce521249
    re_path(r'^nationlist/',Nation_list,name='nationlist'),
    re_path(r'^nationedit-(?P<nid>\d+)/',Nation_Edit,name='nationedit'),
    re_path(r'^nationadd/',Nation_add,name='nationadd'),
    re_path(r'^nationview-(?P<nid>\d+)/',Nation_view,name='nationview'),
    re_path(r'^nationdelete-(?P<nid>\d+)/',Nation_delete,name='nationdelete'),
<<<<<<< HEAD

    re_path(r'^regionlist/',Region_list,name='regionlist'),
    re_path(r'^regionedit-(?P<nid>\d+)/',)
=======
    re_path(r'^customerlist/', Customer_list, name='customerlist'),
    re_path(r'^customeredit-(?P<nid>\d+)/', Customer_Edit, name='customeredit'),
    re_path(r'^customeradd/', Customer_add, name='customeradd'),
    re_path(r'^customerview-(?P<nid>\d+)/', Customer_view, name='customerview'),
    re_path(r'^customerdelete-(?P<nid>\d+)/', Customer_delete, name='customerdelete'),
>>>>>>> 123323a3612af5a0c78095787c9cff83ce521249
 ]