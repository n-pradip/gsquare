# Generated by Django 4.0.5 on 2022-06-28 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('room',)},
        ),
    ]