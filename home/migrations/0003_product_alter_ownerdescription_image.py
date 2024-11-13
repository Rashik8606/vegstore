# Generated by Django 5.1.3 on 2024-11-09 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_ownerdescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('net_weight', models.CharField(max_length=50)),
                ('storage_method', models.TextField()),
                ('discount_percentage', models.PositiveIntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
            ],
        ),
        migrations.AlterField(
            model_name='ownerdescription',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
