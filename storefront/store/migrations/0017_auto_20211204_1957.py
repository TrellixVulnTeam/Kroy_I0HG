# Generated by Django 3.2.9 on 2021-12-04 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0016_bid_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='bought',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='sold',
        ),
        migrations.RemoveField(
            model_name='product',
            name='active',
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]