# Generated by Django 3.0.1 on 2020-01-23 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='useremail',
        ),
    ]
