# Generated by Django 5.1.3 on 2024-11-09 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product_alter_ownerdescription_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
