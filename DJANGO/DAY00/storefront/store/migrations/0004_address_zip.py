# Generated by Django 5.0.7 on 2024-07-18 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
