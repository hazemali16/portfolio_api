# Generated by Django 5.0.4 on 2024-04-29 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='image',
            field=models.FileField(upload_to='hero/'),
        ),
    ]