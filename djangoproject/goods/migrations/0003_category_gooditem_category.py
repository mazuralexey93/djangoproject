# Generated by Django 4.0 on 2021-12-15 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20211212_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название Категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Картегории',
            },
        ),
        migrations.AddField(
            model_name='gooditem',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.category'),
        ),
    ]
