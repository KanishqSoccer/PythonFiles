# Generated by Django 3.0.5 on 2020-05-06 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0012_auto_20200505_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
