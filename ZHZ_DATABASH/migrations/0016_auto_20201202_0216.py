# Generated by Django 2.2 on 2020-12-01 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZHZ_DATABASH', '0015_thing_end_line'),
    ]

    operations = [
        migrations.AddField(
            model_name='contracts',
            name='manager_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='项目经理'),
        ),
        migrations.AddField(
            model_name='contracts',
            name='proof',
            field=models.CharField(blank=True, choices=[('有', '有'), ('无', '无')], max_length=20, null=True, verbose_name='项目经理业绩证明'),
        ),
    ]
