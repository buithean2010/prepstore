# Generated by Django 3.1.5 on 2021-01-09 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_products_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='img',
            new_name='img_url',
        ),
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
