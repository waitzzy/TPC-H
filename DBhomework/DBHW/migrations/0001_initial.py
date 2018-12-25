# Generated by Django 2.1.2 on 2018-12-25 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('c_custkey', models.IntegerField(db_column='C_CUSTKEY', primary_key=True, serialize=False)),
                ('c_name', models.CharField(blank=True, db_column='C_NAME', max_length=25, null=True)),
                ('c_address', models.CharField(blank=True, db_column='C_ADDRESS', max_length=40, null=True)),
                ('c_phone', models.CharField(blank=True, db_column='C_PHONE', max_length=15, null=True)),
                ('c_acctbal', models.FloatField(blank=True, db_column='C_ACCTBAL', null=True)),
                ('c_mktsegment', models.CharField(blank=True, db_column='C_MKTSEGMENT', max_length=10, null=True)),
                ('c_comment', models.CharField(blank=True, db_column='C_COMMENT', max_length=17, null=True)),
            ],
            options={
                'db_table': 'customer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Lineitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_orderkey', models.IntegerField(db_column='L_ORDERKEY')),
                ('l_linenumber', models.IntegerField(db_column='L_LINENUMBER')),
                ('l_quantity', models.FloatField(blank=True, db_column='L_QUANTITY', null=True)),
                ('l_extendedprice', models.FloatField(blank=True, db_column='L_EXTENDEDPRICE', null=True)),
                ('l_discount', models.FloatField(blank=True, db_column='L_DISCOUNT', null=True)),
                ('l_tax', models.FloatField(blank=True, db_column='L_TAX', null=True)),
                ('l_returnflag', models.CharField(blank=True, db_column='L_RETURNFLAG', max_length=1, null=True)),
                ('l_linestatus', models.CharField(blank=True, db_column='L_LINESTATUS', max_length=1, null=True)),
                ('l_shipdate', models.DateField(blank=True, db_column='L_SHIPDATE', null=True)),
                ('l_commitdate', models.DateField(blank=True, db_column='L_COMMITDATE', null=True)),
                ('l_receiptdate', models.DateField(blank=True, db_column='L_RECEIPTDATE', null=True)),
                ('l_shipinstruct', models.CharField(blank=True, db_column='L_SHIPINSTRUCT', max_length=25, null=True)),
                ('l_shipmode', models.CharField(blank=True, db_column='L_SHIPMODE', max_length=10, null=True)),
                ('l_comment', models.CharField(blank=True, db_column='L_COMMENT', max_length=44, null=True)),
            ],
            options={
                'db_table': 'lineitem',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('n_nationkey', models.IntegerField(db_column='N_NATIONKEY', primary_key=True, serialize=False)),
                ('n_name', models.CharField(blank=True, db_column='N_NAME', max_length=25, null=True)),
                ('n_comment', models.CharField(blank=True, db_column='N_COMMENT', max_length=152, null=True)),
            ],
            options={
                'db_table': 'nation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('o_orderkey', models.IntegerField(db_column='O_ORDERKEY', primary_key=True, serialize=False)),
                ('o_orderstatus', models.CharField(blank=True, db_column='O_ORDERSTATUS', max_length=1, null=True)),
                ('o_totalprice', models.FloatField(blank=True, db_column='O_TOTALPRICE', null=True)),
                ('o_orderdate', models.DateField(blank=True, db_column='O_ORDERDATE', null=True)),
                ('o_orderpriority', models.CharField(blank=True, db_column='O_ORDERPRIORITY', max_length=15, null=True)),
                ('o_clerk', models.CharField(blank=True, db_column='O_CLERK', max_length=15, null=True)),
                ('o_shippriority', models.IntegerField(blank=True, db_column='O_SHIPPRIORITY', null=True)),
                ('o_comment', models.CharField(blank=True, db_column='O_COMMENT', max_length=79, null=True)),
                ('o_custkey', models.ForeignKey(blank=True, db_column='O_CUSTKEY', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='DBHW.Customer')),
            ],
            options={
                'db_table': 'orders',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('p_partkey', models.IntegerField(db_column='P_PARTKEY', primary_key=True, serialize=False)),
                ('p_name', models.CharField(blank=True, db_column='P_NAME', max_length=55, null=True)),
                ('p_emfgr', models.CharField(blank=True, db_column='P_EMFGR', max_length=25, null=True)),
                ('p_brand', models.CharField(blank=True, db_column='P_BRAND', max_length=10, null=True)),
                ('p_type', models.CharField(blank=True, db_column='P_TYPE', max_length=25, null=True)),
                ('p_size', models.IntegerField(blank=True, db_column='P_SIZE', null=True)),
                ('p_container', models.CharField(blank=True, db_column='P_CONTAINER', max_length=10, null=True)),
                ('p_retailprice', models.FloatField(blank=True, db_column='P_RETAILPRICE', null=True)),
                ('p_comment', models.CharField(blank=True, db_column='P_COMMENT', max_length=23, null=True)),
            ],
            options={
                'db_table': 'part',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Partsupp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ps_availqty', models.IntegerField(blank=True, db_column='PS_AVAILQTY', null=True)),
                ('ps_supplycost', models.FloatField(blank=True, db_column='PS_SUPPLYCOST', null=True)),
                ('ps_comment', models.CharField(blank=True, db_column='PS_COMMENT', max_length=199, null=True)),
                ('ps_partkey', models.ForeignKey(db_column='PS_PARTKEY', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ps_partkey_Partsupp', to='DBHW.Part')),
            ],
            options={
                'db_table': 'partsupp',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('r_regionkey', models.IntegerField(db_column='R_REGIONKEY', primary_key=True, serialize=False)),
                ('r_name', models.CharField(blank=True, db_column='R_NAME', max_length=25, null=True)),
                ('r_comment', models.CharField(blank=True, db_column='R_COMMENT', max_length=152, null=True)),
                ('ps_supplycost', models.FloatField(blank=True, db_column='PS_SUPPLYCOST', null=True)),
                ('ps_comment', models.CharField(blank=True, db_column='PS_COMMENT', max_length=199, null=True)),
            ],
            options={
                'db_table': 'region',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('s_suppkey', models.IntegerField(db_column='S_SUPPKEY', primary_key=True, serialize=False)),
                ('s_name', models.CharField(blank=True, db_column='S_NAME', max_length=25, null=True)),
                ('s_address', models.CharField(blank=True, db_column='S_ADDRESS', max_length=40, null=True)),
                ('s_phone', models.CharField(blank=True, db_column='S_PHONE', max_length=15, null=True)),
                ('s_acctbal', models.FloatField(blank=True, db_column='S_ACCTBAL', null=True)),
                ('s_comment', models.CharField(blank=True, db_column='S_COMMENT', max_length=101, null=True)),
                ('s_nationkey', models.ForeignKey(blank=True, db_column='S_NATIONKEY', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='DBHW.Nation')),
            ],
            options={
                'db_table': 'supplier',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='partsupp',
            name='ps_suppkey',
            field=models.ForeignKey(db_column='PS_SUPPKEY', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ps_suppkey_Partsupp', to='DBHW.Supplier'),
        ),
        migrations.AddField(
            model_name='nation',
            name='n_regionkey',
            field=models.ForeignKey(blank=True, db_column='N_REGIONKEY', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='DBHW.Region'),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='l_partkey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='l_partkey_Lineitem', to='DBHW.Part'),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='l_suppkey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='l_suppkey_Lineitem', to='DBHW.Supplier'),
        ),
        migrations.AddField(
            model_name='customer',
            name='c_nationkey',
            field=models.ForeignKey(blank=True, db_column='C_NATIONKEY', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='DBHW.Nation'),
        ),
        migrations.AlterUniqueTogether(
            name='partsupp',
            unique_together={('ps_partkey', 'ps_suppkey')},
        ),
        migrations.AlterUniqueTogether(
            name='lineitem',
            unique_together={('l_orderkey', 'l_linenumber')},
        ),
    ]
