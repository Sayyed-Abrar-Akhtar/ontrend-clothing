# Generated by Django 3.0.1 on 2020-02-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20200210_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='customize',
            name='reviewbanner',
            field=models.ImageField(default='hero.jpg', upload_to='images/'),
        ),
    ]
