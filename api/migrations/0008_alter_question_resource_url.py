# Generated by Django 3.2.7 on 2021-10-03 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_question_resource_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='resource_url',
            field=models.URLField(max_length=2000),
        ),
    ]
