# Generated by Django 3.2.9 on 2021-12-03 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffer',
            name='staffer',
            field=models.CharField(max_length=100),
        ),
    ]
