# Generated by Django 5.1.1 on 2024-09-18 17:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RenameField(
            model_name='products',
            old_name='name',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='username',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
