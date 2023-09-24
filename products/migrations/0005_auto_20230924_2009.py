# Generated by Django 3.2.21 on 2023-09-24 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.product'),
        ),
    ]
