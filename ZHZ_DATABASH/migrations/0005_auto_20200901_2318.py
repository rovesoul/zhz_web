# Generated by Django 2.2 on 2020-09-01 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZHZ_DATABASH', '0004_auto_20200901_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradecontracts',
            name='c_time',
            field=models.DateField(default='2020-08-01', null=True, verbose_name='记录时间'),
        ),
    ]
