# Generated by Django 2.1 on 2019-04-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kc_Erp_Kccx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riqi', models.DateField(verbose_name='日期')),
                ('spbm', models.CharField(max_length=64, verbose_name='商品编码')),
                ('leibie', models.CharField(max_length=32, verbose_name='类别')),
                ('pinpai', models.CharField(max_length=32, verbose_name='品牌')),
                ('spmc', models.CharField(max_length=128, verbose_name='商品名称')),
                ('zsl', models.IntegerField(verbose_name='总数量')),
                ('kxs', models.FloatField(verbose_name='可销数')),
                ('djcb', models.FloatField(verbose_name='单价成本')),
                ('je', models.FloatField(verbose_name='金额')),
                ('cwkc', models.IntegerField(verbose_name='财务库存')),
                ('hsbz', models.FloatField(verbose_name='含税比重')),
                ('hsxj', models.FloatField(verbose_name='含税限价')),
                ('wsxj', models.FloatField(verbose_name='未税限价')),
                ('dairu', models.FloatField(verbose_name='待入')),
                ('daichu', models.FloatField(verbose_name='待出')),
                ('sczt', models.FloatField(verbose_name='生产在途')),
                ('daishen', models.FloatField(verbose_name='待审')),
                ('huola', models.CharField(max_length=64, verbose_name='货拉')),
                ('zl', models.FloatField(verbose_name='重量')),
                ('xz', models.CharField(max_length=16, verbose_name='性质')),
                ('zhcgsj', models.CharField(max_length=32, verbose_name='最后采购时间')),
                ('hsyj', models.FloatField(verbose_name='含税预计')),
                ('wsyj', models.FloatField(verbose_name='未税预计')),
            ],
        ),
    ]