# Generated by Django 5.0.6 on 2024-06-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miss_animals', '0006_alter_foundanimalcard_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foundanimalcard',
            name='image',
            field=models.ImageField(default='test.jpg', upload_to='media/'),
        ),
    ]
