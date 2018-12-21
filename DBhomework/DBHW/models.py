# Create your models here.
from django.db import models


class Customer(models.Model):
    c_custkey = models.IntegerField(db_column='C_CUSTKEY', primary_key=True)  # Field name made lowercase.
    c_name = models.CharField(db_column='C_NAME', max_length=25, blank=True, null=True)  # Field name made lowercase.
    c_address = models.CharField(db_column='C_ADDRESS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    c_nationkey = models.ForeignKey('Nation', models.DO_NOTHING, db_column='C_NATIONKEY', blank=True, null=True)  # Field name made lowercase.
    c_phone = models.CharField(db_column='C_PHONE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    c_acctbal = models.FloatField(db_column='C_ACCTBAL', blank=True, null=True)  # Field name made lowercase.
    c_mktsegment = models.CharField(db_column='C_MKTSEGMENT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    c_comment = models.CharField(db_column='C_COMMENT', max_length=17, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class Lineitem(models.Model):
    l_orderkey = models.IntegerField(db_column='L_ORDERKEY', primary_key=True)  # Field name made lowercase.
    l_partkey = models.ForeignKey('Partsupp', models.DO_NOTHING,related_name='l_partkey_Lineitem' ,db_column='L_PARTKEY', blank=True, null=True)  # Field name made lowercase.
    l_suppkey = models.ForeignKey('Partsupp', models.DO_NOTHING,related_name='l_suppkey_Lineitem', db_column='L_SUPPKEY', blank=True, null=True)  # Field name made lowercase.
    l_linenumber = models.IntegerField(db_column='L_LINENUMBER')  # Field name made lowercase.
    l_quantity = models.FloatField(db_column='L_QUANTITY', blank=True, null=True)  # Field name made lowercase.
    l_extendedprice = models.FloatField(db_column='L_EXTENDEDPRICE', blank=True, null=True)  # Field name made lowercase.
    l_discount = models.FloatField(db_column='L_DISCOUNT', blank=True, null=True)  # Field name made lowercase.
    l_tax = models.FloatField(db_column='L_TAX', blank=True, null=True)  # Field name made lowercase.
    l_returnflag = models.CharField(db_column='L_RETURNFLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    l_linestatus = models.CharField(db_column='L_LINESTATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    l_shipdate = models.DateField(db_column='L_SHIPDATE', blank=True, null=True)  # Field name made lowercase.
    l_commitdate = models.DateField(db_column='L_COMMITDATE', blank=True, null=True)  # Field name made lowercase.
    l_receiptdate = models.DateField(db_column='L_RECEIPTDATE', blank=True, null=True)  # Field name made lowercase.
    l_shipinstruct = models.CharField(db_column='L_SHIPINSTRUCT', max_length=25, blank=True, null=True)  # Field name made lowercase.
    l_shipmode = models.CharField(db_column='L_SHIPMODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    l_comment = models.CharField(db_column='L_COMMENT', max_length=44, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lineitem'
        unique_together = (('l_orderkey', 'l_linenumber'),)


class Nation(models.Model):
    n_nationkey = models.IntegerField(db_column='N_NATIONKEY', primary_key=True)  # Field name made lowercase.
    n_name = models.CharField(db_column='N_NAME', max_length=25, blank=True, null=True)  # Field name made lowercase.
    n_regionkey = models.ForeignKey('Region', models.DO_NOTHING, db_column='N_REGIONKEY', blank=True, null=True)  # Field name made lowercase.
    n_comment = models.CharField(db_column='N_COMMENT', max_length=152, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nation'


class Orders(models.Model):
    o_orderkey = models.IntegerField(db_column='O_ORDERKEY', primary_key=True)  # Field name made lowercase.
    o_custkey = models.ForeignKey(Customer, models.DO_NOTHING, db_column='O_CUSTKEY', blank=True, null=True)  # Field name made lowercase.
    o_orderstatus = models.CharField(db_column='O_ORDERSTATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    o_totalprice = models.FloatField(db_column='O_TOTALPRICE', blank=True, null=True)  # Field name made lowercase.
    o_orderdate = models.DateField(db_column='O_ORDERDATE', blank=True, null=True)  # Field name made lowercase.
    o_orderpriority = models.CharField(db_column='O_ORDERPRIORITY', max_length=15, blank=True, null=True)  # Field name made lowercase.
    o_clerk = models.CharField(db_column='O_CLERK', max_length=15, blank=True, null=True)  # Field name made lowercase.
    o_shippriority = models.IntegerField(db_column='O_SHIPPRIORITY', blank=True, null=True)  # Field name made lowercase.
    o_comment = models.CharField(db_column='O_COMMENT', max_length=79, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Part(models.Model):
    p_partkey = models.IntegerField(db_column='P_PARTKEY', primary_key=True)  # Field name made lowercase.
    p_name = models.CharField(db_column='P_NAME', max_length=55, blank=True, null=True)  # Field name made lowercase.
    p_emfgr = models.CharField(db_column='P_EMFGR', max_length=25, blank=True, null=True)  # Field name made lowercase.
    p_brand = models.CharField(db_column='P_BRAND', max_length=10, blank=True, null=True)  # Field name made lowercase.
    p_type = models.CharField(db_column='P_TYPE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    p_size = models.IntegerField(db_column='P_SIZE', blank=True, null=True)  # Field name made lowercase.
    p_container = models.CharField(db_column='P_CONTAINER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    p_retailprice = models.FloatField(db_column='P_RETAILPRICE', blank=True, null=True)  # Field name made lowercase.
    p_comment = models.CharField(db_column='P_COMMENT', max_length=23, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'part'


class Partsupp(models.Model):
    ps_partkey = models.ForeignKey(Part, models.DO_NOTHING, related_name='l_partkey_ps_partkey',db_column='PS_PARTKEY', primary_key=True)  # Field name made lowercase.
    ps_suppkey = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='PS_SUPPKEY')  # Field name made lowercase.
    ps_availqty = models.IntegerField(db_column='PS_AVAILQTY', blank=True, null=True)  # Field name made lowercase.
    ps_supplycost = models.FloatField(db_column='PS_SUPPLYCOST', blank=True, null=True)  # Field name made lowercase.
    ps_comment = models.CharField(db_column='PS_COMMENT', max_length=199, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'partsupp'
        unique_together = (('ps_partkey', 'ps_suppkey'),)


class Region(models.Model):
    r_regionkey = models.IntegerField(db_column='R_REGIONKEY', primary_key=True)  # Field name made lowercase.
    r_name = models.CharField(db_column='R_NAME', max_length=25, blank=True, null=True)  # Field name made lowercase.
    r_comment = models.CharField(db_column='R_COMMENT', max_length=152, blank=True, null=True)  # Field name made lowercase.
    ps_supplycost = models.FloatField(db_column='PS_SUPPLYCOST', blank=True, null=True)  # Field name made lowercase.
    ps_comment = models.CharField(db_column='PS_COMMENT', max_length=199, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'region'


class Supplier(models.Model):
    s_suppkey = models.IntegerField(db_column='S_SUPPKEY', primary_key=True)  # Field name made lowercase.
    s_name = models.CharField(db_column='S_NAME', max_length=25, blank=True, null=True)  # Field name made lowercase.
    s_address = models.CharField(db_column='S_ADDRESS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    s_nationkey = models.ForeignKey(Nation, models.DO_NOTHING, db_column='S_NATIONKEY', blank=True, null=True)  # Field name made lowercase.
    s_phone = models.CharField(db_column='S_PHONE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    s_acctbal = models.FloatField(db_column='S_ACCTBAL', blank=True, null=True)  # Field name made lowercase.
    s_comment = models.CharField(db_column='S_COMMENT', max_length=101, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplier'