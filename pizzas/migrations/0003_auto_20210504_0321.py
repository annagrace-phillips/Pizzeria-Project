# Generated by Django 3.2 on 2021-05-04 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_auto_20210504_0306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name_plural': 'Toppings'},
        ),
        migrations.RemoveField(
            model_name='topping',
            name='image',
        ),
    ]
