# Generated by Django 2.2 on 2020-09-11 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZHZ_DATABASH', '0008_auto_20200911_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chinesename',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='中文名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='登录用户名'),
        ),
    ]
