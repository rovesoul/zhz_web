# Generated by Django 2.2 on 2021-04-21 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZHZ_DATABASH', '0031_delete_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='np_note',
            name='notename',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='更新人员'),
        ),
    ]
