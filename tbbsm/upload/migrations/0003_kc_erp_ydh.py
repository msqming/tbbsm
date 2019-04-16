# Generated by Django 2.1 on 2019-04-16 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_kc_erp_splr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kc_Erp_Ydh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cjsj', models.CharField(max_length=32, verbose_name='创建时间')),
                ('yjdh', models.CharField(max_length=32, verbose_name='预计到货')),
                ('cqts', models.FloatField(verbose_name='超期天数')),
                ('danhao', models.CharField(max_length=32, verbose_name='单号')),
                ('ks', models.CharField(max_length=64, verbose_name='客商')),
                ('spbm', models.CharField(max_length=64, verbose_name='商品编码')),
                ('spmc', models.CharField(max_length=256, verbose_name='商品名称')),
                ('ywy', models.CharField(max_length=32, verbose_name='业务员')),
                ('kds', models.IntegerField(verbose_name='开单数')),
                ('danjia', models.FloatField(verbose_name='单价')),
                ('jine', models.FloatField(verbose_name='金额')),
                ('ydh', models.FloatField(verbose_name='已到货')),
                ('wds', models.IntegerField(verbose_name='未到数')),
                ('wdje', models.FloatField(verbose_name='未到金额')),
            ],
        ),
    ]