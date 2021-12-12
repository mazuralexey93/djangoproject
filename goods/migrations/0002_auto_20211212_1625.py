# Generated by Django 3.2.1 on 2021-12-12 16:25

from django.db import migrations


def forward_code(apps, se):
    GoodItem = apps.get_model('goods', 'GoodItem')
    alias = se.connection.alias
    GoodItem.objects.using(alias).bulk_create([
        GoodItem(title='Sofa', price=10000, vendor='Firma A'),
        GoodItem(title='Chair', price=5000, vendor='Firma B'),
        GoodItem(title='Table', price=7500, vendor='Firma A'),
        GoodItem(title='Bed', price=100000, vendor='Firma C'),
    ])


def reverse_code():
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(code=forward_code, reverse_code=reverse_code)
    ]
