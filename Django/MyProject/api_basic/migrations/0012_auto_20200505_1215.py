# Generated by Django 3.0.5 on 2020-05-05 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0011_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(default='', max_length=100000),
        ),
    ]
