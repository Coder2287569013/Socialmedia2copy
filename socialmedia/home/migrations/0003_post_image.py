# Generated by Django 3.2.21 on 2023-11-11 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20231021_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='C:\\Users\\Admin\\Desktop\\Python\\socialmedia\\socialmedia\\media\\меч в камне.png', null=True, upload_to='post/'),
        ),
    ]