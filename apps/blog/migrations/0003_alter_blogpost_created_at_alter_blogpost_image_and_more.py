# Generated by Django 5.0.6 on 2024-07-04 19:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(upload_to='media/blog_images/'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='updated_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
