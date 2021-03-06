# Generated by Django 2.0 on 2017-12-31 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rickshaw', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rickshaw_example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rickshaw',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Driver'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='product',
            field=models.ForeignKey(on_delete=None, to='rickshaw_example.Product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='rickshaw',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rickshaw.Rickshaw', to_field='uuid', verbose_name='Rickshaw'),
        ),
    ]
