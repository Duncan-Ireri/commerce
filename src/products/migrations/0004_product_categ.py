# Generated by Django 2.1 on 2018-08-15 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('products', '0003_auto_20180814_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categ',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Categories'),
        ),
    ]