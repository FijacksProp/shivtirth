# Generated by Django 5.1.1 on 2025-05-10 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shivtirth_app', '0004_alter_enquire_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquire',
            name='name',
        ),
    ]
