# Generated by Django 2.1.5 on 2019-12-17 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191213_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='nombre',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set(),
        ),
    ]
