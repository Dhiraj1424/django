# Generated by Django 3.2.4 on 2021-06-16 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='last_name',
            new_name='phone',
        ),
    ]
