# Generated by Django 5.1.3 on 2024-11-10 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerdescription',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]