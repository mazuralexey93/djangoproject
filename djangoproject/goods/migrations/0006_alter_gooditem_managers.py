# Generated by Django 4.0 on 2021-12-20 23:37

import django.contrib.sites.managers
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_gooditem_site'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='gooditem',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager('site')),
            ],
        ),
    ]
