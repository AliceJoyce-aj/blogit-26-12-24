# Generated by Django 5.1.4 on 2024-12-30 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdetails',
            name='blog_author',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
    ]