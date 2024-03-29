# Generated by Django 2.2 on 2021-03-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZHZ_DATABASH', '0027_auto_20210315_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcompanyproject',
            name='money_Bid_security_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, max_length=60, null=True, verbose_name='投标保证金'),
        ),
        migrations.AddField(
            model_name='newcompanyproject',
            name='money_Performance_bond',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, max_length=60, null=True, verbose_name='履约保证金'),
        ),
        migrations.AddField(
            model_name='newcompanyproject',
            name='money_agency_service_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, max_length=60, null=True, verbose_name='招标代理服务费'),
        ),
        migrations.AddField(
            model_name='newcompanyproject',
            name='money_price_control',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, max_length=60, null=True, verbose_name='招标控制价'),
        ),
        migrations.AddField(
            model_name='newcompanyproject',
            name='money_transaction_service_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, max_length=60, null=True, verbose_name='交易服务费'),
        ),
        migrations.AddField(
            model_name='newcompanyproject',
            name='money_use_room_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, max_length=60, null=True, verbose_name='开标室费用'),
        ),
        migrations.AddField(
            model_name='newcompanyproject',
            name='monney_buy_biddingDoc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, max_length=60, null=True, verbose_name='招标文件费用'),
        ),
    ]
