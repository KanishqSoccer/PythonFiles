# Generated by Django 3.0.5 on 2020-05-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0005_auto_20200504_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]