# Generated by Django 3.2.18 on 2023-08-18 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrichment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enrichmentactivity',
            options={'ordering': ['time'], 'verbose_name_plural': 'enrichment activities'},
        ),
    ]