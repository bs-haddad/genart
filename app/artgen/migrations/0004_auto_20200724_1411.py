# Generated by Django 3.0.8 on 2020-07-24 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artgen', '0003_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='filepath',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='art',
            name='image_1',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='art',
            name='image_2',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
