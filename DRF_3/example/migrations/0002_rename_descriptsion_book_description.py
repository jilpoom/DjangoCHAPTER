# Generated by Django 3.2.10 on 2022-08-13 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='descriptsion',
            new_name='description',
        ),
    ]