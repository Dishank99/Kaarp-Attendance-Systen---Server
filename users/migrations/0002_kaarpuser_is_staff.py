# Generated by Django 3.1.2 on 2021-01-27 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kaarpuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
