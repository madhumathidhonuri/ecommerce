# Generated by Django 5.1.5 on 2025-02-08 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rogue', '0011_alter_footwear_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footwear',
            name='color',
        ),
    ]
