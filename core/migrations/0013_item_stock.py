# Generated by Django 2.2.14 on 2020-07-21 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200721_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='stock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
