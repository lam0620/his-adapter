# Generated by Django 3.2.4 on 2024-08-06 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_order_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.CharField(max_length=14, verbose_name='order time'),
        ),
    ]
