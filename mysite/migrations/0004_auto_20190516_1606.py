# Generated by Django 2.2.1 on 2019-05-16 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_product_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='edit_date',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='上传时间'),
        ),
    ]
