# Generated by Django 4.2.4 on 2023-08-20 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='summary',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]