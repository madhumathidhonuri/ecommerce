# Generated by Django 5.1.5 on 2025-02-15 04:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rogue', '0012_remove_footwear_color'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
