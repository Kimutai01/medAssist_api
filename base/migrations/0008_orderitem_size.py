# Generated by Django 4.2.3 on 2023-07-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_orderitem_image_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
