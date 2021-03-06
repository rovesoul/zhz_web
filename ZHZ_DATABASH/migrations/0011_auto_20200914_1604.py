# Generated by Django 2.2 on 2020-09-14 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZHZ_DATABASH', '0010_auto_20200914_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luggagecompany',
            name='certificates',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='资质证书'),
        ),
        migrations.AlterField(
            model_name='luggagecompany',
            name='company_name',
            field=models.CharField(max_length=200, unique=True, verbose_name='公司名称-必填'),
        ),
        migrations.AlterField(
            model_name='luggagecompany',
            name='legal_person',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='法人-必填'),
        ),
        migrations.AlterField(
            model_name='luggagecompany',
            name='patents_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='专利名称'),
        ),
    ]
