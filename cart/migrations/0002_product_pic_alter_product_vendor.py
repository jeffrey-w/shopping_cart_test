# Generated by Django 4.2.11 on 2024-04-22 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pic',
            field=models.ImageField(default=None, null=True, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.CharField(max_length=32),
        ),
    ]
