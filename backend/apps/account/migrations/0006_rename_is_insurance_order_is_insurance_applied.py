# Generated by Django 3.2.4 on 2024-08-04 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_order_referring_phys'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='is_insurance',
            new_name='is_insurance_applied',
        ),
    ]
