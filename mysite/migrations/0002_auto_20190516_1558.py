# Generated by Django 2.2.1 on 2019-05-16 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='kucun',
        ),
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.PositiveIntegerField(default=0, verbose_name='库存'),
        ),
    ]
