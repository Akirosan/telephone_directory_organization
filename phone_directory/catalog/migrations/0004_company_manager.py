# Generated by Django 3.2.9 on 2021-12-05 17:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0003_auto_20211203_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='manager',
            field=models.ManyToManyField(related_name='myorganisations', to=settings.AUTH_USER_MODEL, verbose_name='Управляющий'),
        ),
    ]
