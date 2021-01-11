# Generated by Django 2.2 on 2021-01-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZHZ_DATABASH', '0017_auto_20210103_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='contracts',
            name='add_money',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='contracts',
            name='confirm_paper',
            field=models.CharField(blank=True, choices=[('有', '有'), ('无', '无')], max_length=100, null=True, verbose_name='中标通知书'),
        ),
        migrations.AddField(
            model_name='contracts',
            name='project_closed',
            field=models.CharField(blank=True, choices=[('是', '是'), ('否', '否'), ('已作废', '已作废')], max_length=10, null=True, verbose_name='项目是否闭合'),
        ),
        migrations.AlterField(
            model_name='contracts',
            name='aready_get_income',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='已收款金额'),
        ),
        migrations.AlterField(
            model_name='contracts',
            name='project_status',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='项目当前状态'),
        ),
    ]