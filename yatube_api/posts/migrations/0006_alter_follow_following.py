# Generated by Django 3.2.16 on 2024-03-01 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20240229_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.TextField(),
        ),
    ]
