# Generated by Django 3.0.6 on 2020-09-19 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200918_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_credits',
            field=models.TextField(default=''),
        ),
    ]
