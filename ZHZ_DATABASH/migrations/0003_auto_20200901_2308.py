# Generated by Django 2.2 on 2020-09-01 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZHZ_DATABASH', '0002_auto_20200901_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=200, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='person',
            name='idNO',
            field=models.CharField(max_length=18, null=True, verbose_name='身份证号'),
        ),
    ]
