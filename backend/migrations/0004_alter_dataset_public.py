# Generated by Django 4.1.7 on 2023-03-01 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_rename_datecreated_dataset_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]