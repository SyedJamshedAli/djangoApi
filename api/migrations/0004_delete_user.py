# Generated by Django 5.0.2 on 2024-02-24 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
