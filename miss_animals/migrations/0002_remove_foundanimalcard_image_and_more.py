# Generated by Django 5.0.6 on 2024-06-09 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miss_animals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foundanimalcard',
            name='image',
        ),
        migrations.AlterField(
            model_name='foundanimalcard',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
