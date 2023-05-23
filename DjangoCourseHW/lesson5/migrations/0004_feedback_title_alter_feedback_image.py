# Generated by Django 4.2 on 2023-05-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson5', '0003_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='title',
            field=models.CharField(default='Some title', max_length=255),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='image',
            field=models.ImageField(upload_to='lesson5/static/img/feedback_images'),
        ),
    ]